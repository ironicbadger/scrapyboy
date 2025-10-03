---
video_id: "dneNjDu4HKU"
title: "Remote Raspberry Pi Setup Made Easy a Step-by-Step Guide"
description: "Today's video is aimed at those of you who have been wanting to get started with a Raspberry Pi but weren't sure where to start. Alex walks through the whole process from flashing the boot media to ge..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-09-29"
duration_seconds: 2587
youtube_url: "https://www.youtube.com/watch?v=dneNjDu4HKU"
thumbnail_url: "https://i.ytimg.com/vi/dneNjDu4HKU/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:18:00.885313"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 8416
transcription_time_seconds: 67.4
---

# Remote Raspberry Pi Setup Made Easy a Step-by-Step Guide

**[00:00](https://youtube.com/watch?v=dneNjDu4HKU&t=0s)** Hi, I'm Alex from Tailscale, and in today's video I'm going to show you how to get started with a Raspberry Pi. I've got a starter kit here that I got off Amazon for about $150 or so. It includes the Raspberry Pi 5 itself, of course. It also includes an active cooler because these new Raspberry Pi's are so powerful they need active cooling these days, as well as things like a power adapter and a case and SD card and all that kind of stuff. We'll dig into that throughout the video, don't worry. But if you're a complete beginner, I will do my absolute best today to not skip over

**[00:30](https://youtube.com/watch?v=dneNjDu4HKU&t=30s)** any of the little details like flashing the SD card or the USB sticks and whether you need an Ethernet cord or whether you need Wi-Fi, all of that stuff. I'm going to show you how to put Raspberry Pi OS on this thing today, as well as how to connect it to your tailnet so you can turn this thing into an exit node or a subnet router, and I'll come onto what those things do and mean and can do for you later on in the video. So, that's what today's video is going to be, a getting started guide for a Raspberry Pi 5. Okay, first things first, we need to have a look at what's in the box.

**[01:02](https://youtube.com/watch?v=dneNjDu4HKU&t=62s)** And this might sound weird to start with the power supply, but in the days of the Raspberry Pi 4, there were some issues with how the Raspberry Pi Foundation implemented the power spec on the USB-C port. And since that day, I've been very careful to select a official power supply whenever I'm dealing with the Raspberry Pi. Indeed, this is a USB-C 27 watt power adapter in my hands right here. Most USB-C cables have the ability to communicate.

**[01:32](https://youtube.com/watch?v=dneNjDu4HKU&t=92s)** By direction, so they request from the charger, I need X amount of power at this voltage, yada yada. But there was some weirdness with the Raspberry Pi 4, with how that USB-C port was hooked up, didn't follow the spec. So, they ran into some issues, where

**[01:46](https://youtube.com/watch?v=dneNjDu4HKU&t=106s)** chargers just weren't working properly with the Raspberry Pi 4 and it caused some issues. So, get yourself a solid USB-C power supply, that's the first thing. And it comes in the starter kit that's linked in the description down below.

**[01:59](https://youtube.com/watch?v=dneNjDu4HKU&t=119s)** Next thing is the active cooling. Again, this is the official Raspberry Pi active cooling solution. And it comes pre-baked with all of the thermal pads that you need to keep the Raspberry Pi cool. You can see on the top-down camera there, that this thing has the blue thermal pads that line up with the chips that need to be kept cool on the Raspberry Pi itself. So, I just slots on here and we'll do that later on. And that's included in the kit too.

**[02:24](https://youtube.com/watch?v=dneNjDu4HKU&t=144s)** Now, here is a slightly contentious point. I am not going to use microSD card today because they don't have the best right endurance. Now, typically in the old days at least, you used to have to boot a Raspberry Pi from a microSD card.

**[02:40](https://youtube.com/watch?v=dneNjDu4HKU&t=160s)** With the Raspberry Pi 5 and some later Raspberry Pi 4 firmwares, you no longer need to boot from an SD card. You can just boot directly from a USB drive. Isn't that fantastic?

**[02:52](https://youtube.com/watch?v=dneNjDu4HKU&t=172s)** So, what we need to do is install Raspberry Pi OS onto our boot medium. We need to install Raspberry Pi OS onto this USB stick. Now, most laptops, modern laptops, for whatever reason, only ship with USB-C ports. And I know Macbooks have shipped that way for a decade now, and I should just get over it.

**[03:15](https://youtube.com/watch?v=dneNjDu4HKU&t=195s)** But what will be wrong with a single USB-A port? Anyway, if you have the budget to buy yourself a brand new USB stick, I would highly recommend looking at these Sandisk ones because they have USB-A on one end but then USB-C on the other. And it's the same flash chip inside that gets accessed.

**[03:37](https://youtube.com/watch?v=dneNjDu4HKU&t=217s)** Now, if you don't have one of these fancy USB sticks, you can of course just use one of these standard USB-A sticks, but connecting into a Macbook, you're going to need a dongle. So, that's what I have right here.

**[03:47](https://youtube.com/watch?v=dneNjDu4HKU&t=227s)** This just takes a couple of USB-C ports and converts them into other ports, in my case. So, I'm going to put my USB stick into my dongle and then connect that into my laptop.

**[03:59](https://youtube.com/watch?v=dneNjDu4HKU&t=239s)** Next, I'm going to go to the internet and search for the Raspberry Pi Imager. And the Raspberry Pi Foundation make this software freely available.

**[04:08](https://youtube.com/watch?v=dneNjDu4HKU&t=248s)** In fact, this whole process is laughably easy compared to what it used to be several years ago, but we'll still walk you through the process today just to be complete.

**[04:16](https://youtube.com/watch?v=dneNjDu4HKU&t=256s)** Now, first thing we're going to need to do is click on this download for whatever operating system you're using. The process between Mac and Windows should be broadly the same.

**[04:24](https://youtube.com/watch?v=dneNjDu4HKU&t=264s)** Linux, Linux people, they do provide the Imager for Debian and Ubuntu. If you're on a different distro, you might need to get dirty with some other command line commands, but I doubt you're watching this video if you're already using Linux in anger on the desktop anyway.

**[04:38](https://youtube.com/watch?v=dneNjDu4HKU&t=278s)** If you are good for you, I suppose, but you probably already know how to make a USB disk.

**[04:43](https://youtube.com/watch?v=dneNjDu4HKU&t=283s)** OK, Mac OS is what we're using today, so I'm going to click on the download for Mac OS button. And as soon as that's finished downloading, I'm going to click on the DMG that appears and then drag and drop this into my applications folder.

**[04:55](https://youtube.com/watch?v=dneNjDu4HKU&t=295s)** Now, I already had the Pi Imager installed from a previous video that I made, so I'm just going to click replace. You probably won't see that prompt pop up. Now, if you're on Windows, of course, you'll go through the standard installer process and then you will be good to go.

**[05:10](https://youtube.com/watch?v=dneNjDu4HKU&t=310s)** Now, in the Mac world, you click on the finder and go to the applications menu and scroll through this list until you find Raspberry Pi Imager, or indeed you can do command space and use Spotlight to search for Raspberry Pi Imager.

**[05:24](https://youtube.com/watch?v=dneNjDu4HKU&t=324s)** Now, the next thing we're going to need to do is select our target device. In our case, that's the Raspberry Pi 5, and then we're going to want to select an OS that we're going to put on to this thing.

**[05:34](https://youtube.com/watch?v=dneNjDu4HKU&t=334s)** Now, I'm going to go to Raspberry Pi OS other. You'll see the default option here is the Debian Bookworm Raspberry Pi Desktop Raspberry Pi OS.

**[05:43](https://youtube.com/watch?v=dneNjDu4HKU&t=343s)** I don't want to put a desktop on here. This has, it has a lot of computing power, but it's still finite. So I want to save every single CPU cycle to make this into the most performant, headless Linux server that I possibly can.

**[05:56](https://youtube.com/watch?v=dneNjDu4HKU&t=356s)** And I don't want it burning up energy and CPU cycles on rendering a desktop environment that I'm never going to use.

**[06:04](https://youtube.com/watch?v=dneNjDu4HKU&t=364s)** So I'm going to go to the Raspberry Pi OS other option here, and then click on OS Lite. This is installing Debian Bookworm with no desktop environment, compatible with all the different Raspberry Pi variants.

**[06:18](https://youtube.com/watch?v=dneNjDu4HKU&t=378s)** Next, assuming that our USB stick is inside of our dongle and connected to our computer, it should just appear here in the storage list.

**[06:26](https://youtube.com/watch?v=dneNjDu4HKU&t=386s)** The next thing to do is to edit the settings. This is important because we need to do something like configuring our wireless LAN. So I'm going to put in my Wi-Fi information here of the wireless LAN, the SSID name, and then also the SSID password.

**[06:41](https://youtube.com/watch?v=dneNjDu4HKU&t=401s)** Now, this brings me to an important point. You can, if you want, skip the Wi-Fi configuration and just go straight for an Ethernet cable. That will plug straight into the Ethernet port of the Raspberry Pi like so.

**[06:55](https://youtube.com/watch?v=dneNjDu4HKU&t=415s)** And then also plug directly into something like this. This is an Ethernet switch. And this is a really cheap, unmanaged one by a company called Netgear. You're probably familiar with them if you're interested in home labbing or

**[07:07](https://youtube.com/watch?v=dneNjDu4HKU&t=427s)** computers of any description. These gigabit switches are more than plenty for what we're going to do with the Raspberry Pi and they're like $20 on Amazon. So hopefully not too much of an impediment to get started there.

**[07:19](https://youtube.com/watch?v=dneNjDu4HKU&t=439s)** You just plug each end of the Ethernet cord into the Raspberry Pi and the switch or your ISP router and you should be good to go.

**[07:26](https://youtube.com/watch?v=dneNjDu4HKU&t=446s)** So I am going to use Wi-Fi just to illustrate that we don't actually need anything more than a power cable to get started.

**[07:33](https://youtube.com/watch?v=dneNjDu4HKU&t=453s)** But I would caution that if you're going to be using this long term as a server, Ethernet's going to be more reliable and just less headaches overall. So if you can do Ethernet, do Ethernet.

**[07:44](https://youtube.com/watch?v=dneNjDu4HKU&t=464s)** But don't sweat it too much if you can't. So I've selected my wireless LAN information here, fill in the boxes, wireless LAN countries, set to US.

**[07:53](https://youtube.com/watch?v=dneNjDu4HKU&t=473s)** I'm going to set my local setting so that my keyboard layout and time zone are configured correctly. I am going to set the username and password here, Z4D and then a test password.

**[08:02](https://youtube.com/watch?v=dneNjDu4HKU&t=482s)** And then finally, I'm going to leave the host name alone, but finally, I need to go to this services box here and make sure that enable SSH is ticked.

**[08:10](https://youtube.com/watch?v=dneNjDu4HKU&t=490s)** This is so that once the Raspberry Pi boots up for the very first time, we can actually connect to it to configure it and install tail scale.

**[08:17](https://youtube.com/watch?v=dneNjDu4HKU&t=497s)** Now I'm going to set use password authentication for now because that's just the easiest thing to do. And then click save.

**[08:23](https://youtube.com/watch?v=dneNjDu4HKU&t=503s)** The next thing to do is to click, yes, I want to apply these customizations and then I want to overwrite the contents of this USB drive before I flash flash the data now.

**[08:33](https://youtube.com/watch?v=dneNjDu4HKU&t=513s)** Important caveat time. We're about to wipe everything off of this USB disk, never to be seen again.

**[08:40](https://youtube.com/watch?v=dneNjDu4HKU&t=520s)** So please be warned, do not do this with a USB drive. It has any important information on it because you will never be able to get it back.

**[08:48](https://youtube.com/watch?v=dneNjDu4HKU&t=528s)** Caviarce, but probably everything that's on there that you're about to wipe will be gone.

**[08:53](https://youtube.com/watch?v=dneNjDu4HKU&t=533s)** Now this process will take five or six minutes or so. So I'm not going to make you sit through that whole process and I'll be right back with the magic of editing.

**[09:02](https://youtube.com/watch?v=dneNjDu4HKU&t=542s)** Okay, looks like we're all done. So I'm going to click on continue to remove the says SD card, but it is just a US standard USB stick, as we said earlier.

**[09:11](https://youtube.com/watch?v=dneNjDu4HKU&t=551s)** Now the Raspberry Pi 5 has two sets of USB ports. One is black, one set is black and one set is blue.

**[09:19](https://youtube.com/watch?v=dneNjDu4HKU&t=559s)** And we want to put the USB stick into the blue port because that's the more performant one. That's the USB 3 port. So it has higher throughput into the Raspberry Pi.

**[09:29](https://youtube.com/watch?v=dneNjDu4HKU&t=569s)** These ones here, the black ones are only USB two speeds. So they are perfect for things like a keyboard or mouse.

**[09:35](https://youtube.com/watch?v=dneNjDu4HKU&t=575s)** But for any storage related devices or cameras or anything that has any higher throughput whatsoever, you always want to use the blue ports.

**[09:43](https://youtube.com/watch?v=dneNjDu4HKU&t=583s)** Next thing to do is to power it up. So I'm going to grab my power supply, plug it into my trusty extension lead right here.

**[09:51](https://youtube.com/watch?v=dneNjDu4HKU&t=591s)** And then I am literally just going to plug in the USB cable right here and that is all we need to do.

**[09:58](https://youtube.com/watch?v=dneNjDu4HKU&t=598s)** The Raspberry Pi now will just boot up and appear on the network, at least I hope it will.

**[10:04](https://youtube.com/watch?v=dneNjDu4HKU&t=604s)** Now I haven't mentioned displays at this point whatsoever. I have here the HDMI cable that comes in the starter kit.

**[10:11](https://youtube.com/watch?v=dneNjDu4HKU&t=611s)** The Raspberry Pi 5 has two micro HDMI ports and on the other end you can output to full size HDMI. So you can connect it up to your TV or indeed any other HDMI compatible screen.

**[10:23](https://youtube.com/watch?v=dneNjDu4HKU&t=623s)** We don't need this for a headless server, but purely for illustrative purposes for this video.

**[10:28](https://youtube.com/watch?v=dneNjDu4HKU&t=628s)** I am going to connect this up to the Pi so we can see what it's doing in the background.

**[10:31](https://youtube.com/watch?v=dneNjDu4HKU&t=631s)** And actually already you can see just in the minute or two there whilst I was messing about finding the cable,

**[10:37](https://youtube.com/watch?v=dneNjDu4HKU&t=637s)** the Raspberry Pi has now booted up and you can see the IP address that's actually been assigned to the Pi by the network.

**[10:43](https://youtube.com/watch?v=dneNjDu4HKU&t=643s)** So now if we go to my terminal window just over here and I do ping Raspberry Pi local,

**[10:49](https://youtube.com/watch?v=dneNjDu4HKU&t=649s)** you can see that 192-168-1.161 is the address that this Pi now has.

**[10:55](https://youtube.com/watch?v=dneNjDu4HKU&t=655s)** So now I should be able to connect via SSH from my local laptop here to the Raspberry Pi.

**[11:01](https://youtube.com/watch?v=dneNjDu4HKU&t=661s)** Now this is a moment where I'm not going to assume that you know what SSH is.

**[11:05](https://youtube.com/watch?v=dneNjDu4HKU&t=665s)** So SSH stands for Secure Shell and that is a way for me to control the processes that are running on this remote computer through nothing but text in the terminal.

**[11:17](https://youtube.com/watch?v=dneNjDu4HKU&t=677s)** So if I type SSH and then the username Z-Fod that we configured in the Raspberry Pi image earlier and then at the IP address of the Raspberry Pi,

**[11:27](https://youtube.com/watch?v=dneNjDu4HKU&t=687s)** I can now connect using SSH from this laptop into this Raspberry Pi so that I can start to manipulate it and control it

**[11:36](https://youtube.com/watch?v=dneNjDu4HKU&t=696s)** and make it do what we want in terms of installing tail scale and all the rest of the other things that we can do with Linux to be honest with you, not just Raspberry Pi's.

**[11:46](https://youtube.com/watch?v=dneNjDu4HKU&t=706s)** Now you remember earlier in the video when I talked to you about how much better of an experience you might have with a cable over Wi-Fi.

**[11:53](https://youtube.com/watch?v=dneNjDu4HKU&t=713s)** Just look at the lag I'm experiencing right here. If I type just H-top into the terminal, which H-top is the way that I can view the running process as a bit like system monitor or activity monitor would be on Mac or Windows, this is not usable is it.

**[12:10](https://youtube.com/watch?v=dneNjDu4HKU&t=730s)** So I'll be right back. I'm going to switch out to an ethernet cable to try and reduce the latency between this laptop and this Raspberry Pi.

**[12:17](https://youtube.com/watch?v=dneNjDu4HKU&t=737s)** Even though they are sat, mere inches away from each other, the Wi-Fi traffic has to go from here to my Wi-Fi access point below my feet in the ceiling down to his back up through, it shouldn't be this slow and I don't know why it is.

**[12:30](https://youtube.com/watch?v=dneNjDu4HKU&t=750s)** And this is one of the reasons why I never really recommend Wi-Fi for server situations is because it can just be slow.

**[12:39](https://youtube.com/watch?v=dneNjDu4HKU&t=759s)** One other thing that you should note too is that the Raspberry Pi 5 has a power button I know I know we're in the 21st century folks but just on the top here you can see next to the red LED look there is a little power button so if I press that now it will turn from red to green.

**[12:57](https://youtube.com/watch?v=dneNjDu4HKU&t=777s)** And we can boot the Raspberry Pi up that way instead now I'm hoping that when I plug in this ethernet cable there's going to take precedence with the cable over the Wi-Fi that we can figure.

**[13:07](https://youtube.com/watch?v=dneNjDu4HKU&t=787s)** And we'll find out shortly because if it comes back up with the IP address of 161 that we had earlier we'll know that the DHCP lease was grandfathered in from the old Wi-Fi chip but I see here that we've actually got 1.160 so that tells me hopefully that it has indeed taken precedent with the ethernet cable and you saw much faster that loaded up just then.

**[13:31](https://youtube.com/watch?v=dneNjDu4HKU&t=811s)** Now I'm going to jump over to make other station because we don't need to be doing anything more physically with the Raspberry Pi at this point say for perhaps installing the fan and the CPU cooler on top so let's actually let's do that before before we go over to the bench over to my desk we're at the bench and so yeah let's do that now i'm going to unpeel these little stickies right here and then.

**[13:58](https://youtube.com/watch?v=dneNjDu4HKU&t=838s)** Just connect this up so how we want to do it right we're going to line it up the CPU goes here and then these two chips are is this one here I think is the I don't know is that the network not sure and then this one is power power supplies over there of course because it's coming in by the USB regulator over there and i'm going to line in line up this little plastic pin with this plastic hole plastic pin here and then just push down on the plastic pins until until they click through obviously.

**[14:30](https://youtube.com/watch?v=dneNjDu4HKU&t=870s)** Like the old Intel if you remember 20 years ago how Intel do stock heatsinks used to connect in so these little plastic pins here they sort of barb through the holes and connect the the fan up now there's another little header just in here where we have to get this little plastic.

**[14:49](https://youtube.com/watch?v=dneNjDu4HKU&t=889s)** This little tiny little plastic thing out and put that on the bench and then all we want to do is connect up this fan so i'm going to look at the orientation there are two little pins on either side.

**[15:00](https://youtube.com/watch?v=dneNjDu4HKU&t=900s)** Line up with the orientation of the hole that we need so that's the orientation we need and then i'm just going to connect up the fan cable and we are now good to go this is a actively cooled Raspberry Pi 5 now so hopefully it runs nice and cool and quiet so i'm going to once again grab my power cable plug that in.

**[15:21](https://youtube.com/watch?v=dneNjDu4HKU&t=921s)** Grab my ethernet cable plug that in make sure that's good to go and then my display cable even though that's entirely optional for you dear viewer okay well i can tell you that the fan works i don't know if that comes across our mic but it reminds me of like the old laptop fans of your small and shrill but let's have a look yeah we're back up now so if I do SSH again.

**[15:55](https://youtube.com/watch?v=dneNjDu4HKU&t=955s)** Fantastic i'm back into the pie so this is all booted up now in fact you can even see that the heat sink isn't that the fan isn't even spinning right now that the passive heat sink for just running the pie idle seems to be everything that it needs.

**[16:07](https://youtube.com/watch?v=dneNjDu4HKU&t=967s)** So that's going to do us for this portion of the video as I say we're going to jump over to the desk now i'm going to show you how to get tail scale installed and configure your first applications on the Raspberry Pi.

**[16:18](https://youtube.com/watch?v=dneNjDu4HKU&t=978s)** So what do you want to do we want to do a few things in the next few minutes and bear in mind there are chapters down below if you want to skip around in the video probably should have said that at the beginning but there you go.

**[16:27](https://youtube.com/watch?v=dneNjDu4HKU&t=987s)** We want to install tail scale we're going to install docker as well if you've heard of docker it's a way to run applications in what are called containers that isolated happy accidents of code.

**[16:39](https://youtube.com/watch?v=dneNjDu4HKU&t=999s)** The allow you to run applications without worrying about how they deployed you just do a docker run command and it figures it out it's it's kind of cool it's kind of magic and I love docker and we're also then going to configure the Raspberry Pi to run as what's called a subnet router so we can access things like printers and other devices in our local network or the network where the Raspberry Pi happens to be.

**[17:03](https://youtube.com/watch?v=dneNjDu4HKU&t=1023s)** Without physically being in that network it's very it's just a very useful backup if nothing else.

**[17:10](https://youtube.com/watch?v=dneNjDu4HKU&t=1030s)** It's quite an advanced thing like if you know you need a subnet router you probably have been looking for a solution like this for a while.

**[17:16](https://youtube.com/watch?v=dneNjDu4HKU&t=1036s)** And then the other thing we're going to do is configure an exit node from the previous Raspberry Pi to run as an exit node so the purpose of that is that you can take all of the packets and all of the traffic that comes from a client device so that could be your phone it could be a laptop.

**[17:30](https://youtube.com/watch?v=dneNjDu4HKU&t=1050s)** Doesn't really matter any device that can run tail scale can then send all of its traffic out through that Raspberry Pi as if that client device was on the same physical network as the Raspberry Pi itself.

**[17:40](https://youtube.com/watch?v=dneNjDu4HKU&t=1060s)** So an example for this might be for example you put the Raspberry Pi at your parents house I don't know they're in another state or whatever I don't know.

**[17:50](https://youtube.com/watch?v=dneNjDu4HKU&t=1070s)** And you want to route all the traffic from where you are out through your parents house for some reason.

**[17:55](https://youtube.com/watch?v=dneNjDu4HKU&t=1075s)** That's exactly what an exit node can do and it's it's the same model as all of the typical privacy VPNs use so I won't name names but you know typically the VPNs you see advertised.

**[18:07](https://youtube.com/watch?v=dneNjDu4HKU&t=1087s)** They are what's called privacy VPNs and they allow you to funnel all of the traffic through a VPN encrypted connection from your client device out through their service which you don't control.

**[18:17](https://youtube.com/watch?v=dneNjDu4HKU&t=1097s)** They come out in data center IP blocks which get all sorts of spammers and things like that associated to those IP blocks so you end up with a ton more captures on your internet traffic and that kind of thing.

**[18:30](https://youtube.com/watch?v=dneNjDu4HKU&t=1110s)** But with tail scale and using an exit node in a residential IP you can figure it out right you just get a normal residential grade internet connection so you don't get kind of

**[18:43](https://youtube.com/watch?v=dneNjDu4HKU&t=1123s)** bucketed put put in the bucket with spammers and all the rest of it so you know with a much better internet experience as a consequence online banking works better that way too.

**[18:51](https://youtube.com/watch?v=dneNjDu4HKU&t=1131s)** There's a lot of reasons why it's really useful so first thing we need to do probably is install tail scale so to do that we're going to head over to tailscale.com slash download.

**[19:02](https://youtube.com/watch?v=dneNjDu4HKU&t=1142s)** And you're out of your pies running Linux of course so the browser detected that my local laptop is running Mac OS and that's not what we want we want to go to Linux and copy this string when I say string I mean these characters here onto my clipboard i'm going to go back to my terminal manager.

**[19:20](https://youtube.com/watch?v=dneNjDu4HKU&t=1160s)** I think I skipped that only by the way and in case you were lost I use an app called ghosty for my terminal but macOS ships with one built in as well called terminal.

**[19:30](https://youtube.com/watch?v=dneNjDu4HKU&t=1170s)** And you can just as well use that if you want to now you can see that it doesn't have some other fanciness that mine does like it doesn't quite know how to render some of these they're called glyphs in the terminal so I ended up with a bunch of question marks whatever but I can still type in here and do exactly the same thing that i'm doing in ghosty.

**[19:46](https://youtube.com/watch?v=dneNjDu4HKU&t=1186s)** It's totally up to you which one you use I really like ghosty it's done by Mitchell Hashimoto the guy who helped found hashie corp back in the day.

**[19:54](https://youtube.com/watch?v=dneNjDu4HKU&t=1194s)** This is this current project and it's it's great so digress a little just to go back i've copied this curl command to my clipboard and i'm going to go back to my raspberry pie and i'm going to paste it into the command line right here now at some point it's going to download a bunch of packages and it's going to looks you're going to look like your you're in a hacker movie right now is all this text scrolls by.

**[20:19](https://youtube.com/watch?v=dneNjDu4HKU&t=1219s)** Essentially what it's doing is it's going out to debian dot org and grabbing the latest list of packages that are available and a package on linux essentially is a piece of software that somebody has packaged up into the name and released and done a bunch of stuff with like versioning and what have you.

**[20:38](https://youtube.com/watch?v=dneNjDu4HKU&t=1238s)** So debian keep a list of that stuff in what are called repositories what we've just done is effectively an apt update command.

**[20:46](https://youtube.com/watch?v=dneNjDu4HKU&t=1246s)** Well technically we've added some tail scale specific repositories that we own and we maintain and then we've updated that list of packages that are available and then we've told debian to go ahead and download tail scale and all of the other packages that tail scale needs to run.

**[21:02](https://youtube.com/watch?v=dneNjDu4HKU&t=1262s)** Those things are called dependencies and that's why it can look like such a long list is because what i'm just installing tail scale outside.

**[21:10](https://youtube.com/watch?v=dneNjDu4HKU&t=1270s)** Well yeah but tail scale needs things like IP tables and as you can see it needs lib IP six TC to the bunch of other stuff besides.

**[21:20](https://youtube.com/watch?v=dneNjDu4HKU&t=1280s)** Of course it needs go because tail scales written in the go programming language bunch of other stuff to so so tail scales install package or tail scales package takes care of all that stuff for you are still script takes care of all that stuff for you.

**[21:33](https://youtube.com/watch?v=dneNjDu4HKU&t=1293s)** So by the time we're done here you will have the tail scale package installed along with all of its dependencies and you'll be able to just start using tail scale without really having to worry too much about how to configure anything else under the hood.

**[21:47](https://youtube.com/watch?v=dneNjDu4HKU&t=1307s)** Okay there we go now you can see that the tail scale installation is complete and i'm going to type pseudo tail scale up i'm also going to do dash dash SSH.

**[21:57](https://youtube.com/watch?v=dneNjDu4HKU&t=1317s)** This is going to allow us to SSH into the Raspberry Pi from any tail scale client device regardless of whether we have an SSH key configured or not.

**[22:06](https://youtube.com/watch?v=dneNjDu4HKU&t=1326s)** Now because we use the Raspberry Pi imager from this laptop i have this laptops SSH key because i have one generated previously.

**[22:14](https://youtube.com/watch?v=dneNjDu4HKU&t=1334s)** You may very well have been asked to enter a password when you SSH for the first time and but tail scale SSH it's not like a special.

**[22:22](https://youtube.com/watch?v=dneNjDu4HKU&t=1342s)** You don't need to use the tail scale SSH command you can just use your ordinary SSH commands and it will transparently pick up the SSH keys in the process it's kind of magic right so i'm going to do a command click on this URL right here to open it in my browser if I just click on this link nothing happens.

**[22:38](https://youtube.com/watch?v=dneNjDu4HKU&t=1358s)** If i do a command click i can actually open this in a browser i'm going to assume you've already got a tail scale account but if you haven't you can head over to tail scale dot com to get started.

**[22:48](https://youtube.com/watch?v=dneNjDu4HKU&t=1368s)** We offer a hundred devices and three users for free on our personal plan we've committed that plan will remain free forever so enjoy that and if you couldn't fill up a hundred devices in your personal tail net it's good for you.

**[23:04](https://youtube.com/watch?v=dneNjDu4HKU&t=1384s)** Okay now i've already signed up for tail scale a long time ago with this sort of fake email here a tail and scales at gmail dot com i mean emails real but it's just for demonstrative purposes in these videos.

**[23:14](https://youtube.com/watch?v=dneNjDu4HKU&t=1394s)** i'm going to click on the signing with Google option and as you can see we support Microsoft GitHub Apple past keys you can even self host your own authentication if you want to.

**[23:23](https://youtube.com/watch?v=dneNjDu4HKU&t=1403s)** And I put a link to a video about tsi dp up here which is our own self hostable.

**[23:28](https://youtube.com/watch?v=dneNjDu4HKU&t=1408s)** Authentication server that runs on what's called the OIDC open ID connect protocol that allows you to do just that now i'm going to click on this and sign in to my specific town that you can see i've got a couple here you probably won't see this screen.

**[23:42](https://youtube.com/watch?v=dneNjDu4HKU&t=1422s)** But because I do lots of demos for this channel I go have a couple of extra bits turned on i'm going to connect this Raspberry Pi to our town it.

**[23:51](https://youtube.com/watch?v=dneNjDu4HKU&t=1431s)** Okay so that should be done in fact behind the scenes we can see that it is already done so.

**[23:57](https://youtube.com/watch?v=dneNjDu4HKU&t=1437s)** My laptop is already connected to this tail net and I can show you that with tail scale status is going to list all of the devices on my town it and you can see I have a brand new one that's the Raspberry Pi right here.

**[24:10](https://youtube.com/watch?v=dneNjDu4HKU&t=1450s)** Now beforehand we had to know the IP address of the Raspberry Pi to SSH into it right not anymore all I need to know now is the tail scale network node name which in this case is Raspberry Pi and I can do SSH Raspberry Pi now SSH keys no extra configuration and i'm in and I could do that from any other device on my town so if I have.

**[24:32](https://youtube.com/watch?v=dneNjDu4HKU&t=1472s)** Blink on my iOS device which is a way to get a shell on your iOS device.

**[24:38](https://youtube.com/watch?v=dneNjDu4HKU&t=1478s)** Simply connect that device to your tail net and type SSH Raspberry Pi and you'll be in it's magic and on the Raspberry Pi of course now I can do tail scale status and I can see.

**[24:49](https://youtube.com/watch?v=dneNjDu4HKU&t=1489s)** All of the other devices on my town it and I can do tail scale ping let's do let's ping this device in my house to a device at my mother in law's house in England all the way across the Atlantic Ocean how about that let's do tail scale ping UK exit Norwich and after four five different pings there you go tail scale has just established a direct connection from that Raspberry Pi in this room to my server in England.

**[25:18](https://youtube.com/watch?v=dneNjDu4HKU&t=1518s)** Remember she's a brand new like you've seen the configuration in real time i've been doing today i haven't had to do anything complicated and there are no firewall rules to to mess around with or anything.

**[25:29](https://youtube.com/watch?v=dneNjDu4HKU&t=1529s)** Just works i'm laying it on thick today but really like that is the magic of tail scale is that you can just connect anything to anything and it's really super easy to get started.

**[25:40](https://youtube.com/watch?v=dneNjDu4HKU&t=1540s)** Okay, we have tail scale installed is probably time to get docker installed and we can do that by going to get dot docker dot com and they provide this little script here now i'm going to modify the tail scale install command that we used earlier and just.

**[25:56](https://youtube.com/watch?v=dneNjDu4HKU&t=1556s)** Copy and get dot docker dot com this is going to install docker now on to our Raspberry Pi so once that's done i'll be right back.

**[26:04](https://youtube.com/watch?v=dneNjDu4HKU&t=1564s)** And with that docker is now installed now is the command we can run just to verify that so we do docker run dash dash rm hello world and this.

**[26:15](https://youtube.com/watch?v=dneNjDu4HKU&t=1575s)** Will promptly tell me that my safe would user is not in the docker group so i can do pseudo bang banged with exclamation marks and it will run the previous command as pseudo.

**[26:27](https://youtube.com/watch?v=dneNjDu4HKU&t=1587s)** Rest a super user.

**[26:30](https://youtube.com/watch?v=dneNjDu4HKU&t=1590s)** Downloading the latest image hello world yet okay so docker is installed and working properly now if we want to be able to run containers as the non route user we can do user mod a g i think it's safe i think it's.

**[26:44](https://youtube.com/watch?v=dneNjDu4HKU&t=1604s)** Add to group and then say ford we have to do it as pseudo and now if we type ID we can see that this user is not in the docker group but if we log out.

**[26:57](https://youtube.com/watch?v=dneNjDu4HKU&t=1617s)** And log back in again and do ID we can see that we've been added where is it here we go added to the docker group so this means we can now run our hello world command without doing pseudo and these are little things i think as a new user that trip you up that people don't include in.

**[27:15](https://youtube.com/watch?v=dneNjDu4HKU&t=1635s)** Documentation or.

**[27:17](https://youtube.com/watch?v=dneNjDu4HKU&t=1637s)** Explanation videos just like this one so i've left little mistakes like that in throughout the video and i try to do that on the channel in general to be honest.

**[27:27](https://youtube.com/watch?v=dneNjDu4HKU&t=1647s)** Because i feel like each of each of those moments is a teachable moment or something right so now we know that docker is installed and running and we've got tail scale installed and running on the Raspberry Pi.

**[27:40](https://youtube.com/watch?v=dneNjDu4HKU&t=1660s)** Let's do something useful or somewhat useful at least let's install our first app on the tail net so I have used vibe coding to create a very very simple demo application that we're going to use for our purposes today.

**[27:56](https://youtube.com/watch?v=dneNjDu4HKU&t=1676s)** This is this runs in docker and its entire purpose is to show you that you can connect to a remote node over tail scale and some of the identity that gets exposed through the tail scale identity headers they get included as part of.

**[28:10](https://youtube.com/watch?v=dneNjDu4HKU&t=1690s)** Every single web request you make on the internet so what we want to do is just clone this get repo put a link to it in the description the ironic badger that's me.

**[28:20](https://youtube.com/watch?v=dneNjDu4HKU&t=1700s)** TSNet hello world i'm going to go to this big green code button here and copy that I clipboard now i'm going to go back to the shell of my Raspberry Pi I like to put all of my get repos in a directory in the home users folder called get creative I know.

**[28:36](https://youtube.com/watch?v=dneNjDu4HKU&t=1716s)** But if I do mkdure make directory get I can now then change directory or cd into that get directory next I want to use get to clone this repo to the Raspberry Pi and now that's just copied all of that source code look if I go into so LS lists the contents of a specific directory that you're in.

**[28:57](https://youtube.com/watch?v=dneNjDu4HKU&t=1737s)** If I change directory into that tSNet hello world directory you can see I've got all of the source code that was on get up now locally on this Raspberry Pi and so if I go back to the read me instructions as part of this project we can see that.

**[29:12](https://youtube.com/watch?v=dneNjDu4HKU&t=1752s)** I'm going to want to rename the dot end dot example file to dot end so let's do that let's do move mv dot end dot example to dot end.

**[29:25](https://youtube.com/watch?v=dneNjDu4HKU&t=1765s)** Okay that was easy enough now I almost always default using them on this channel but I know some of you prefer nano so let's use nano today and we do nano which is a text editor dot end so we.

**[29:37](https://youtube.com/watch?v=dneNjDu4HKU&t=1777s)** Can just modify just this line right here where it says TS or key now what's an or key I haven't covered that yet so an or key is a way to authenticate.

**[29:48](https://youtube.com/watch?v=dneNjDu4HKU&t=1788s)** A container or a node or a device or a client or anything that can run tail scale code to your tail nets that you know it is yours or so that tail scale knows it's yours and we can generate an or key by going to our admin console over at tail scale dot com so up here at the top there's a button that says admin console and then moving over to the settings option right here and then go down to keys copy or actually want to go generate or key first i'm going to make mine reusable and call this one.

**[30:16](https://youtube.com/watch?v=dneNjDu4HKU&t=1816s)** Hello world doesn't really matter what you call it you can leave all the rest of this stuff just completely default and copy that to your clipboard next we want to replace the value of everything after the equals sign with just on our clipboard just the value that we put on to our clipboard next we want to save the contents of this file and we do that with a control X and then press Y to do so and that will write out the contents of that file to disk so we're now getting one step closer to being able to deploy.

**[30:47](https://youtube.com/watch?v=dneNjDu4HKU&t=1847s)** Application what else we've got left to do we've generated an or key we renamed our end file and now actually yeah we can just deploy this application so let's do Docker compose up dash dash build you're actually building an application from source code right now using Docker using the Raspberry Pi using tail scale all the things we've covered in this video so far just on that little computer that we flashed a few minutes ago.

**[31:11](https://youtube.com/watch?v=dneNjDu4HKU&t=1871s)** This is why I really love self hosting and and kind of hacking around with these little single board computers is because it exposes you to things that you just wouldn't otherwise do like sure you could sign up for a subscription service to do half of what you do with self hosting and pay someone else to have all the fun.

**[31:28](https://youtube.com/watch?v=dneNjDu4HKU&t=1888s)** But I can't think of a better video game done the Linux terminal to be honest with you so.

**[31:33](https://youtube.com/watch?v=dneNjDu4HKU&t=1893s)** It's probably why I'm in the right career so we are reaching the final stages of the build right now and I've opened another terminal window in the background ssh into the Raspberry Pi and you can see that we are actually pushing the Raspberry Pi pretty hard right now all four CPU cores are well.

**[31:50](https://youtube.com/watch?v=dneNjDu4HKU&t=1910s)** Dipping in and out of 100% usage as go compiles that source code into our final application once this step is done it's going to join the application to our tail scale network we call it tail net once that's done and we will then be able to access the application in our web browser which we'll get on to next.

**[32:10](https://youtube.com/watch?v=dneNjDu4HKU&t=1930s)** Right so there we are the application has now built let's go and check we can actually access it shall we we can see here that it worked out that it needed a log in so it started to enter.

**[32:19](https://youtube.com/watch?v=dneNjDu4HKU&t=1939s)** Active login process in the background it's also started tail scale serve enabled but funnel false now tail scale serve is a way to expose a web application to just your tail net tail scale funnel is a way to expose a web application to the entire internet.

**[32:36](https://youtube.com/watch?v=dneNjDu4HKU&t=1956s)** So only use funnel with extreme caution because anybody and I do mean anybody from the internet can get to it without opening any ports in your firewall or anything like that because it just puts it out on the public internet.

**[32:48](https://youtube.com/watch?v=dneNjDu4HKU&t=1968s)** So only you serve if you're absolutely sure that's what you need most of the time you just want things on your tail net with a URL that you can access so let's grab the URL for this application.

**[33:00](https://youtube.com/watch?v=dneNjDu4HKU&t=1980s)** We can see here that this is the list of nodes on my tail net which now includes T s hello world who we can see all sorts of interesting stuff about this know like the tail scale version it's using we can see it has this bill info thing here because it's built from source code and it's not like a typical client release.

**[33:18](https://youtube.com/watch?v=dneNjDu4HKU&t=1998s)** Like some of the other things here so you see one dot eight eight dot one for example.

**[33:23](https://youtube.com/watch?v=dneNjDu4HKU&t=2003s)** Those are client releases that are built by tail scale proper 1.86 is what happens when you compile it from source code you can even see the Linux kernel of the kernel of the of the node underneath.

**[33:35](https://youtube.com/watch?v=dneNjDu4HKU&t=2015s)** So here now this for example is running on macOS 15.6.1 but this one hello world is running on the Linux kernel 6.12 such running on the Raspberry Pi now let's get back to the task at hand and load this into our

**[33:48](https://youtube.com/watch?v=dneNjDu4HKU&t=2028s)** web browser let's grab the fully qualified domain name right here create a new tab paste that in boom is easy as that it isn't easy as that so we you hopefully if you're following along are now running your very first application on your Raspberry Pi that you compiled from source on a Raspberry Pi that you flash the operating system for just a few minutes ago.

**[34:15](https://youtube.com/watch?v=dneNjDu4HKU&t=2055s)** It's fantastic OK and all of this information is exposed over the tail net using the ID headers built into your web browser now the next thing we need to do is create a will turn this node into a exit node for tail scale as well as a subnet router so let's do tail scale as an exit node.

**[34:34](https://youtube.com/watch?v=dneNjDu4HKU&t=2074s)** Now if you're still here from the previous chapter to quit out of the application that you built from source is just a control see OK easy as that.

**[34:42](https://youtube.com/watch?v=dneNjDu4HKU&t=2082s)** If you want to bring that up in the background by the way you can just add a minus D and that will run the application in the background for you you never really have to worry about it and you can see that it's still accessible over your tail net just fine OK so now let's set tail scale up as an exit node so we do tail scale set dash dash advertise exit node and that's it except we have to do it as route so we do my pseudo bang bang trick again.

**[35:07](https://youtube.com/watch?v=dneNjDu4HKU&t=2107s)** And there we go this node is now officially an exit node on your town it almost we need to go to our admin console next and look for the Raspberry Pi where did it go search for Pi.

**[35:20](https://youtube.com/watch?v=dneNjDu4HKU&t=2120s)** There it is and you can see that we've got the exit node option here with an exclamation point next to it we need to make sure that the admin of the town that approves and it's probably you in this case but we need to make sure that the admin approves this node for use as an exit node.

**[35:36](https://youtube.com/watch?v=dneNjDu4HKU&t=2136s)** So all we do in our tail scale admin console is click on the three dot menu click on edit route settings check the box.

**[35:44](https://youtube.com/watch?v=dneNjDu4HKU&t=2144s)** It's it we're done now any node on your town it no matter where it is in the world can route traffic out through this Raspberry Pi as if it was in this same physical building is that cool so let's take this laptop for example I know I'm in the same physical building as the Raspberry Pi I know it's not the most impressive example but it would still work whether I went to the coffee shop or not.

**[36:04](https://youtube.com/watch?v=dneNjDu4HKU&t=2164s)** But you can see I now have Raspberry Pi as an option where I didn't before it's as easy as that okay let's do a subnet routers next so we can do tail scale set.

**[36:15](https://youtube.com/watch?v=dneNjDu4HKU&t=2175s)** Here are all the different options we can use for tail scale sets so I want to advertise a subnet route that means that I can access over the tailnet devices that don't natively run tail scale over tail scale because this node effectively acts as like a.

**[36:30](https://youtube.com/watch?v=dneNjDu4HKU&t=2190s)** Do you remember the male man in men in black with five arms under the table like this node effectively acts as like central dispatch for all of the packets on your network so you publish a route for a specific what's called a subnet which is like a grouping of IP addresses.

**[36:46](https://youtube.com/watch?v=dneNjDu4HKU&t=2206s)** You say to any other node on your town it hey if you see a node that has an IP address in that subnet send it to the Raspberry Pi over there via tail scale.

**[36:56](https://youtube.com/watch?v=dneNjDu4HKU&t=2216s)** It will then take that subnet and package it up and send that package over your tailnet and then it will come out of the Raspberry Pi and reach assuming the Raspberry Pi can route a packet to that remote target come out through the Raspberry Pi as if it was the Raspberry Pi itself making that request.

**[37:12](https://youtube.com/watch?v=dneNjDu4HKU&t=2232s)** But I've probably just gone to level 27 when actually some of you are wondering what's a subnet how do I know what I want to advertise all that kind of stuff.

**[37:21](https://youtube.com/watch?v=dneNjDu4HKU&t=2241s)** It's actually quite straightforward so if we do an IPA on a Linux box we get presented with a huge number of different what are called interfaces.

**[37:32](https://youtube.com/watch?v=dneNjDu4HKU&t=2252s)** You can see here that we've got my Wi-Fi interface as WLAN zero this has the IP address that we saw earlier of 1921681.161 slash 24 now.

**[37:43](https://youtube.com/watch?v=dneNjDu4HKU&t=2263s)** The slash 24 is an important distinction because that shows what's called the cider CID CID R.

**[37:52](https://youtube.com/watch?v=dneNjDu4HKU&t=2272s)** Sider.

**[37:53](https://youtube.com/watch?v=dneNjDu4HKU&t=2273s)** Oh, I want to sign in now.

**[37:55](https://youtube.com/watch?v=dneNjDu4HKU&t=2275s)** Anyway, that shows the side that it's being used and the slash 24 means that there's 200 and I think it's 255 devices available in this subnet.

**[38:04](https://youtube.com/watch?v=dneNjDu4HKU&t=2284s)** So the first IP address available in this subnet is 1.1 the last address is 19216 1.254.

**[38:12](https://youtube.com/watch?v=dneNjDu4HKU&t=2292s)** Now this is what's called a slash 24 subnet and I know for a fact that this network its cider is a slash 24 because it told me as part of the IPA command.

**[38:24](https://youtube.com/watch?v=dneNjDu4HKU&t=2304s)** If I do my IP space A again we can see that my WLAN has 161 and that my ethernet zero that's the cable that we plugged in has a 160.24.

**[38:35](https://youtube.com/watch?v=dneNjDu4HKU&t=2315s)** So I want to be able to access another device in that tailnet over tail scale using a subnet router with this route right here.

**[38:45](https://youtube.com/watch?v=dneNjDu4HKU&t=2325s)** So let me copy that selection to my clipboard type in tail scale set once more just to get the syntax of I want to do tail scale set dash dash

**[38:55](https://youtube.com/watch?v=dneNjDu4HKU&t=2335s)** advertise routes equals and then I'm going to put in the subnet now rather than putting in the specific IP address of a specific node in that subnet.

**[39:05](https://youtube.com/watch?v=dneNjDu4HKU&t=2345s)** I'm going to use the specially reserved dot zero at the beginning of the cider this way tail scale knows to pattern match anything that is on that 192168 slash 24 subnet and send that out through through the subnet router that way.

**[39:21](https://youtube.com/watch?v=dneNjDu4HKU&t=2361s)** So when I type set of course I'm going to do it pseudo now any time I want to send a packet to that remote subnet okay this laptops already in that subnet so it would it would work just fine.

**[39:33](https://youtube.com/watch?v=dneNjDu4HKU&t=2373s)** But if I get if I take this laptop somewhere else I can now use my Raspberry Pi as well as like a Trojan horse right as long as you're connected tail scale you can get in through the front door without knocking it's pretty cool.

**[39:46](https://youtube.com/watch?v=dneNjDu4HKU&t=2386s)** But just like an exit node we need to make sure that we've actually advertised and allowed the correct routes so you can see here the subnet option has a similar kind of exclamation point next to it that the exit node option did before so if I do edit route settings now we can see that one route is advertised but not approved so if I check this box right here and click save now I am able to publish these routes as ones that can be rooted through the Raspberry Pi.

**[40:15](https://youtube.com/watch?v=dneNjDu4HKU&t=2415s)** I hope that makes sense and subnet routing is actually kind of an advanced topic to be honest but it's an incredibly useful one so if I take you over to the tail scale subnet routing page you'll find a tail scale explain video from yours truly that I made a couple of years ago at this point talking about subnet routers in excruciating detail but what I've just shown you is basically what's in that video just a little less nuanced I suppose.

**[40:42](https://youtube.com/watch?v=dneNjDu4HKU&t=2442s)** But it's essentially let you extend your tail scale network beyond just the devices that can run tail scale incredibly handy and very very useful.

**[40:50](https://youtube.com/watch?v=dneNjDu4HKU&t=2450s)** I can't think of anything else specific to show you today I would just invite you to go and look at the tail scale dev repo where I have a bunch of code snippets from all of the repo all of the videos I publish on this channel showing you how to set up things like self hosted get server or a recipe manager or indeed in self hosting part two which I'll put a link to that video up here.

**[41:11](https://youtube.com/watch?v=dneNjDu4HKU&t=2471s)** It was a long one but it was a good one I think where you can set up things like yourself hosted audible clone with audio bookshelf and you can replace Google photos with image and all of that stuff will run just fine on that little Raspberry Pi over there in the corner it really is amazing what you can do with very low low power hardware these days that thing will just sip electricity in the corner of just a couple of watts when it's not doing much.

**[41:35](https://youtube.com/watch?v=dneNjDu4HKU&t=2495s)** It's yeah what a time to be alive okay so that is I think going to do us for today that is my version of a getting started guide with the Raspberry Pi 5.

**[41:46](https://youtube.com/watch?v=dneNjDu4HKU&t=2506s)** If you have any questions please head over to our brand new discord discord dot gg slash tail scale.

**[41:53](https://youtube.com/watch?v=dneNjDu4HKU&t=2513s)** There may or may not be by the time you watch this video a new channel over there called in the comments where you can go and.

**[41:59](https://youtube.com/watch?v=dneNjDu4HKU&t=2519s)** Ask questions and come and ping me I think I'm over there Alex Ktz I will answer questions as best I can or indeed drop a comment down below or whatever you want to do.

**[42:08](https://youtube.com/watch?v=dneNjDu4HKU&t=2528s)** But you know I need discord is is pop in as a couple of thousand people in there it's only been active for a couple of weeks so come join us have some fun place and world talk tail scale what was what more could you like.

**[42:20](https://youtube.com/watch?v=dneNjDu4HKU&t=2540s)** Get subscribed to the channel of course we've got a bunch of content coming about CICD in the coming weeks as well so if you want to start.

**[42:26](https://youtube.com/watch?v=dneNjDu4HKU&t=2546s)** Learning how you can take some of this stuff to work and actually start using tail scale to make your work life easier which you can by the way.

**[42:34](https://youtube.com/watch?v=dneNjDu4HKU&t=2554s)** There will be a bunch of stuff coming on the channel about that too if you're going to be in rally in October I'm going to be all things open which is what's about a month away from now is October 13th or so you will take.

**[42:46](https://youtube.com/watch?v=dneNjDu4HKU&t=2566s)** Come by the tail scale booth and grab a t-shirt I'll be happy to see you there and until next time thank you so much for watching I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
