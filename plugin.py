import Image

class ImageManipulation():

	def __init__(self, main_window)	:
		self.main_window = main_window
		self.mimes = ('image/png', 'image/jpeg', 'image/gif','image/bmp','image/tiff', )
		self.items = (
		{
			'label': 'Image manipulation',
		    'submenu':
			    (
				    {
				         'label':'Resize 25%',
				         'data': 25,
				         'callback': self.resize,
			        },
			        {
				         'label':'Resize 50%',
				         'data': 50,
				         'callback': self.resize,
			        },
			        {
				         'label':'Resize 75%',
				         'data': 75,
				         'callback': self.resize,
			        },
			        {
				        'type': 'separator',
			        },
			        {
				        'label': 'Rotate 90',
			            'data': Image.ROTATE_90,
			            'callback': self.transpose,
			        },
			        {
			            'label': 'Rotate 180',
			            'data': Image.ROTATE_180,
			            'callback': self.transpose,
			        },
			        {
				        'label': 'Rotate 270',
				        'data': Image.ROTATE_270,
				        'callback': self.transpose,
			        },
			        {
				        'label': 'Flip left to rigth',
				        'data': Image.FLIP_LEFT_RIGHT,
				        'callback': self.transpose,
			        },
			        {
				        'label': 'Flip top to bottom',
				        'data': Image.FLIP_TOP_BOTTOM,
				        'callback': self.transpose,
			        },
			        {
				        'type': 'separator',
			        },
			        {
				        'label': 'Convert',
		                'submenu':
			            (
				            {
					            'label': 'PNG',
					            'data': 'png',
					            'callback': self.convert,
				            },
				            {
				            'label': 'JPEG',
				            'data': 'JPEG',
				            'callback': self.convert,
				            },
				            {
				            'label': 'BMP',
				            'data': 'bmp',
				            'callback': self.convert,
				            },
				            {
				            'label': 'TIFF',
				            'data': 'tiff',
				            'callback': self.convert,
				            },
			                {
				            'label': 'GIF',
				            'data': 'gif',
				            'callback': self.convert,
				            },
			            )
			        }

				)
		},
	)

	def get_selection_mimes(self):

		selections = self.main_window.get_active_object()._get_selection_list()
		is_subset = lambda x:self.main_window.associations_manager.get_mime_type(x) in self.mimes
		result = filter(is_subset, selections)
		return result

	def resize(self, widget, percent):
		for image in self.get_selection_mimes():
			try:
				im = Image.open(image)
				w,h = im.size
				im.resize(((percent*w)/100,(percent*h)/100), Image.ANTIALIAS).save(image)
			except IOError:
				print "cannot resize", image


	def transpose(self, widget, method):
		for image in self.get_selection_mimes():
			try:
				im = Image.open(image)
				im.transpose(method).save(image)
			except IOError:
				print "cannot rotate", image

	def convert(self, widget, format):
		for image in self.get_selection_mimes():
			try:
				im = Image.open(image)
				im.save(image+'.'+format, format=format)
			except IOError:
					print "cannot convert", image


def register_plugin(application):

	im = ImageManipulation(application)
	for item in im.items:
		application.register_popup_menu_action(im.mimes, application.menu_manager.create_menu_item(item))
