import idaapi
import socket

def s_send(msg):
  #idaapi.msg("[i2q Plugin] s_send start\n")
  try:
    s = socket.socket()
    host = "127.0.0.1"
    port = 3001
  
    s.connect((host, port))
  except Exception, e:
    idaapi.msg("[i2q Plugin] conn failed : %s\n" % e)
  #idaapi.msg("[i2q Plugin] s_send : " + msg + "\n")
  s.send(msg)
  s.close

  
def update_address(addr_type, addr):
  cmd = "i2q set%s 0x%x" % (addr_type, addr,)
  #idaapi.msg("[i2q Plugin] cmd : %s\n" % cmd)
  s_send(cmd)

class qiraplugin_t(idaapi.plugin_t):
  flags = 0
  comment = ""
  help = ""
  wanted_name = "IDA to Qira sync Plugin"
  wanted_hotkey = "Alt-x"

  def init(self):
    self.old_addr = None
    self.addr = None
    idaapi.msg("[i2q Plugin] init!\n")

    return idaapi.PLUGIN_KEEP


  def run(self, arg):
    idaapi.msg("[i2q Plugin] Syncing ...\n")
    self.addr = idaapi.get_screen_ea()

    
    if (self.old_addr != self.addr):
      if (idaapi.isCode(idaapi.getFlags(self.addr))):
        #idaapi.msg("[i2q Plugin] update instrunction address\n")
        update_address("iaddr", self.addr)
      else:
        # Data Address
        #idaapi.msg("[i2q Plugin] update data address\n")
        update_address("daddr", self.addr)
    self.old_addr = self.addr
    

  def term(self):
    idaapi.msg("[i2q Plugin] Plugin uninstalled!\n")


def PLUGIN_ENTRY():
  return qiraplugin_t()
