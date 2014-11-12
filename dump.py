#!/usr/bin/python
"""
dump card data, waitman gobble <ns@waitman.net>
"""
import sys
import sqlite3
import gnupg
import getpass

gpg = gnupg.GPG(gnupghome='/root/.gnupg')

secret = getpass.getpass('Enter passphrase:')

db = sqlite3.connect('cc_data.sqlite3')
c = db.cursor()
c.execute('''SELECT * FROM scans''')
for row in c:
	data = gpg.decrypt(row[2], passphrase=secret)
	print('{0}\t{1}\t{2}'.format(row[0], row[1], data))
db.close()

