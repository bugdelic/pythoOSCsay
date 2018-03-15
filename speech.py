# pip3 install python-osc 
# example : oscer 127.0.0.1 1099 /talk "ここに文字"
import argparse
import math
import subprocess

from pythonosc import dispatcher
from pythonosc import osc_server

def print_volume_handler(unused_addr, args):
  print(''.join(args));
  sayargs = ['say', ''.join(args)]
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
