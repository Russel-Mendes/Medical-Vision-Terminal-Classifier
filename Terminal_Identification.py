# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:31:31 2019

"""
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator 
#THIS HELPS TO PROCESS THE DATA FROM A DIRECTORY
from keras.models import load_model
import os
from PIL import Image


counter, contusion_counter, avulsion_counter, puncture_counter, abrasion_counter, laceration_counter = 0,0,0,0,0,0

def clear_history(): #empties history
    global counter, contusion_counter, avulsion_counter, puncture_counter, abrasion_counter, laceration_counter
    counter, contusion_counter, avulsion_counter, puncture_counter, abrasion_counter, laceration_counter = 0,0,0,0,0,0

def show_hist():
    global counter, contusion_counter, avulsion_counter, puncture_counter, abrasion_counter, laceration_counter      
    print('\n'+'\n'+
              "There were " + str(counter) + " images" + '\n' +
              "There were " + str(contusion_counter) + " Contusions images" + '\n' +
              "There were " + str(laceration_counter) + " Laceration images" + '\n' +
              "There were " + str(avulsion_counter) + " Avulsions images" + '\n' +
              "There were " + str(abrasion_counter) + " Abrasions images" + '\n'+
              "There were " + str(puncture_counter) + " Punctures images" + '\n')
    
    
def Single_Image_Identification(IMG_PATH = '', give_output = True, track_history = True):
    if IMG_PATH == '':
        IMG_PATH = input("Please Give The Image Path: ")
    try:
        img = Image.open(IMG_PATH)
        if give_output:
            print("Image has been loaded succesfully")
    except:
        if give_output:
            print('Invalid Image Path. Function has ended early')
        return 0
    LOCAL_DIRECTORY = os.getcwd() #This is the local directory of the user
    TEMP_PATH = LOCAL_DIRECTORY + r'\DataDump\unknown' #THIS PROGRAM CREATES A DATA DUMP OF THE IMAGE
    if give_output:
        print('Creating Data Dump')
    try:
      os.makedirs(TEMP_PATH)
      if give_output:
          print('New Data Dump has been created' )
    except:
      if give_output: 
          print('Prior Data Dump has been found')    
    head,tail =  os.path.split(IMG_PATH)
    TEMP_IMAGE_PATH = os.path.join(TEMP_PATH, tail)    
    try:
        os.remove(TEMP_IMAGE_PATH)
    except:
        if give_output:
            print("there is no old image")
    img.save(TEMP_IMAGE_PATH) 
    result = Single_Image_Processing() #This is where the AI is deployed and the result is given  
    os.remove(TEMP_IMAGE_PATH)
    if give_output:    
        print('The image called: ' + str(tail) + ' is called ' + result + '\n'+'Thank you for using this program')
    if track_history:
        global counter, contusion_counter, avulsion_counter, puncture_counter, abrasion_counter, laceration_counter
        counter +=1
        if result == 'Contusion':
            contusion_counter +=1
        if result == 'Laceration':
            laceration_counter +=1
        if result == 'Avulsion':
            avulsion_counter +=1
        if result == 'Abrasion':
            abrasion_counter +=1
        if result == 'Puncture':
            puncture_counter +=1
            
    return result


def Single_Image_Processing():
    #Deploying AI
    model = load_model('MVC2.h5')
    test_path = 'DataDump'

    SINGLE_IMAGE = ImageDataGenerator().flow_from_directory(test_path, target_size = (224, 224)) 
    #Target Size is the adjusted size of the image. The AI can only handle this parameter
    IMAGE_FILE, IMAGE_CLASS  = next(SINGLE_IMAGE) 
    #the image file is the actual file, and the image class is a generated tagline which is based on the DataDump
    predictions = model.predict(IMAGE_FILE)
    #['Contusion', 'Laceration', 'Avulsion', 'Abrasion', 'Puncture'] These are the AI Classifications
    pos = int(predictions.argmax(axis=1)) #Defines what is the end prediction of the image 
    del model 
    
    if pos == 0:
        return 'Contusion'
    if pos == 1:
        return 'Laceration'
    if pos == 2:
        return 'Avulsion'
    if pos == 3:
        return 'Abrasion'
    if pos == 4:
        return 'Puncture'

def Auto_Image_Saver(IMG_PATH, TEMP_PATH, result):
    img = Image.open(IMG_PATH)
    head,tail =  os.path.split(IMG_PATH)
    TEMP_DIR = os.path.join(TEMP_PATH, result)
    TEMP_IMAGE_PATH = os.path.join(TEMP_DIR, tail)
    img.save(TEMP_IMAGE_PATH)

def Auto_Classification(track_history = True):
    
    DIR_PATH = input("Please Give Directory: ")    
    truth = os.path.isdir(DIR_PATH)
    if truth == False:
        print('Invalid Directory. Ending Function Early')
        return 0

    LOCAL_DIRECTORY = os.getcwd() #This is the local directory of the user
    TEMP_PATH = LOCAL_DIRECTORY + r'\TargetLocation' #THIS PROGRAM CREATES A DATA DUMP OF THE IMAGE

    print('Creating Target Location')
    try:
      os.makedirs(TEMP_PATH)
      print('New Target has been created' )
    except:
      print('Prior Target Location has been found')
    
    print('Establishing Sub_Targets')
    file_sub = ['Contusion', 'Laceration', 'Avulsion', 'Abrasion', 'Puncture']    
    for name in file_sub:
        NEW_DIR = os.path.join(TEMP_PATH, name)
        try:
            os.makedirs(NEW_DIR)
        except:
            print("Targets Has Been Established")
    
    print("Identifying")
    local_counter, local_contusion_counter, local_avulsion_counter = 0,0,0
    local_puncture_counter, local_abrasion_counter, local_laceration_counter = 0,0,0
    for filename in os.listdir(DIR_PATH):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            IMG_PATH = os.path.join(DIR_PATH,filename)
            result = Single_Image_Identification(IMG_PATH, give_output = False)
            img = Image.open(IMG_PATH)
            head,tail =  os.path.split(IMG_PATH)
            TEMP_DIR = os.path.join(TEMP_PATH, result)
            TEMP_IMAGE_PATH = os.path.join(TEMP_DIR, tail)
            try:
                img.save(TEMP_IMAGE_PATH)
            except:
                print("Image with Same Name Exists")
                
            if track_history:    
                local_counter +=1
                if result == 'Contusion':
                    local_contusion_counter +=1
            
                if result == 'Laceration':
                    local_laceration_counter +=1
            
                if result == 'Avulsion':
                    local_avulsion_counter +=1
            
                if result == 'Abrasion':
                    local_abrasion_counter +=1
            
                if result == 'Puncture':
                    local_puncture_counter +=1    
        else:
            print(str(filename) + "Is not a JPG or a PNG" )
      

        print('\n'+'\n'+
                "There were " + str(local_counter) + " images" + '\n' +
              "There were " + str(local_contusion_counter) + " Contusions images" + '\n' +
              "There were " + str(local_laceration_counter) + " Laceration images" + '\n' +
              "There were " + str(local_avulsion_counter) + " Avulsions images" + '\n' +
              "There were " + str(local_abrasion_counter) + " Abrasions images" + '\n'+
              "There were " + str(local_puncture_counter) + " Punctures images" + '\n')
        


help_bank = ['!help', '!help_SII', '!help_AC', '!help_CC', '!Cat', 'kill', 'SII', 'CC', 'AC', 'clear', 'show_history']
print('\n'+
      '###############################################' + '\n' +
      'Welcome to Image Categorizer'+ '\n' +
      'This program can categorize images from a location into new designated folders or automatically' + '\n' +
      'It can also identify a single image if requested' + '\n' +
      'For help type "!help" or "kill" to stop the program')
user_command = ''
while(user_command != 'kill'):
    
    user_command = input("Please Give A Command: ")
  
    if user_command == 'kill':
        print('\n'+'The Code Will Be Killed')
    
  
    if user_command == '!help':
        print('\n'+'Specify What Type of Help You Need' + '\n' +
          'Single Image Identification: type "!help_SII"' + '\n' +
          'Auto Classification: type "!help_AC"' + '\n' +
          'Available Classifications: type "!Cat"')
  
    if user_command == '!help_SII':
        print('\n'+'SII stands for Single Image Identification' + '\n' +
          'SII will take a photo from given directory --defaults to the local--' + '\n' +
          ' and will classify them across the available classifications.' + '\n' +
          'SII will prompt the user for specific task and customizations')
    
    if user_command == '!help_AC':
        print('\n'+'AC stands for Auto Classification' + '\n' +
         'AC will take photos from a directory and sorts them into new directories')
        
    if user_command == '!Cat':  
        cat = ['Contusion', 'Laceration', 'Avulsion', 'Abrasion', 'Puncture']
        print(cat) 
    
    if user_command == 'AC':
        Auto_Classification()
        print('\n'+"AC Function Has Been Completed")

    if user_command == 'SII':  
        Single_Image_Identification()
        print('\n'+"SII Function Has Been Completed")

    if user_command == 'clear':
        clear_history()
        print('\n'+"History Has been Cleared")

    if user_command == 'show_history':
        show_hist()
        
    if user_command not in help_bank:
        print('unknown input')






























    
