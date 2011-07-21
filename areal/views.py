# Create your views here.

from shared import *
#from mail_tools.gmail_imap import gmail_imap
import imaplib
import quopri
import email
import chardet


@render_to('areal/index.html')
def index(request):
    c=imaplib.IMAP4_SSL('imap.yandex.ru')
    print 'connection'
    c.login('arealtr99@yandex.ru','201965')
    print 'logged'
    c.select('INBOX', readonly=True)
    print 'selected'
    typ, msg_ids = c.search(None, 'ALL')
    print '='*8
    last=msg_ids[0].split(' ')[-1]
    resp=[]
    for i in xrange(8):
        typ, msg_data = c.fetch(last, '(RFC822)')
        print 'fetch %s [%s]' % (last,typ)
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1])
    #            msg.set_charset('koi8-r')
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
                msg['id']=last
                text=''
                if msg.is_multipart():
                    for part in msg.get_payload():
                        print '%s -- %s' % (last,part.get_content_maintype())
                        if part.get_content_maintype() == 'text':
                            text=part.get_payload(decode=True)
                        elif part.is_multipart():
                            for pp in part.get_payload():
                                print '-- %s -- %s' % (last,pp.get_content_maintype())
                                if pp.get_content_maintype() == 'text':
                                    text=pp.get_payload(decode=True)
#                            if not text:
#                                text=part.get_payload()
                else:
                    text=msg.get_payload(decode=True)

#                text=msg.get_payload()[1].get_payload()
                text=quopri.decodestring(text)
                enc=chardet.detect(text)['encoding']
#                print '%s: %s (%s)' % (last,text[0:60],enc)

                if enc and enc in ['ISO-8859-2'] and not msg['subj_e'].startswith('RE:'):
                    msg['text_e']=text.decode('cp1251')
                elif enc and enc not in ['utf8','utf-8']:
                    if msg['subj_e'].startswith('RE:'):
                        msg['text_e']=text.decode('koi8-r')
                    else:
                        msg['text_e']=text.decode(enc)
                else:
                    msg['text_e']=text



                resp.append(msg)
        last=str(int(last)-1)
    c.logout()


    return {'msgs':resp,'response':''}


