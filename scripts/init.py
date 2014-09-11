#!/usr/bin/env python
#fileencoding=utf-8

import time
import logging
import hashlib

from scaff import Scaffold

def hash_pwd(pwd, salt):
    return hashlib.sha1(pwd+'|'+salt).hexdigest()[:16]

class Runner(Scaffold):
    def main(self):
        root_user = self.db.user.find_one({'mail': 'root@root'}) or {}
        root_user.update({
            "name": "root",
            "created_at": time.time(),
            "created_by": "sys",
            "valid": True,
            "role": 0,
            "mail": "root@root",
            "salt": "dzwOrPqGdgOwBqyV"
        })
        root_user['pwd'] = hash_pwd(hash_pwd('802debaed8f55ffc', root_user['mail']), root_user['salt'])

        self.db.user.save(root_user)

        logging.info('root user created.')

        self.db.user.ensure_index([('mail', 1)], unique=True)

if __name__ == '__main__':
    Runner().run()
