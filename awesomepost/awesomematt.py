#!/usr/bin/python3
# This is a prankification for Mattermost Channel

from mattermostdriver import Driver
from time import sleep
from asciiart import asciiart


class AwesomePost():
    default_path = 80
    initial_post_message = ' '
    mg = asciiart.MegaNimation()

    def __init__(self, matt_driver, channel_id):
        self.matt_driver = matt_driver
        # self.matt_driver = Driver #Used for completion in VSCode
        self.channel_id = channel_id

    def create_post(self, initial_message = None):
        if initial_message == None:
            initial_message = AwesomePost.initial_post_message
        return self.matt_driver.posts.create_post(options={
            'channel_id': self.channel_id['id'],
            'message': str(initial_message)
        })
    
    def update_post(self, post_id, message):
        return self.matt_driver.posts.update_post(post_id, options={
            'id': str(post_id),
            'message': str(message)
        })

    def delete_post(self, post_id):
        return self.matt_driver.posts.delete_post(post_id)

    def delete_after_delay(self, post_id, delete_delay = None):
        if delete_delay == None:
            delete_delay = 0
        if delete_delay != 0:
            sleep(int(delete_delay))
            self.delete_post(post_id)

    def count_down(self, count, end_message="GO !!!", between_delay=1, delete_delay=0):
        post = self.create_post(str(count))
        for i in reversed(range(0, count)):
            self.update_post(post['id'], str(i))
            sleep(between_delay)
        
        self.update_post(post['id'], str(end_message))

        if delete_delay != 0:
            sleep(int(delete_delay))
            self.delete_post(post['id'])
    
    def moving_object(self, obj, path = None, delete_delay = 0):
        if path == None:
            mo_gen = AwesomePost.mg.moving_object(obj)
        else:
            mo_gen = AwesomePost.mg.moving_object(obj, path)
        
        post = self.create_post(initial_message=obj)
        
        for pos in mo_gen:
            self.update_post(post['id'], "." + str(pos))
        
        self.delete_after_delay(post['id'], delete_delay)
    
    def waiving(self, post_id = None, obj = None, path = None, delete_delay = 0):
        if path == None and obj == None:
            wa_gen = AwesomePost.mg.waiving()
        elif obj != None and path == None:
            wa_gen = AwesomePost.mg.waiving(obj=obj)
        elif obj == None and path != None:
            wa_gen = AwesomePost.mg.waiving(path=path)
        elif obj != None and path != None:
            wa_gen = AwesomePost.mg.waiving(obj=obj, path=path)
        
        if post_id == None:
            post = self.create_post(initial_message=obj)
            post_id = post['id']
        
        for pos in wa_gen:
            if pos == '_':
                pos == r'\_'
            self.update_post(post_id, str(pos))
        
        self.delete_after_delay(post_id, delete_delay)
    
    def moving_object_in_ether(self, obj, post_id = None, ether = '.', path = None, delete_delay = 0):
        if path == None:
            path = AwesomePost.default_path
            
        moe_gen = AwesomePost.mg.moving_object_in_ether(obj, ether, path)

        if post_id == None:
            post = self.create_post()
            post_id = post['id']
        
        for item in moe_gen:
            self.update_post(post_id, str(item))
        
        self.delete_after_delay(post_id, delete_delay)
    
    def scrolling(self, obj, post_id = None, path = None, delete_delay = 0):
        if path == None:
            path = AwesomePost.default_path
        if post_id == None:
            post = self.create_post()
            post_id = post['id']
        
        scr_gen = AwesomePost.mg.scrolling(obj, path)

        for item in scr_gen:
            self.update_post(post_id, str(item))


