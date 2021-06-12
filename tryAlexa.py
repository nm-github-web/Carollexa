import pygame
import speech_recognition;
import pyttsx3
import vlc
import sys
import time

"""
Spch
ImgSpch
Video
"""

music_dictionary = {
            "how deep is your love" : {
                "type" : "Video",
                "caption": "Video",
                "video": "Music.mp4"
                }
            ,
            "instrumental music" : {
                "type" : "Video",
                "caption": "Aaj Jaane ki Jid na Karo - Instrumental",
                "video": "SitarJaaneKiJid.mp4"
                }
            ,
            "most played songs":{
                "type": "Spch",
                "text": "Despacito, Shape of you are the worlds most played songs",
                "caption": "Most Popular Song"
                }
             ,
            "types of western music":{
                "type": "ImgSpch",
                "text": "Rock, hip-hop, pop, and country, are some types of western music",
                "pic": "typesofmusic.png",
                "caption": "Types of Music"
                }
            ,
            "famous band":{
                "type": "ImgSpch",
                "text": "The Beatles was the most famous band",
                "pic": "Thebeatles.jpg",
                "caption": "The Beatles"
                }
            ,
            "most awards":{
                "type": "ImgSpch",
                "text": "The UD band have won the most awards which is 22",
                "pic": "udBand.jpg",
                "caption": "Most awards won by a band"
                }
            ,
            "famous singers":{
                "type": "ImgSpch",
                "text": "The most famous ones are Michael Jackson, Taylor Swift and Justin Bieber",
                "pic": "michaeljackson.jpg",
                "caption": "Famous singers"
                }
            ,
            "easiest instrument":{
                "type": "ImgSpch",
                "text": "The easiest instrument to learn is piano and the hardest is violin",
                "pic": "piano.jpg",
                "caption": "Easiest instrument"
                }
            ,
            "benefits of music":{
                "type": "ImgSpch",
                "text": "The benefit of music is that it's calming and soothing",
                "pic": "MusicBenefits.jpeg",
                "caption": "Benefits of music"
                }
            ,
            "indian music":{
                "type": "ImgSpch",
                "text": "It consists of Gazal, Raga, Thumri",
                "pic": "indian music.jpg",
                "caption": "Indian Music"
                }
            ,
            "mozart":{
                "type": "Spch",
                "text": "Mozart was a child prodigy, born in salsburg Austria. His full name is Wolfgang Amadeus Mozart. Some of his fammous compositions are The Marriage of Figaro, Don Giovanni and the Jupiter Symphony",
                "caption": "Mozart"
                }
             ,
            "beethoven":{
                "type": "Spch",
                "text": "Beethoven was born in bonn Germany, his full name is Ludwig van Beethoven, some of his fammous compositions are Septet, Moonlight Sonata, Für Elise",
                "caption": "Beethoven"
                }
             ,
            "styles":{
                "type": "ImgSpch",
                "text": "There are many types of styles but the most used ones are waltz, swing, jazz and dance",
                "pic": "styles.png",
                "caption": "Styles"
                }
             ,
            "tone":{
                "type": "Spch",
                "text": "Traditionally in Western music, a musical tone is a steady periodic sound. A musical tone is characterized by its duration, pitch, intensity, and timbre.",
                "caption": "Tone"
                }
            }

# set width and height of screen
screen_dimensions = (900,600)
# location of text on screen
textlocation = (50,500)

def executeCommand(command):
    commandType = music_dictionary[command]["type"]
    
    if commandType == "ImgSpch":
        commandText = music_dictionary[command]["text"]
        commandPic = music_dictionary[command]["pic"]
        commandCaption = music_dictionary[command]["caption"]
        
        setScreenImg(commandPic, commandCaption) 
        time.sleep(1)
        
        if commandText:
            setScreenText (commandText, textlocation)
            sayText (commandText)
            time.sleep(2)
    
    elif commandType == "Spch":
        commandText = music_dictionary[command]["text"]
        commandCaption = music_dictionary[command]["caption"]
                
        if commandText:
            setScreenText (commandText, textlocation)
            pygame.display.set_caption(commandCaption)
            sayText (commandText)
            time.sleep(2)

    elif commandType == "Video":
        commandVid = music_dictionary[command]["video"]
        commandCaption = music_dictionary[command]["caption"]
        pygame.display.set_caption(commandCaption)

        mediaplayer = vlc.MediaPlayer()
        media = vlc.Media(commandVid)
        mediaplayer.set_media(media)
        # start playing video
        mediaplayer.play()
        time.sleep(20)
        mediaplayer.stop()
   
# end of function executeCommand

def setScreenText (displaytext, location = (0,0)):
    # set font
    font = pygame.font.SysFont("Calibri", 22)
    # set text
    text = font.render(displaytext, True,(255,255,255),(0,0,0))
    # display text
    screen.blit(text, location)
    pygame.display.update()

def setScreenImg(img, caption = "Welcome to Carollexa!", location = (0,0)):
    screen.fill((0,0,0))
    
    # set caption
    pygame.display.set_caption(caption)
    
    # loading image
    screenimg = pygame.image.load(img)
    screenimg = pygame.transform.scale(screenimg, screen_dimensions)
    
    # set location of image on screen
    screen.blit(screenimg, location)
    pygame.display.update()

def sayText(text):
    engine.say(text)
    engine.runAndWait()


# set screen
pygame.init()
screen = pygame.display.set_mode(screen_dimensions)

engine=pyttsx3.init()
setScreenImg ("background.png")
setScreenText ("Welcome to Carollexa. Press \"s\" to interact, and \"q\" to quit.", (50,50))
sayText("Please wait while the app initializes. Press S to interact, and Q to quit")

isQuit = False

while isQuit == False:
    try:
        for event in pygame.event.get():
            pygame.display.update()
            time.sleep(.25)

            # check if user wants to quit
            if (event.type == pygame.QUIT):
                sayText('Have a good day!')
                isQuit = True
                break
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    recognizer=speech_recognition.Recognizer();
                
                    with speech_recognition.Microphone() as source:
                            recognizer.adjust_for_ambient_noise(source)
                            sayText("How may I help you?")
                            audio=recognizer.listen(source)            
                            #Convert Voice Commands to Text
                            command=recognizer.recognize_google(audio).lower()                
                            sayText("You said: "+command)
                            
                            bIsCommand = False
                            for keyword in music_dictionary:
                                if keyword in command:
                                    bIsCommand = True
                                    executeCommand(keyword)
                            if bIsCommand == False:
                                sayText("Unrecognized command")
                    setScreenImg("background.png")
                    setScreenText ("Welcome to Carollexa. Press \"s\" to interact, and \"q\" to quit.", (50,50))
               
                elif event.key == pygame.K_q: #activate=="q":
                        sayText('Have a good day!')
                        isQuit = True
                        break
        
                else:
                    sayText('I did not understand the command')
    
    #Stop Taking Voice Commands
    except speech_recognition.UnknownValueError:
        sayText("I did not understand the audio")
    except speech_recognition.RequestError as e:
        sayText("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break

# end while isQuit == False
    
pygame.quit()
sys.exit()
