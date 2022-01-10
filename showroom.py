import viz
import vizfx
import vizconnect
import vizinput
import vizinfo
import webbrowser

# Info box
vizinfo.InfoPanel(align=viz.ALIGN_RIGHT_BOTTOM)
info = vizinfo.InfoPanel('Welcome to my virutal reality career showroom!\nEmail: davidtran2440@gmail.com\nGithub: https://github.com/davidtran001', align=viz.ALIGN_RIGHT_TOP, icon=False)
info.addSeparator()

# Physics
viz.phys.enable()

# Add collision
viz.MainView.collision( viz.ON )

#Add ground
ground = viz.addChild('ground.osgb')
ground.setScale([0.23,0,0.25])
ground.setPosition([0,-0.1,0])
ground.collidePlane() #Make ground collide with objects as if it were an infinite plane
ground.collideMesh() #Make object collide if its actual geometry intersects another object
ground.disable( viz.DYNAMICS ) #Disables dynamic physics forces from acting on the object

#Can use desktop one for desktop mode or create your own
#vizconnect.go('vizconnect_config_vive.py')aaaa
vizconnect.go('vizconnect_config_desktop.py')

#env = vizfx.addChild('../../Vizard Sample Scene/Resources/kitchen.osgb')
#env = vizfx.addChild('showroom.osgb')
env = vizfx.addChild('showroom.osgb')

#Add objects to grab
PIEMAP = env.getChild('PIEMAP')
pie = env.getChild('pie')
featherink = env.getChild('featherink')
robot = env.getChild('robot')
dumbbell = env.getChild('dumbbell')
dumbbell2 = env.getChild('dumbbell2')
chatbubble = env.getChild('chatbubble')
ibmmodelm = env.getChild('ibmmodelm')
PIEMAPText = env.getChild('PIEMAPText')
poetifyText = env.getChild('poetifyText')
VisionFitText = env.getChild('VisionFitText')
TCPChatServerText = env.getChild('TCPChatServerText')

grabbableObjects = [PIEMAP,pie,featherink,robot,dumbbell,dumbbell2,chatbubble,ibmmodelm]

# Code to get the grabber tool by name and supply the list of items which can be grabbed
grabber = vizconnect.getRawTool('grabber')
grabber.setItems(grabbableObjects)
grabber2 = vizconnect.getRawTool('grabber2')
grabber2.setItems(grabbableObjects)

# activate physics on grabbable objects after they have been grabbed
def onGrab(e):
	if e.grabbed == PIEMAP:
		PIEMAP.collideBox()
		print('grabbed PIEMAP')
		
	if e.grabbed == pie:
		pie.collideBox()
		print('grabbed pie')
	
	if e.grabbed == featherink:
		featherink.collideBox()
		print('grabbed featherink')
		
	if e.grabbed == robot:
		robot.collideBox()
		print('grabbed robot')
	
	if e.grabbed == dumbbell:
		dumbbell.collideBox()
		print('grabbed dumbbell')
	
	if e.grabbed == dumbbell2:
		dumbbell2.collideBox()
		print('grabbed dumbbell2')
	
	if e.grabbed == chatbubble:
		chatbubble.collideBox()
		print('grabbed chatbubble')
	
	if e.grabbed == ibmmodelm:
		ibmmodelm.collideBox()
		print('grabbed ibmmodelm')
	
	# open github link for the following items
	if e.grabbed == PIEMAPText:
		webbrowser.open('https://github.com/davidtran001/PIE_MAP', new=0, autoraise=True)
		PIEMAPText.collideBox()
		print('grabbed PIEMAPText')
	
	if e.grabbed == poetifyText:
		webbrowser.open('https://github.com/davidtran001/Poetify', new=0, autoraise=True)
		poetifyText.collideBox()
		print('grabbed poetifyText')
	
	if e.grabbed == VisionFitText:
		VisionFitText.collideBox()
		print('grabbed VisionFitText')
		
	if e.grabbed == TCPChatServerText:
		webbrowser.open('https://github.com/davidtran001/TCP-Chat-Server', new=0, autoraise=True)
		TCPChatServerText.collideBox()
		print('grabbed TCPChatServerText')

from tools import grabber
viz.callback(grabber.GRAB_EVENT, onGrab)


