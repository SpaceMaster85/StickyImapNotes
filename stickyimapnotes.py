from xmlrpc.client import DateTime
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtMultimedia import *
from PySide2.QtMultimediaWidgets import *


from MainWindow import Ui_MainWindow

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


import os, sys, configparser, imaplib, re,  PIL.Image, PIL.ImageTk, socket
import email.parser, email.header, email.utils, email.message
from PIL import Image
import base64
from io import BytesIO
import time
import html
import datetime
import uuid
import html2text


Base = declarative_base()

class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, unique=True)
    xuuid= Column(String(1000), nullable=True)
    timestamp = Column(DateTime(timezone = True), nullable=False)
    subject = Column(String(1000), nullable=False)
    type = Column(String(1000), nullable=False)
    deleteNote = Column(Boolean, unique=False, default=False)
    newNote = Column(Boolean, unique=False, default=False)
    sync = Column(Boolean, unique=False, default=False)
    text = Column(String(1000), nullable=True)
    x = Column(Integer, nullable=False, default=0)
    y = Column(Integer, nullable=False, default=0)
    w = Column(Integer, nullable=False, default=0)
    h = Column(Integer, nullable=False, default=0)

engine = create_engine('sqlite:///notes.db', connect_args={'check_same_thread': False})
# Initalize the database if it is not already.
#if not engine.dialect.has_table(engine, "note"):
Base.metadata.create_all(engine)

# Create a session to handle updates.
Session = sessionmaker(bind=engine)
session = Session()

_ACTIVE_NOTES = {}

def create_new_note():
    MainWindow()




class ImapNotes():
    def __init__(self, parent = None):
        #QThread.__init__(self, parent)
        self.imap = []
        self.notes = []
        self.data = []
        self.timer=QTimer()
        self.timer.timeout.connect(self.getNotes)
        self.user =""
        self.startup=True
        self.firstConnect = True
        #self.exiting= False
        self.getNotes()




    def open(self):
        try:
            config = configparser.ConfigParser()
            print(os.path.join(os.getcwd(),"imapnotes.ini"))
            config.read(os.path.join(os.getcwd(),"imapnotes.ini"))

            host = config.get("connection", "host")
            socket.setdefaulttimeout(1)
            if config.has_option("connection", "port"):
                self.imap = imaplib.IMAP4_SSL(host, config.get("connection", "port"))
            else:
                self.imap = imaplib.IMAP4_SSL(host)

            self.imap.login(config.get("connection", "user"),
                       config.get("connection", "pass"))
            self.imap.select("Notes")
            self.user= config.get("connection", "user")
            for obj in session.query(Note).all():
                obj.sync=False
                session.add(obj)
            session.commit()

        except Exception as e:
            if self.firstConnect:
                QMessageBox.critical(None, "Connection failed","Cannot connect to IMAPS server:\n%s" % (str(e)))
                self.firstConnect = False
            #sys.exit(1)
            

    def getNotes(self):

        try:
            self.imap.noop()
        except Exception as e:
            try:
                self.imap.open()
            except Exception as e:
                self.open()
                self.timer.start(5000)
                return
        # search returns tuple with list
        notes_numbers = self.imap.uid("search", None, "ALL")[1][0].decode().replace(" ", ",")
        # imap fetch expects comma separated list
        newWindow = False
        for obj in session.query(Note).all():
            obj.sync=False
            session.add(obj)
        #session.commit()


        if len(notes_numbers) > 0:
            notes_list = self.imap.uid("fetch", notes_numbers, "RFC822")
            uid_re = re.compile(r"UID\s+(\d+)")
            for part in notes_list[1]:
                #print(part)
                # imap fetch returns s.th. like:
                # ('OK', [('1 (UID 1 RFC822 {519}', 'From: ...'), ')'])
                if part == b")":
                   continue
                #print(part[1])
                match = uid_re.search(part[0].decode())
                uid = None if match is None else match.group(1)
                message = email.message_from_bytes(part[1])
                #print(message)
                timestamp = email.utils.parsedate_to_datetime(message.get("date"))
                #print(timestamp)
                xuuid= message.get("X-Universally-Unique-Identifier")

                subject = ""
                raw_subject = message.get("subject")
                #print(raw_subject)
                for substring, charset in email.header.decode_header(raw_subject):
                    if not charset is None:
                        substring = substring.decode(charset)
                    subject += substring

                text, type=self.decodeNote(message)
                #print(text)
                print("Found on server: ", subject)


                obj = session.query(Note).filter_by(xuuid=xuuid, subject=subject, type=type, text=text).first()
                if obj:
                    print("Note equal on Server and Client: ", subject)

                    obj.uid = uid
                    obj.sync= True
                    obj.timestamp = timestamp
                    session.add(obj)
                    session.commit()
                    continue

                obj=session.query(Note).filter(Note.xuuid==xuuid, Note.timestamp<timestamp).first()
                if obj:
                    print("Update database: ", subject)
                    obj.subject = subject
                    obj.timestamp = timestamp
                    obj.uid = uid
                    obj.text= text
                    obj.type = type
                    obj.sync= True
                    if self.startup == False:
                        _ACTIVE_NOTES[obj.xuuid].update()
                    session.add(obj)
                    session.commit()
                    continue

                obj=session.query(Note).filter(Note.xuuid==xuuid, Note.timestamp>timestamp).first()
                if obj:
                    print("Update imap: ", subject)
                    obj.sync= True
                    self.updateNotes(obj)
                    session.add(obj)
                    session.commit()
                    continue

                obj=session.query(Note).filter_by(xuuid=xuuid).first()
                if obj == None:
                    print("New Note on Server: ", subject)
                    obj = Note()
                    obj.uid = uid
                    obj.x = 12
                    obj.y = 12
                    obj.w = 150
                    obj.h =200
                    newWindow = True

                    obj.subject = subject
                    obj.timestamp = timestamp

                    obj.text= text
                    obj.type = type
                    obj.sync= True
                    if xuuid == None:
                        obj.xuuid = str(uuid.uuid4())
                        self.updateNotes(obj)
                    else:
                        obj.xuuid = xuuid
                    if newWindow and not self.startup:
                        MainWindow(obj=obj)
                    session.add(obj)
                    session.commit()

        for obj in session.query(Note).filter_by(deleteNote=True).all():
            print("Delete Note Imap")
            if obj.uid:
                self.deleteUid(str(obj.uid))
            session.delete(obj)
        for obj in session.query(Note).filter_by(newNote=True).all():
            print("New Note")
            self.updateNotes(obj)
            obj.newNote = False
            obj.sync = True
        for obj in session.query(Note).filter_by(sync=False).all():
            print("Delete Note")
            if self.startup==False:
                print("Close Note")
                _ACTIVE_NOTES[obj.xuuid].close()
            session.delete(obj)

        session.commit()
        self.startup = False
        self.timer.start(30000)


    def updateNotes(self, obj):

        now = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        message = email.message.EmailMessage()
        rfc_now = email.utils.formatdate(localtime=True)
        message[ "Subject"]= obj.subject
        message[ "Content-Type"]= obj.type
        message[ "Content-Transfer-Encoding"]= "8bit"
        message[ "X-Uniform-Type-Identifier"]= "com.apple.mail-note"
        message[ "From"]= self.user
        message[ "Message-ID"]= email.utils.make_msgid()
        message[ "Date"]= email.utils.formatdate(localtime=True)
        message[ "X-Mail-Created-Date"]= rfc_now
        message[ "X-Universally-Unique-Identifier"]= obj.xuuid
        message.set_content(obj.text, subtype ="html")

        now = imaplib.Time2Internaldate(time.time())
        ret = self.imap.append("Notes", "", now, message.as_bytes())

        if obj.newNote ==False:
            self.deleteUid(str(obj.uid))
        obj.uid=str(ret[1][0]).split(' ')[2][:-1]
        #print(obj.uid)
        session.add(obj)
        session.commit()

    def deleteUid(self,uid):
        ret = self.imap.uid("COPY", uid, "Trash")
        print("moved note to Trash:\nuid=%s\nret=%s\n" % (uid, ret))
        ret = self.imap.uid("STORE", uid, "+FLAGS", "(\\Deleted)")
        print("deleted note:\nuid=%s\nret=%s\n" % (uid, ret))
        self.imap.expunge()

    def decodeNote(self, message):
            if message.is_multipart():
                for part in message.get_payload():
                    #print(part)
                    self.decodeNote(part)
            else:

                contenttype = message.get_content_type().lower()
                #print(contenttype)
                body = message.get_payload(decode=True)
                if contenttype.startswith("text/plain"):
                    #self.textEdit.setPlainText(body.decode().replace("\r", ""))
                    #print(body.decode().replace("\r", ""))
                    return body.decode().replace("\r", ""), "text/plain"
                elif contenttype.startswith("text/html"):
                    #self.textEdit.setHtml(body.decode())

                    #print(body.decode())
                    return body.decode(), "text/html"
                # elif contenttype.startswith("image/"):
                #     print("Image")
                #     print(body)
                #     img = PIL.Image.open(BytesIO(body))
                #     res_img = img.resize((200, 200))
                #     im_file = BytesIO()
                #     res_img.save(im_file, format="JPEG")
                #     im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
                #     im_b64 = base64.b64encode(im_bytes)
                #     print(im_b64)
                #     return
                else:
                    return ( "<cannot display " + contenttype + ">") ,"Unkown"

    def close(self):
        self.imap.noop()
        print("expunged mailbox=%s\n" % (self.imap.expunge(),))
        print("closed mailbox=%s\n" % (self.imap.close(),))



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint ) #| Qt.WindowStaysOnTopHint
        self.show()
        self.sizegrip.installEventFilter(self)
        self.header.installEventFilter(self)



        self.setAttribute(Qt.WA_TranslucentBackground)
        #self.setWindowOpacity(0.6)


        radius = 10
        self.centralWidget.setStyleSheet(
            """
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )
        # Custom green palette.
        # self.header.setStyleSheet('background-color: rgb(152, 230, 182);')
        # self.textEdit.setStyleSheet('color: rgb(80, 80, 80); background-color: rgb(169, 255, 203);')
        # self.footer.setStyleSheet('background-color: rgb(169, 255, 203);')

        #Windows Style
        self.header.setStyleSheet(
            """
            background-color: #fff2ab;
            border-top-left-radius:{0}px;
            border-bottom-left-radius:0px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:0px;
            """.format(radius)
        )
        self.footer.setStyleSheet(
            """
            background-color: #fff7d1;             
            border-top-left-radius:0px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:0px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )
        self.textEdit.setStyleSheet('color: rgb(80, 80, 80); background-color: #fff7d1; border-top-left-radius:0px;border-top-right-radius:0px;border-bottom-left-radius:0px;border-bottom-right-radius:0px;')
        self.textEdit.setFont(QFont('Calibri', 14))
       
        self.sizegrip.setStyleSheet('background-color: rgba(169, 255, 203, 0);')

      

        self.textEdit.selectionChanged.connect(self.update_format)
        self.boldButton.toggled.connect(lambda x: self.textEdit.setFontWeight(QFont.Bold if x else QFont.Normal))
        self.italicButton.toggled.connect(self.textEdit.setFontItalic)
        self.underlineButton.toggled.connect(self.textEdit.setFontUnderline)

        def strikeOutFont(state):
            item = self.textEdit.currentFont()
            item.setStrikeOut(state)
            self.textEdit.setCurrentFont(item)

        self.strikeoutButton.toggled.connect(strikeOutFont)

        # Load/save note data, store this notes db reference.
        if obj:
            self.obj = obj
            self.load()
        else:
            self.obj = Note()
            self.obj.subject = "New Note"
            self.obj.type= "text/html"
            self.obj.xuuid = str(uuid.uuid4())
            self.obj.newNote=True
            self.obj.sync=True
            self.saveNote()
            self.savePosition()
            self.saveSize()

        self.closeButton.pressed.connect(self.delete_window)
        self.moreButton.pressed.connect(create_new_note)
        self.textEdit.textChanged.connect(self.saveNote)
        self.deleteButton.pressed.connect(self.deleteNote)

        # Flags to store dragged-dropped
        self._drag_active = False
        self._format_actions = [
            self.boldButton,
            self.italicButton,
            self.underlineButton,
            self.strikeoutButton,
            # We don't need to disable signals for alignment, as they are paragraph-wide.
        ]


    def block_signals(self, objects, b):
        for o in objects:
            o.blockSignals(b)

    def eventFilter(self, source, event):
        #print('mouse event', source)
        if source == self.header:
            if event.type() == QEvent.MouseButtonPress:
                #print('mouse pressed', source)
                self.previous_pos = event.globalPos()
            if event.type() == QEvent.MouseMove:
                #print('mouse moved', source)
                self.move(self.pos() + event.globalPos() - self.previous_pos)
                self.previous_pos = event.globalPos()
                self._drag_active = True
            if event.type() == QEvent.MouseButtonRelease:
                if self._drag_active:
                    self.savePosition()
                    self._drag_active = False
        if source == self.sizegrip:
            # print("Resize")
            # if event.type() == QEvent.MouseButtonPress:
            #     print('mouse pressed', source)
            # if event.type() == QEvent.MouseMove:
            #     print('mouse moved', source)
            if event.type() == QEvent.MouseButtonRelease:
                #print("mouse release")
                self.saveSize()
        return super(MainWindow, self).eventFilter(source, event)

    def load(self):
        self.move(self.obj.x, self.obj.y)
        self.textEdit.setHtml(self.obj.text)
        self.resize(self.obj.w, self.obj.h)
        _ACTIVE_NOTES[self.obj.xuuid] = self

    def update(self):
        #print("Update triggerd")
        self.textEdit.blockSignals(True)
        self.move(self.obj.x, self.obj.y)
        #print(self.obj.text)
        self.textEdit.setHtml(self.obj.text)
        self.resize(self.obj.w, self.obj.h)
        self.textEdit.blockSignals(False)
        _ACTIVE_NOTES[self.obj.xuuid] = self

    def saveNote(self):
        #print("SaveNote triggerd")
        self.obj.text = self.textEdit.toHtml()
        self.obj.timestamp = datetime.datetime.now()
        self.obj.deleteNote = False
        self.obj.subject=html2text.html2text(self.obj.text).split('\n', 1)[0]
        session.add(self.obj)
        session.commit()
        _ACTIVE_NOTES[self.obj.xuuid] = self

    def savePosition(self):
        self.obj.x = self.x()
        self.obj.y = self.y()

        session.add(self.obj)
        session.commit()

        _ACTIVE_NOTES[self.obj.xuuid] = self

    def saveSize(self):
        self.obj.w = self.width()
        self.obj.h = self.height()

        session.add(self.obj)
        session.commit()

        _ACTIVE_NOTES[self.obj.xuuid] = self


    def deleteNote(self):
        result = QMessageBox.question(self, "Delete Note?", "Are you sure you want to delete this note?")
        if result == QMessageBox.Yes:
            self.obj.deleteNote=True
            session.add(self.obj)
            session.commit()
            self.close()

    def update_format(self):
        """
        Update the font format toolbar/actions when a new text selection is made. This is neccessary to keep
        toolbars/etc. in sync with the current edit state.
        :return:
        """
        # Disable signals for all format widgets, so changing values here does not trigger further formatting.
        self.block_signals(self._format_actions, True)

        # self.fonts.setCurrentFont(self.editor.currentFont())
        # # Nasty, but we get the font-size as a float but want it was an int
        # self.fontsize.setCurrentText(str(int(self.editor.fontPointSize())))

        self.italicButton.setChecked(self.textEdit.fontItalic())
        self.underlineButton.setChecked(self.textEdit.fontUnderline())
        self.boldButton.setChecked(self.textEdit.fontWeight() == QFont.Bold)
        self.strikeoutButton.setChecked(self.textEdit.font().strikeOut())
        # self.alignl_action.setChecked(self.editor.alignment() == Qt.AlignLeft)
        # self.alignc_action.setChecked(self.editor.alignment() == Qt.AlignCenter)
        # self.alignr_action.setChecked(self.editor.alignment() == Qt.AlignRight)
        # self.alignj_action.setChecked(self.editor.alignment() == Qt.AlignJustify)

        self.block_signals(self._format_actions, False)

    def delete_window(self):
        result = QMessageBox.question(self, "Close All Notes?", "Are you sure you want to close all notes?")
        if result == QMessageBox.Yes:
            app.quit()



if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Sticky Notes")
    app.setStyle("Fusion")
    
    # Custom brown palette.
    # palette = QPalette()
    # palette.setColor(QPalette.Window, QColor(233, 209, 97)) #233
    # palette.setColor(QPalette.WindowText, QColor(78, 78, 76))
    # palette.setColor(QPalette.ButtonText, QColor(78, 78, 76))
    # palette.setColor(QPalette.Text, QColor(78, 78, 76))
    # palette.setColor(QPalette.Base, QColor(233, 209, 150))
    # palette.setColor(QPalette.AlternateBase, QColor(233, 209, 150))
    # app.setPalette(palette)



    # thread = ImapNotes()
    # thread.start()

    notes = ImapNotes()
    #notes.open()
    #notes.getNotes()

    existing_notes = session.query(Note).all()
    if len(existing_notes) == 0:
        MainWindow()
    else:
        for note in existing_notes:
            MainWindow(obj=note)
    app.exec_()
    #thread.exiting=True
    notes.close()