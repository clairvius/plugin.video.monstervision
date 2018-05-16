import urlparse
import sys,urllib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urlresolver
import os,requests,urllib2,re




base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

_addon = xbmcaddon.Addon()
_icon = _addon.getAddonInfo('icon')



def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def resolve_url(url):
    duration=7500   #in milliseconds
    message = "Cannot Play URL"
    stream_url = urlresolver.HostedMediaFile(url=url).resolve()
    # If urlresolver returns false then the video url was not resolved.
    if not stream_url:
        dialog = xbmcgui.Dialog()
        dialog.notification("URL Resolver Error", message, xbmcgui.NOTIFICATION_INFO, duration)
        return False
    else:        
        return stream_url    

def play_video(path):
    """
    Play a video by the provided path.
    :param path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    vid_url = play_item.getfilename()
    stream_url = resolve_url(vid_url)
    if stream_url:
        play_item.setPath(stream_url)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)

# addon kicks in

mode = args.get('mode', None)


if mode is None:
    video_play_url = "https://openload.co/f/jZlK1qL9NmA/TNT_Monstervision_Joe_Bob_Briggs_Presents_Slaughter_High.mp4"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Slaughter High', iconImage='https://i.imgur.com/QmX16hR.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

    video_play_url = "https://openload.co/f/i6en49nqvV8/TNT_Monstervision_Joe_Bob_Briggs_Presents_Xtro_2.mp4"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Xtro 2', iconImage='https://i.imgur.com/YpHnzXf.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)


    video_play_url = "https://openload.co/f/kXNhVdl2ql0/TNT_Monstersion_Joe_Bob_Briggs_Presents_Breeders.mp4"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Breeders', iconImage='https://i.imgur.com/v2uRc6O.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

    video_play_url = "https://openload.co/f/RWEnFlmW9Do/TNT_Monstervision_Joe_Bob_Briggs_Presents_The_Beast_Within.mp4"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('The Beast Within', iconImage='https://i.imgur.com/9Xkg0tz.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

    video_play_url = "https://openload.co/f/kY-QPG_ffKQ/TNT_Monstervision_Joe_Bob_Briggs_Presents_The_Ice_Cream_Man.mp4"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('The Ice-Cream Man', iconImage='https://i.imgur.com/iQPyaNK.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

    video_play_url = "https://openload.co/f/F5MPGd5cRKk/TNT_Monstervision_Joe_Bob_Briggs_Presents_Worlock_II_The_Armadeddon.mp4"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Worlock II The Armageddon', iconImage='https://i.imgur.com/tfd4RSk.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li) 

    video_play_url = "https://openload.co/f/IRFh2ZrelV0/TNT_Monstervision_Joe_Bob_Briggs_Presents_Halloween_II.mp4"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Halloween II', iconImage='https://i.imgur.com/Jwy53E7.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

    video_play_url = "https://openload.co/f/8IIM3V9O_Uc/TNT_Monstervision_Joe_Bob_Briggs_Presents_Halloween_III_Season_of_the_Witch.mp4"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Halloween III Season of the Witch', iconImage='https://i.imgur.com/ZoWAMBz.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
   
    video_play_url = "https://openload.co/f/D9O37h2rxIQ/TNT_Monstervision_Joe_Bob_Briggs_Presents_Bettlejuice.mp4"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Beetlejuice', iconImage='https://i.imgur.com/MZQyykh.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    
    video_play_url = "https://openload.co/f/KfJ6H5HMTF0/TNT_Monstervision_Joe_Bob_Briggs_Presents_Burnt_Offerings"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Burnt Offerings', iconImage='https://i.imgur.com/yNVQxHb.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    
    video_play_url = "https://openload.co/f/y84BVS4DfWI/TNT_Monstervision_Joe_Bob_Briggs_Presents_Carrie"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Carrie', iconImage='https://i.imgur.com/ts2snFJ.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    
    video_play_url = "https://openload.co/f/w9sxwGjwJEk/TNT_Monstervision_Joe_Bob_Briggs_Presents_Big_Trouble_in_Little_China"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Big Trouble in Little China', iconImage='https://i.imgur.com/JrcAEWA.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
   
    video_play_url = "https://openload.co/f/c2LpERTL2CU/TNT_Monstervision_Joe_Bob_Briggs_Presents_Child%27s_Play_2.mp4"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Childs Play II', iconImage='https://i.imgur.com/S0gkZRE.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
     
    video_play_url = "https://openload.co/f/0xv6LDq8Q1s/TNT_Monstervision_Joe_Bob_Briggs_Presents_Critters.mp4"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Critters', iconImage='https://i.imgur.com/tx3D4f2.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    
    video_play_url = "https://openload.co/f/tuVJoCfs68Y/TNT_Monstervision_Joe_Bob_Briggs_Presents_Children_of_the_Corn_II.mp4"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Children of the Corn II', iconImage='https://i.imgur.com/oZpkd5C.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
     
    video_play_url = "https://openload.co/f/3yYdqGzkjik/TNT_Monstervision_Joe_Bob_Briggs_Presents_Friday_the_13th_Part_2"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Friday the 13th Part II', iconImage='https://i.imgur.com/5SP5l41.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
         
    video_play_url = "https://openload.co/f/kHaURlyq0A4/TNT_Monstervision_Joe_Bob_Briggs_Presents_Friday_the_13th_VI"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Friday the 13th Part VI', iconImage='https://i.imgur.com/hfGeVOz.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
             
    video_play_url = "https://openload.co/f/TMR6AR7Wuvw/TNT_Monstervision_Joe_Bob_Briggs_Presents_Ghoulies_II"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Ghoulies II', iconImage='https://i.imgur.com/I0Iuo50.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
                 
    video_play_url = "https://openload.co/f/fno2GiGW2VY/TNT_Monstervision_Joe_Bob_Briggs_Presents_Friday_the_13TH"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Friday the 13th', iconImage='https://i.imgur.com/1DtC8DW.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
                 
    video_play_url = "https://openload.co/f/qXLJ7A1avJo/TNT_Monstervision_Joe_Bob_Briggs_Presents_Ghoulies"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Ghoulies', iconImage='https://i.imgur.com/O6z1Krc.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
                     
    video_play_url = "https://openload.co/f/NkeL5JtDZoI/TNT_Monstervision_Joe_Bob_Briggs_Presents_House_IV"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('House IV', iconImage='https://i.imgur.com/eVhBsmu.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
                      
    video_play_url = "https://openload.co/f/VuKtCbEB-PU/TNT_Monstervision_Joe_Bob_Briggs_Presents_In_the_Mouth_of_Madness"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('In the Mouth of Madness', iconImage='https://i.imgur.com/6lWgjcn.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
                          
    video_play_url = "https://openload.co/f/Tpzex2dHTlU/TNT_Monstervision_Joe_Bob_Briggs_Presents_Gremlins"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Gremlins', iconImage='https://i.imgur.com/2EqywrJ.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
                              
    video_play_url = "https://openload.co/f/Njod7FadZU4/TNT_Monstervision_Joe_Bob_Briggs_Presents_It_Lives_Again"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Its Alive II It Lives Again', iconImage='https://i.imgur.com/1zUOl7F.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
                                
    video_play_url = "https://openload.co/f/-jsXsBOfdbw/TNT_Monstervision_Joe_Bob_Briggs_Presents_It%27s_Alive_III_Island_of_Alive"
    url = build_url({'mode' :'play', 'playlink' : video_play_url})
    li = xbmcgui.ListItem('Its Alive III Island of Alive', iconImage='https://i.imgur.com/JYPWalE.jpg')
    li.setProperty('IsPlayable' , 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
                                                                                                                                                                                                           
    xbmcplugin.endOfDirectory(addon_handle)


elif mode[0] == 'play':
    final_link = args['playlink'][0]
    play_video(final_link)
