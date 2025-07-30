from dotenv import load_dotenv
load_dotenv()

import os
import time

from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

while True:
    resp = supabase.storage().from_("output").upload("log.txt","log.txt")
    print(resp)
    time.sleep(15)