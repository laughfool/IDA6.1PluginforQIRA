import idaapi
import socket


def jump_to(qira_address):
    #idaapi.jumpto(qira_address, -1, 0)
    idaapi.jumpto(qira_address)

def parse_msg(msg):
  dat = msg.split(" ")
  if dat[0] == "setaddress" and dat[1] != "undefined":
    try:
      a = idaapi.toEA(0, int(str(dat[1][2:]),16))
      #idaapi.msg("[q2i Plugin] parse_msg : %s\n" % a)
      jump_to(a)
    except:
      idaapi.msg("[q2i Plugin] Error processing the address\n")

def s_send(msg):
  idaapi.msg("[q2i]s_send start\n")
  s = socket.socket()
  #host = socket.gethostname()
  host = "127.0.0.1"
  port = 3001
  s.connect((host, port))
  #idaapi.msg("[q2i Plugin]send msg : " + msg + "\n")
  s.send(msg)
  result = s.recv(1024)
  #idaapi.msg("[q2i Plugin]recv msg " + result + "\n" )
  parse_msg(result)
  s.close


def get_address():
  cmd = "getaddress"
  s_send(cmd)
  
class qiraplugin_t(idaapi.plugin_t):
  flags = 0
  comment = ""
  help = ""
  wanted_name = "Qira to IDA sync Plugin"
  wanted_hotkey = "Alt-c"

  def init(self):
    self.old_addr = None
    self.addr = None
    idaapi.msg("[q2i Plugin] init!\n")
    return idaapi.PLUGIN_KEEP


  def run(self, arg):
    idaapi.msg("[q2i Plugin] Syncing ...\n")
    get_address()
    

  def term(self):
    idaapi.msg("[q2i Plugin] Plugin uninstalled!\n")


def PLUGIN_ENTRY():
  return qiraplugin_t()