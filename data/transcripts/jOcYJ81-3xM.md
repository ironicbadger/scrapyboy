---
video_id: "jOcYJ81-3xM"
title: "5 beginner friendly tips to get more from your Tailnet"
description: "If you've been looking for new and interesting ways to use Tailscale but you're not super technical, then this video is for you.

Today, I'll show you how to:

- Use Taildrop for secure encrypted file..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-04-17"
duration_seconds: 392
youtube_url: "https://www.youtube.com/watch?v=jOcYJ81-3xM"
thumbnail_url: "https://i.ytimg.com/vi_webp/jOcYJ81-3xM/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T18:19:01.661187"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1216
transcription_time_seconds: 10.6
---

# 5 beginner friendly tips to get more from your Tailnet

**[00:00](https://youtube.com/watch?v=jOcYJ81-3xM&t=0s)** Welcome into today's video. I'm Alex from Tailscale, and in today's video I'm going to walk you through five top tips that you can try to get started with Tailscale. Tip number one, Taildrop. Now let's be honest, at some point in your life, you have emailed yourself a sensitive document. Because emails are encrypted, you've effectively just sent your social security number across the public internet for anybody to get hold of. Well, wouldn't it be nice if there was a way to create an encrypted tunnel between two devices you own and send five

**[00:30](https://youtube.com/watch?v=jOcYJ81-3xM&t=30s)** files with a couple of taps? Well, using Taildrop, you can do just that. So I have a highly classified piece of 3D printing merchandise here. This is my very first ever 3D printer, a little benchy boy. I'm going to take a photo of this on a Google Pixel, and send it from Android to a Mac with no complicated configuration required. Taildrop, in just a couple of taps, let's be send that photo from the pixel to MacOS or anywhere else that Tailscale runs Taildrop.

**[00:59](https://youtube.com/watch?v=jOcYJ81-3xM&t=59s)** We support a wide range of different OSs, and this is the easiest way to send a file between two devices that you own. So stop emailing yourself, stuff across the public internet in an unencrypted fashion, and use Taildrop instead. It's included for free in every Tailscale plan, where you get three users and 100 devices for free.

**[01:21](https://youtube.com/watch?v=jOcYJ81-3xM&t=81s)** Tip number two, use an Apple TV as a Tailscale Exit node. To do this, you'll want to install the Tailscale app on your Apple TV, and then scan the QR code that appears on the screen using your phone. So in my case, I just have an Android phone here. It's then going to take me into a browser and ask me to do the standard login procedure.

**[01:39](https://youtube.com/watch?v=jOcYJ81-3xM&t=99s)** I'm going to log in with my test Google account right here, and then add this node to my tailnet. Once the Apple TV is connected, enabling exit node functionality is really straightforward. Head on over to the exit node menu and click on Run as exit node.

**[01:54](https://youtube.com/watch?v=jOcYJ81-3xM&t=114s)** I'm going to select the option to run as an exit node, then head over to tailscale.com and go to your admin console. Once in the admin console, find the Apple TV that you just added. Click on the three dot menu and edit route settings.

**[02:08](https://youtube.com/watch?v=jOcYJ81-3xM&t=128s)** Check the box that says use as exit node, and now your Apple TV can be used as an exit node for your tailnet. Now the Apple TV makes a particularly great device to pick for this kind of use case because of its low idle power consumption.

**[02:22](https://youtube.com/watch?v=jOcYJ81-3xM&t=142s)** This thing will sit there under your TV quietly, pulling less than one watt most of the time, waiting for these connections. So what an exit node allows you to do is route packets, let's say you're at the coffee shop and you need to pretend that you're at your house for some reason in terms of your network traffic.

**[02:38](https://youtube.com/watch?v=jOcYJ81-3xM&t=158s)** You can route those packets out through the Apple TV as if you were physically sat in this room plugged into the Apple TV box somehow, and you can route those packets through the Apple TV and exit, hence the name exit node, you can exit your traffic through that node on your tailnet.

**[02:56](https://youtube.com/watch?v=jOcYJ81-3xM&t=176s)** Tip number three, use your Apple TV as a subnet router. Now I will admit this is quite close to tip number two, but a subnet router lets you access devices within the network, the physical network that the Apple TV is sat within from anywhere else on your tailnet.

**[03:12](https://youtube.com/watch?v=jOcYJ81-3xM&t=192s)** So let's say you need to access a printer remotely or a scanner or some other device that can't run tailscale for some reason. It's pretty unusual because tailscale runs on most things, but there are certain scenarios where that can make sense.

**[03:22](https://youtube.com/watch?v=jOcYJ81-3xM&t=202s)** We'll use the Apple TV and its low power state to access those devices remotely over tailscale.

**[03:31](https://youtube.com/watch?v=jOcYJ81-3xM&t=211s)** Tip number four, stream video games from your powerful gaming GPU to anywhere in the world over tailscale.

**[03:39](https://youtube.com/watch?v=jOcYJ81-3xM&t=219s)** I'm going to use Apollo and Moonlight here to do this, so I'm running the Apollo clients on my Windows gaming desktop in another building.

**[03:47](https://youtube.com/watch?v=jOcYJ81-3xM&t=227s)** This is now streaming over the internet over tailscale with no firewall rules configured and it's streaming steam big picture mode directly to my MacBook.

**[03:57](https://youtube.com/watch?v=jOcYJ81-3xM&t=237s)** Now the same thing will work on a steam deck, you know, I can install Apollo on here and stream video games directly using Moonlight to my handheld device as well.

**[04:06](https://youtube.com/watch?v=jOcYJ81-3xM&t=246s)** So I can use my powerful gaming rig with a video, you know, 3080 in it or whatever and stream those video games over the network to wherever I am playing to wherever I happen to be.

**[04:17](https://youtube.com/watch?v=jOcYJ81-3xM&t=257s)** That means I can play games of different OSs, so a Windows only game I can now play on Mac OS.

**[04:23](https://youtube.com/watch?v=jOcYJ81-3xM&t=263s)** So like dwarf fortress, I can now play on Mac OS if I want to over tailscale. I'm just going to show you very quickly here what's horizon five running over the network.

**[04:33](https://youtube.com/watch?v=jOcYJ81-3xM&t=273s)** So typically these kinds of game streaming engines have issues switching resolutions. So this is a 5K 2K display right here, a 21 by 9 aspect ratio.

**[04:43](https://youtube.com/watch?v=jOcYJ81-3xM&t=283s)** The display that's actually connected to my PC downstairs is only a 4K 16 by 9 display and what Apollo does is it creates a virtual display of the resolution matching the target client resolution.

**[04:54](https://youtube.com/watch?v=jOcYJ81-3xM&t=294s)** So I get a perfect 21 by 9 aspect ratio image here. And as you can see, I'm running this thing, well according to the frame counter in the corner, 60 FPS over the network over tailscale.

**[05:06](https://youtube.com/watch?v=jOcYJ81-3xM&t=306s)** And this is running in a completely another building, isn't that amazing? I think it's amazing.

**[05:11](https://youtube.com/watch?v=jOcYJ81-3xM&t=311s)** So tip number four, stream video games using Apollo and they'll be linked to that project in the description down below, as well as a full video coming to the channel in the near future about streaming your games over tailscale.

**[05:25](https://youtube.com/watch?v=jOcYJ81-3xM&t=325s)** Tip number five, use tailscale to connect to remote desktop systems, wherever they are in the world. So I have a window system in another building.

**[05:34](https://youtube.com/watch?v=jOcYJ81-3xM&t=334s)** It's actually the one that was running the Windows 11 gaming demo moment ago. And I'm going to go to my network devices just here.

**[05:40](https://youtube.com/watch?v=jOcYJ81-3xM&t=340s)** Click on my devices and get the IP address for win 11 gaming. I'm then going to add a new host here. I'm going to add PC.

**[05:48](https://youtube.com/watch?v=jOcYJ81-3xM&t=348s)** I'm going to paste in that IP address. You can also use the DNS host name if you would like, but the IP address will just work regardless of your network setup.

**[05:56](https://youtube.com/watch?v=jOcYJ81-3xM&t=356s)** And now I'm going to click on add. And when I do that and double click on it, I'm going to be asked for my username and password. And lo and behold, I can now remote desktop using Windows RDP's native protocols into a remote system, wherever I am and wherever it is in the world over tailscale.

**[06:14](https://youtube.com/watch?v=jOcYJ81-3xM&t=374s)** So there we are. Five top tips for tailscale tryouts. Thank you so much for watching and until next time I've been Alex from tailscale.

---

*Automatically generated transcript. May contain errors.*
