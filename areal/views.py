# -*- coding: utf-8 -*-
# Create your views here.

from shared import *
#from mail_tools.gmail_imap import gmail_imap
import imaplib
import quopri
import email
import chardet


def get_connection():
    c=imaplib.IMAP4_SSL('imap.yandex.ru')
    c.login('arealtr99@yandex.ru','201965')
    c.select('INBOX', readonly=True)
    print 'connected'
    return c

def get_last_id(c):
    typ, msg_ids = c.search(None, 'ALL')
    last=msg_ids[0].split(' ')[-1]
    return last

def fetch_msg(c,id):
    typ, msg_data = c.fetch(id, '(RFC822)')
    print 'fetch %s [%s]' % (id,typ)
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1])
            subj=email.Header.decode_header(msg['subject'])[0]
            s=subj[0]
            if not subj[1] is None:
                s=s.decode(subj[1])
            msg['subj_e']=s
            subj=email.Header.decode_header(msg['from'])[0]
            f=subj[0]
            if not subj[1] is None:
                f=f.decode(subj[1])
            msg['from_e']=f
            msg['id']=id
            msg['text_e']=u'Для получения содержимого письма нажмите кнопку "Текст"'
    return msg

def get_from_mp(msg):
    for part in msg.get_payload():
        print '%s -- %s' % (msg['id'],part.get_content_maintype())
        if part.get_content_maintype() == 'text':
            text=part.get_payload(decode=True)
        else:
            if part.is_multipart():
                text=get_from_mp(part)
    return text

def get_msg_content(msg):
    from BeautifulSoup import BeautifulSoup
    text=''
    last=msg['id']
    if msg.is_multipart():
        text=get_from_mp(msg)
    else:
        text=msg.get_payload(decode=True)

    text=quopri.decodestring(text)
    enc=BeautifulSoup(text).originalEncoding
    msg['enc']=enc
    subre="<b><span style='font-weight:bold'>Subject:</span></b> Re:"
    print msg['subj_e']


    if enc and enc in ['ISO-8859-2']:
        try:
            msg['text']=text.decode('cp1251')
        except:
            msg['text']=text.replace('\x98','').decode('cp1251')
    elif enc and enc not in ['utf8','utf-8']:
        msg['text']=text.decode(enc)
    else:
        msg['text']=text

    return msg['text']




@render_to('areal/index.html')
def index(request):
    c=get_connection()
    last=get_last_id(c)

    resp=[]
    for i in xrange(8):
        msg=fetch_msg(c,last)
        resp.append(msg)
        last=str(int(last)-1)
    c.logout()


    return {'msgs':resp,'response':''}

def get_content(request,msg_id):
    c=get_connection()
    msg=fetch_msg(c,msg_id)
    c.logout()
    try:
        text=get_msg_content(msg)
    except Exception, e:
        text=u'Опять кодировка какая-то левая=((<br> encoding: %s<br>Error: %s' % (msg['enc'],str(e))
    return HttpResponse(text+'<br>Encoding: '+msg['enc'])