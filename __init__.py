
__version__ = "1.0"
__api__     = "4.9"


def match_with_text(arg, msg):
	if arg in msg:return msg[arg]
	else:return None

def match_with_class(arg, msg, classe):
	if arg in msg:return classe(msg[arg])
	else:return None

class Contact:
	def __init__(self, msg):
		self.phone_number = msg['phone_number']
		self.first_name   = msg['first_name']
		self.last_name    = match_with_text('last_name', msg)
		self.user_id      = match_with_text('user_id', msg)
		self.vcard        = match_with_text('vcard', msg)

class Location:
	def __init__(self, msg):
		self.longitude = msg['longitude']
		self.latitude  = msg['latitude']

class Voice:
	def __init__(self, msg):
		self.msg            = msg
		self.file_id        = msg['file_id']
		self.duration       = msg['duration']
		self.mime_type      = msg['mime_type']
		self.file_size      = msg['file_size']
		self.file_unique_id = msg['file_unique_id']

class Venue:
	def __init__(self, msg):
		self.msg             = msg
		self.location 		 = match_with_class('location', msg, Location)
		self.title    		 = msg['title']
		self.address  	  	 = msg['address']
		self.foursquare_id   = msg['foursquare_id']
		self.foursquare_type = msg['foursquare_type']

class UserProfilePhotos:
	def __init__(self, msg):
		self.msg 		 = msg
		self.photos      = msg['photos']
		self.total_count = msg['total_count']

class File:
	def __init__(self, msg):
		self.file_id        = msg['file_id']
		self.file_size      = msg['file_size']
		self.file_path      = msg['file_path']
		self.file_unique_id = msg['file_unique_id']

class ChatPhoto:
	def __init__(self, msg):
		self.msg = msg
		self.big_file_id   = msg['big_file_id']
		self.small_file_id = msg['small_file_id']
		self.big_file_unique_id   = msg['big_file_unique_id']
		self.small_file_unique_id = msg['small_file_unique_id']

class ChatMember:
	def __init__(self, msg):
		self.msg                  		= msg
		self.user                 		= FromUser(msg['user'])
		self.status               		= msg['status']
		self.is_member            		= msg['is_member']
		self.until_date           		= msg['until_date']
		self.custom_title         		= msg['custom_title']
		self.can_be_edited        		= msg['can_be_edited']
		self.can_send_polls       		= msg['can_send_polls']
		self.can_change_info      		= msg['can_change_info']
		self.can_invite_users     	   	= msg['can_invite_users']
		self.can_pin_messages     	   	= msg['can_pin_messages']
		self.can_post_messages    	   	= msg['can_post_messages']
		self.can_edit_messages         	= msg['can_edit_messages']
		self.can_send_messages         	= msg['can_send_messages']
		self.can_delete_messages       	= msg['can_delete_messages']
		self.can_promote_members       	= msg['can_promote_members']
		self.can_restrict_members      	= msg['can_restrict_members']
		self.can_send_media_messages   	= msg['can_send_media_messages']
		self.can_send_other_messages   	= msg['can_send_other_messages']
		self.can_add_web_page_previews 	= msg['can_add_web_page_previews']

class FromUser:
	def __init__(self, msg):
		self.msg           = msg
		self.id            = msg['id']
		self.is_bot        = msg['is_bot']
		self.username      = msg['username']
		self.first_name    = msg['first_name']
		self.last_name     = match_with_text('last_name', msg)
		self.language_code = msg['language_code']
		self.can_join_groups             = match_with_text("can_join_groups", msg)
		self.supports_inline_queries     = match_with_text("supports_inline_queries", msg)
		self.can_read_all_group_messages = match_with_text("can_read_all_group_messages", msg)
		
class Chat:
	def __init__(self, msg):
		self.id    				= msg['id']
		self.msg 		  		= msg
		self.types  			= msg['type']
		self.title 				= match_with_text("title", msg)
		self.photo 				= match_with_class('photo', msg, ChatPhoto)
		self.username    		= match_with_text("username", msg)
		self.first_name  		= match_with_text("first_name", msg)
		self.last_name  		= match_with_text("last_name", msg)
		self.description 		= match_with_text('description', msg)
		self.invite_link	 	= match_with_text('invite_link', msg)
		self.permissions 		= match_with_text("permissions", msg)
		self.pinned_message 	= match_with_text("pinned_message", msg)
		self.slow_mode_delay	= match_with_text('slow_mode_delay', msg)
		self.sticker_set_name	= match_with_text("sticker_set_name", msg)
		self.can_set_sticker_set= match_with_text("can_set_sticker_set", msg)

class MessageEntity:
	def __init__(self, msg):
		self.msg    = msg
		self.length = msg['length']
		self.offset = msg['offset']
		self.type   = msg['type']
		self.url    = match_with_text("url", msg)
		self.user   = match_with_text('user', msg)
		self.language = match_with_text("language", msg)

class ChatPermissions:
	def __init__(self, msg):
		self.msg                        = msg
		self.can_send_polls       		= msg['can_send_polls']
		self.can_change_info      		= msg['can_change_info']
		self.can_invite_users     	   	= msg['can_invite_users']
		self.can_pin_messages     	   	= msg['can_pin_messages']
		self.can_send_messages         	= msg['can_send_messages']
		self.can_send_media_messages   	= msg['can_send_media_messages']
		self.can_send_other_messages   	= msg['can_send_other_messages']
		self.can_add_web_page_previews 	= msg['can_add_web_page_previews']

class Animation:
	def __init__(self, msg):
		self.msg       		= msg
		self.thumb     		= match_with_text("thumb", msg)
		self.width     		= msg['width']
		self.height    		= msg['height']
		self.file_id   		= msg['file_id']
		self.duration  		= msg['duration']
		self.file_name      = match_with_text(file_name, msg)
		self.mime_type      = match_with_text('mime_type', msg)
		self.file_size      = msg['file_size']
		self.file_unique_id = msg['file_unique_id']

class PhotoSize:
	def __init__(self, msg):
		self.width     		= msg['width']
		self.height    		= msg['height']
		self.file_id   		= msg['file_id']
		self.file_size      = msg['file_size']
		self.file_unique_id = msg['file_unique_id']

class Audio:
	def __init__(self, msg):
		self.msg = msg
		self.file_id        = msg['file_id']
		self.file_unique_id = msg['file_unique_id']
		self.duration       = msg['duration']
		self.performer      = msg['performer']
		self.title          = msg['title']
		self.mime_type      = match_with_text('mime_type', msg)
		self.file_size      = match_with_text('file_size', msg)
		self.thumb          = match_with_class('thumb', msg, PhotoSize)

class VideoNote:
	def __init__(self, msg):
		self.msg = msg
		self.file_id        = msg['file_id']
		self.file_unique_id = msg['file_unique_id']
		self.length         = msg['length']
		self.duration      = match_with_text('duration', msg)
		self.file_size      = match_with_text('file_size', msg)
		self.thumb          = match_with_class('thumb', msg, PhotoSize)

class Video:
	def __init__(self, msg):
		self.msg = msg
		self.file_id        = msg['file_id']
		self.file_unique_id = msg['file_unique_id']
		self.duration       = msg['duration']
		self.mime_type      = match_with_text('mime_type', msg)
		self.file_size      = match_with_text('file_size', msg)
		self.thumb          = match_with_class('thumb', msg, PhotoSize)
		self.height         = match_with_text('height', msg)
		self.width          = match_with_text('width', msg)

class Document:
	def __init__(self, msg):
		self.msg = msg
		self.file_id        = msg['file_id']
		self.file_unique_id = msg['file_unique_id']
		self.file_name      = msg['file_name']
		self.mime_type      = match_with_text('mime_type', msg)
		self.file_size      = match_with_text('file_size', msg)
		self.thumb          = match_with_class('thumb', msg, PhotoSize)

class MaskPosition:
	def __init__(self, msg):
		self.msg     = msg
		self.point   = msg['point']
		self.x_shift = msg['x_shift']
		self.y_shift = msg['y_shift']
		self.scale   = msg['scale']

class Sticker:
	def __init__(self, msg):
		self.msg            = msg
		self.width     		= msg['width']
		self.height    		= msg['height']
		self.emoji          = msg['emoji']
		self.set_name       = match_with_text("set_name", msg)
		self.mask_position  = match_with_class('mask_position', msg, MaskPosition)
		self.file_id        = msg['file_id']
		self.is_animated    = msg['is_animated']
		self.file_unique_id = msg['file_unique_id']
		self.duration       = msg['duration']
		self.performer      = msg['performer']
		self.title          = msg['title']
		self.mime_type      = match_with_text('mime_type', msg)
		self.file_size      = match_with_text('file_size', msg)
		self.thumb          = match_with_class('thumb', msg, PhotoSize)

class Dice:
	def __init__(self, msg):
		self.msg    = msg
		self.emoji	= msg['emoji']
		self.value 	= msg['value']

class Game:
	def __init__(self, msg):
		self.msg 			= msg
		self.text 			= msg['text']
		self.title 			= msg['title']
		self.photo 			= match_with_class('photo', msg, PhotoSize)
		self.animation 		= match_with_class('animation', msg, Animation)
		self.description 	= msg['description']
		self.text_enities 	= match_with_class("text_enities", msg, MessageEntity)

class PollOptions:
	def __init__(self, msg):
		self.msg 					= msg
		self.text 					= msg['text']
		self.type 					= msg['type']
		self.is_closed 				= msg['is_closed']
		self.is_anonymous	 		= msg['is_anonymous']
		self.explanation 			= match_with_text('explanation', msg)
		self.open_period 			= match_with_text('open_period', msg)
		self.voter_count 			= msg['voter_count']
		self.correct_option_id 		= match_with_text('correct_option_id', msg)
		self.total_voters_count 	= msg['total_voters_count']
		self.explanation_entities 	= match_with_class("explanation_entities", msg, MessageEntity)
		self.allows_multiple_answers= msg['allows_multiple_answers']

class Poll:
	def __init__(self, msg):
		self.id 	= msg['id']
		self.msg 	= msg
		self.options= match_with_class("options", msg, PollOptions)

class ShippingAddress:
	def __init__(self, msg):
		self.msg 			= msg
		self.city 			= msg['city']
		self.state 			= msg['state']
		self.post_code 		= match_with_text('post_code', msg)
		self.street_line1 	= match_with_text('street_line1', msg)
		self.street_line2 	= match_with_text('street_line2', msg)
		self.country_code 	= msg['country_code']

class OrderInfo:
	def __init__(self, msg):
		self.msg 			  = msg
		self.name 			  = msg['name']
		self.email			  = msg['email']
		self.phone_number	  = msg['phone_number']
		self.shipping_address = match_with_class('shipping_address', msg, ShippingAddress)

class Invoice:
	def __init__(self, msg):
		self.msg 				= msg
		self.title 				= msg['title']
		self.currency 			= msg['currency']
		self.order_info 		= match_with_class('order_info', msg, )
		self.description		= msg['description']
		self.total_amount 		= msg['total_amount']
		self.start_parameter 	= msg['start_parameter']
		self.shipping_option_id = msg['shipping_option_id']

class SuccessfulPayment:
	def __init__(self, msg):
		self.msg 			= msg
		self.currency       = msg['currency']
		self.total_amount   = msg['total_amount']
		self.invoice_payoad = msg['invoice_payoad']

class Message:
	def __init__(self, msg):
		super().__init__()
		if match_with_text("reply_to_message", msg):
			self.reply_to_message  = match_with_class("reply_to_message", msg, Message)
		else:
			self.reply_to_message 		= None
		
		self.msg 		 				= msg
		self.dice 						= match_with_class('dice', msg, Dice)
		self.game 						= match_with_class('game', msg, Game)
		self.poll 						= match_with_class('poll', msg, Poll)
		self.text		 		        = msg['text']
		self.chat 						= Chat(msg['chat'])
		self.date 						= msg['date']
		self.venue 						= match_with_class('venue', msg, Venue)
		self.audio 						= match_with_class("audio", msg, Audio)
		self.photo 						= match_with_class('photo', msg, PhotoSize)
		self.video 						= match_with_class("video", msg, Video)
		self.voice 						= match_with_class('voice', msg, Voice)
		self.via_bot 					= match_with_class("via_bot", msg, FromUser)
		self.sticker 					= match_with_class("sticker",msg, Sticker)
		self.caption 					= match_with_text('caption', msg)
		self.contact 					= match_with_class('contact', msg, Contact)
		self.invoice 					= match_with_class('invoice', msg, Invoice)
		self.entities   				= MessageEntity(msg['entities'][0])
		self.document 					= match_with_class("document", msg, Document)
		self.animation 					= match_with_class("animation", msg, Animation)
		self.edit_date 					= match_with_text("edit_date", msg)
		self.from_user 			 		= FromUser(msg['from'])
		self.video_note 				= match_with_class('video_note', msg, VideoNote)
		self.message_id 				= msg['message_id']
		self.forward_from      			= match_with_class("forward_from", msg, FromUser)
		self.forward_date      			= match_with_text("forward_date", msg)
		self.pinned_message 			= match_with_class('pinned_message', msg, Message)
		self.new_chat_title 			= match_with_text('new_chat_title', msg)
		self.media_group_id 			= match_with_text("media_group_id", msg)
		self.new_chat_photo 			= match_with_class('new_chat_photo', msg, PhotoSize)
		self.author_signature 			= match_with_text("author_signature", msg)
		self.new_chat_members 			= match_with_class('new_chat_members', msg, FromUser)
		self.caption_entities 			= match_with_text('caption_entities',msg)
		self.forward_from_chat 			= match_with_class("forward_from_chat", msg, Chat)
		self.left_chat_members	 		= match_with_class('left_chat_members', msg, FromUser)
		self.forward_signature  		= match_with_text("forward_signature", msg)
		self.delete_chat_photo 			= match_with_text('delete_chat_photo', msg)
		self.successful_payment 		= match_with_class('successful_payment', msg, SuccessfulPayment)
		self.migrate_to_chat_id 		= match_with_text('migrate_to_chat_id', msg)
		self.group_chat_created 		= match_with_text('group_chat_created', msg)
		self.forward_sender_name		= match_with_text("forward_sender_name", msg)
		self.channel_chat_created 		= match_with_text('channel_chat_created', msg)
		self.migrate_from_chat_id 		= match_with_text('migrate_from_chat_id', msg)
		self.supergroup_chat_created 	= match_with_text('supergroup_chat_created', msg)
		self.telegram_payment_charge_id = match_with_text('telegram_payment_charge_id', msg)
		self.provider_payment_charge_id = match_with_text('provider_payment_charge_id', msg)

class ShippingQuery:
	def __init__(self, msg):
		self.id  			  = msg['id']
		self.msg 			  = msg
		self.from_user 		  = match_with_class('from',msg, FromUser)
		self.invoice_payoad   = msg['invoice_payoad']
		self.shipping_address = match_with_class('shipping_address', msg, ShippingAddress)

class PreCheckoutQuery:
	def __init__(self, msg):
		self.id  				= msg['id']
		self.msg 				= msg
		self.currency  			= msg['currency']
		self.from_user 			= match_with_class("from", msg, FromUser)
		self.order_info 		= match_with_class('order_info', msg, OrderInfo)
		self.total_amount 		= msg['total_amount']
		self.invoice_payoad 	= msg['invoice_payoad']
		self.shipping_option_id = msg['shipping_option_id']
class InlineQuery:
	def __init__(self, msg):
		self.id 		= msg['id']
		self.msg 		= msg
		self.query 		= match_with_text('query', msg)
		self.offset 	= match_with_text('offset', msg)
		self.from_user 	= match_with_class('from', msg, FromUser)
		self.localtion 	= match_with_class('localtion', msg, Location)

class CallbackQuery:
	def __init__(self, msg):
		super().__init__()
		self.id   				= msg['id']
		self.msg  				= msg
		self.data 				= msg['data']
		self.message 		  	= Message(msg['message'])
		self.from_user 			= FromUser(msg['from'])
		self.chat_instance  	= match_with_text('chat_instance',msg)
		self.game_short_name   	= match_with_text('game_short_name', msg)
		self.inline_message_id 	= msg['inline_message_id']

class ChosenInlineResult:
	def __init__(self, msg):
		self.msg 		= msg
		self.query 		= msg['query']
		self.result_id 	= msg['result_id']
		self.from_user 	= match_with_class('from', msg, FromUser)
		self.localtion 	= match_with_class('localtion', msg, Location)

class PollAnswer:
	def __init__(self, msg):
		self.msg 		= msg
		self.user 		= match_with_class('from', msg, FromUser)
		self.poll_id 	= msg['poll_id']
		self.option_ids	= msg['option_ids']

class Update:
	def __init__(self, msg):
		self.msg       				= msg
		self.poll 					= match_with_class('poll', msg, Poll)
		self.message   				= match_with_class('message', msg, Message)
		self.poll_answer 			= match_with_class('poll_answer', msg, PollAnswer)
		self.update_id 				= msg['update_id']
		self.inline_query 			= match_with_class('inline_query', msg, InlineQuery)
		self.channel_post   		= match_with_class('channel_post', msg, Message)
		self.callback_query 		= match_with_class('callback_query', msg, CallbackQuery)
		self.shipping_query 		= match_with_class('shipping_query', msg, ShippingQuery)
		self.edited_message 		= match_with_class('edited_message', msg, Message)
		self.pre_checkout_query 	= match_with_class('pre_checkout_query', msg, PreCheckoutQuery)
		self.edited_channel_post	= match_with_class('edited_channel_post',msg, Message)
		self.chosen_inline_result 	= match_with_class('chosen_inline_result', msg, ChosenInlineResult)
		
		if   self.poll is not None:
			self.update_type = "poll"
		elif self.message is not None:
			self.update_type = "message"
		elif self.poll_answer is not None:
			self.update_type = "poll_answer"
		elif self.inline_query is not None:
			self.update_type = "inline_query"
		elif self.channel_post is not None:
			self.update_type = "channel_post"
		elif self.callback_query is not None:
			self.update_type = "callback_query"
		elif self.shipping_query is not None:
			self.update_type = "shipping_query"
		elif self.edited_message is not None:
			self.update_type = "edited_message"
		elif self.pre_checkout_query is not None:
			self.update_type = "pre_checkout_query"
		elif self.edited_channel_post is not None:
			self.update_type = "edited_channel_post"
		elif self.chosen_inline_result is not None:
			self.update_type = "chosen_inline_result"
		else:
			self.update_type = "Unknow"