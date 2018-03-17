# coding:utf-8
# -*- coding:utf-8 -*-
# python-oscを利用します。インストール必要です。
# pip3 install python-osc 
# ポートはデフォで1099です。python speech.pyで起動します。
# example : oscer 127.0.0.1 1099 /talk "ここに文字"
import argparse
import math
import subprocess

import base64

from pythonosc import dispatcher
from pythonosc import osc_server

def print_volume_handler(unused_addr, args):

  #decodeしてもとデータに変換
  dec_file = base64.b64decode( args )
  print(''.join(args));
  sayargs = ['say', dec_file]
  subprocess.call(sayargs)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/talk", print_volume_handler)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
