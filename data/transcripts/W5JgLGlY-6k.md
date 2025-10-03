---
video_id: "W5JgLGlY-6k"
title: "Mazanoke - A self-hosted, local image resizer that respects your privacy"
description: "Mazanoke is a self-hosted local image optimizer that runs in your browser. Use this a fully local, privacy respecting alternative to the hosted options that do who knows what with the images you uploa..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-04-23"
duration_seconds: 456
youtube_url: "https://www.youtube.com/watch?v=W5JgLGlY-6k"
thumbnail_url: "https://i.ytimg.com/vi/W5JgLGlY-6k/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:01:03.657283"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1461
transcription_time_seconds: 13.8
---

# Mazanoke - A self-hosted, local image resizer that respects your privacy

**[00:00](https://youtube.com/watch?v=W5JgLGlY-6k&t=0s)** Hi, I'm Alex from Tailscale, and in today's video, I want to show you a self-hosted app

**[00:04](https://youtube.com/watch?v=W5JgLGlY-6k&t=4s)** pick I found called Mazanoki, Mazanook. I'm not entirely sure of the name, but what this

**[00:11](https://youtube.com/watch?v=W5JgLGlY-6k&t=11s)** app does, it's a pretty straightforward thing, is it's a self-hosted local image optimizer

**[00:17](https://youtube.com/watch?v=W5JgLGlY-6k&t=17s)** that's fully open-source and it runs in your browser. So I'm going to show you today how to put

**[00:22](https://youtube.com/watch?v=W5JgLGlY-6k&t=22s)** this app onto your tailnet so that you can access it from anywhere. Now in my line of work,

**[00:28](https://youtube.com/watch?v=W5JgLGlY-6k&t=28s)** resizing images is something I do multiple times a day. So to have some kind of an ad-free

**[00:33](https://youtube.com/watch?v=W5JgLGlY-6k&t=33s)** self-hosted privacy-respecting application that runs on infrastructure that I own and I control,

**[00:39](https://youtube.com/watch?v=W5JgLGlY-6k&t=39s)** it's very exciting for me. So let's go and grab an image. I have the Pangolin WWF page loaded up

**[00:46](https://youtube.com/watch?v=W5JgLGlY-6k&t=46s)** here because of course Pangolins have both the tail and scales. Yes, very good. Let's just grab a picture,

**[00:53](https://youtube.com/watch?v=W5JgLGlY-6k&t=53s)** I don't know this one here, and let's see what we can do with it. So I'm going to throw this into my

**[00:57](https://youtube.com/watch?v=W5JgLGlY-6k&t=57s)** downloads folder and then go to, this is running on a local system, by the way, not currently on my

**[01:02](https://youtube.com/watch?v=W5JgLGlY-6k&t=62s)** tailnet, but we'll get to that in just a second. I'm going to look at the settings I've got here.

**[01:07](https://youtube.com/watch?v=W5JgLGlY-6k&t=67s)** So let's limit the file size of this to, I don't know, let's do kilobytes, let's do 10 kilobytes

**[01:16](https://youtube.com/watch?v=W5JgLGlY-6k&t=76s)** no way, let's do 512 kilobytes. Now I'm going to browse for the image in my downloads folder,

**[01:22](https://youtube.com/watch?v=W5JgLGlY-6k&t=82s)** oh, it's already only 90 kilobytes. Well, in that case, I don't know if you saw my video last week

**[01:27](https://youtube.com/watch?v=W5JgLGlY-6k&t=87s)** where I demo tail drop, which is an easy way to send files between the devices, but I have this

**[01:32](https://youtube.com/watch?v=W5JgLGlY-6k&t=92s)** beautiful picture of my first ever 3D printed Benji. So let's resize this because this is 3.7 meg,

**[01:39](https://youtube.com/watch?v=W5JgLGlY-6k&t=99s)** let's resize this from 3.7 megabytes to 512 kilobytes. Let's open this image in here and you can see it's

**[01:47](https://youtube.com/watch?v=W5JgLGlY-6k&t=107s)** done. Now I didn't get anywhere close to 512 kilobytes, I will point out, but we didn't change the

**[01:53](https://youtube.com/watch?v=W5JgLGlY-6k&t=113s)** resolution or anything like that. So you know, so what's that? It's a pretty, pretty large resolution

**[01:57](https://youtube.com/watch?v=W5JgLGlY-6k&t=117s)** file at 1.9 megs, it's pretty good. So let's see what else we can do here. If we go to set,

**[02:03](https://youtube.com/watch?v=W5JgLGlY-6k&t=123s)** limit dimensions to, yeah, let's do 1024 and then I'm going to also select PNG and just see what

**[02:12](https://youtube.com/watch?v=W5JgLGlY-6k&t=132s)** this does. I'm going to leave the file size limit thing the same, 3.7 megs, and it's done,

**[02:18](https://youtube.com/watch?v=W5JgLGlY-6k&t=138s)** and this time I'll win much closer at 778 kilobytes. So play around with these features and there's

**[02:24](https://youtube.com/watch?v=W5JgLGlY-6k&t=144s)** a lot of cool stuff you can do with this app, Matsunoki. So now I've shown you the basics of this

**[02:29](https://youtube.com/watch?v=W5JgLGlY-6k&t=149s)** app and it is pretty basic, but I don't know, it looks pretty cool to me. Let's get this thing

**[02:35](https://youtube.com/watch?v=W5JgLGlY-6k&t=155s)** deployed onto our tailnet using Docker. Now I've covered Docker many times on this channel. In

**[02:39](https://youtube.com/watch?v=W5JgLGlY-6k&t=159s)** fact, you can click up here to see a video about Docker and how you can get started if you need

**[02:44](https://youtube.com/watch?v=W5JgLGlY-6k&t=164s)** more information. Now to make this as simple as possible, I provide code snippets for all of this

**[02:49](https://youtube.com/watch?v=W5JgLGlY-6k&t=169s)** stuff. So this compose YAML file is available in GitHub here at TailScaleDev, video code snippets,

**[02:56](https://youtube.com/watch?v=W5JgLGlY-6k&t=176s)** and they'll be a link to that in the description down below. And we're here, we're pretty much ready to

**[03:00](https://youtube.com/watch?v=W5JgLGlY-6k&t=180s)** go, but we do need to do a couple of things on our tailnet just to make sure that everything is in

**[03:05](https://youtube.com/watch?v=W5JgLGlY-6k&t=185s)** position for us. So first of all, we need to grab an auth key. So to do that, we go to tailscale.com

**[03:12](https://youtube.com/watch?v=W5JgLGlY-6k&t=192s)** and we go to our machines page, followed by settings over here once we're logged in.

**[03:17](https://youtube.com/watch?v=W5JgLGlY-6k&t=197s)** Then we go down to keys on the left and click generate auth key. Now I'm going to select reusable

**[03:23](https://youtube.com/watch?v=W5JgLGlY-6k&t=203s)** just because I'm doing a demo. So I'll likely spin up and tear it down a couple of times, but for you,

**[03:27](https://youtube.com/watch?v=W5JgLGlY-6k&t=207s)** you can probably just leave this default exactly as it is. I'm going to click on generate key,

**[03:32](https://youtube.com/watch?v=W5JgLGlY-6k&t=212s)** copy that to my clipboard and put this into the auth key variable right here in VS code.

**[03:37](https://youtube.com/watch?v=W5JgLGlY-6k&t=217s)** Now we also want to just take a quick note of the host name. So in my case, that's images. So

**[03:43](https://youtube.com/watch?v=W5JgLGlY-6k&t=223s)** that's the name that this tailscale container is going to get when it joins my tailnet.

**[03:48](https://youtube.com/watch?v=W5JgLGlY-6k&t=228s)** Also, we probably want to have some kind of TLS, some kind of HTTPS certificate, right? So I've also

**[03:54](https://youtube.com/watch?v=W5JgLGlY-6k&t=234s)** provided a JSON file here, which basically is going to proxy port 80 from inside the container onto

**[04:00](https://youtube.com/watch?v=W5JgLGlY-6k&t=240s)** your tailnet. This is basically a reverse proxy configuration, but specific to tailscale using

**[04:05](https://youtube.com/watch?v=W5JgLGlY-6k&t=245s)** tailscale serve. Now you can configure tailscale serve using an environment variable, and we're

**[04:10](https://youtube.com/watch?v=W5JgLGlY-6k&t=250s)** going to do that here using TS serve config. We also need to add the associated volume for this

**[04:16](https://youtube.com/watch?v=W5JgLGlY-6k&t=256s)** file. So we can do PWD for current working directory or print working directory. I'm going to do

**[04:22](https://youtube.com/watch?v=W5JgLGlY-6k&t=262s)** maths and no key, and then I'm just going to do config, and then I'm going to mount that inside the

**[04:26](https://youtube.com/watch?v=W5JgLGlY-6k&t=266s)** container to slash config, and then I'll put the dot JSON file in that directory on the remote

**[04:31](https://youtube.com/watch?v=W5JgLGlY-6k&t=271s)** system. So using my tailscale extension, I'm going to copy this to my clipboard, navigate to the

**[04:37](https://youtube.com/watch?v=W5JgLGlY-6k&t=277s)** remote system. So in my case, that's TS apps find the location of my remote compose file or create

**[04:44](https://youtube.com/watch?v=W5JgLGlY-6k&t=284s)** it. So I can right click on these directories and just interact with them as if I was actually,

**[04:48](https://youtube.com/watch?v=W5JgLGlY-6k&t=288s)** as if they were local directories. So I've really created this new file and put the contents in here.

**[04:54](https://youtube.com/watch?v=W5JgLGlY-6k&t=294s)** So we should be good to go on that one. Now within the maths and no key folder, I'm going to also

**[04:59](https://youtube.com/watch?v=W5JgLGlY-6k&t=299s)** create the config directory because this is where our JSON configuration for tailscale service

**[05:06](https://youtube.com/watch?v=W5JgLGlY-6k&t=306s)** going to live. So just copy and paste in a couple of files around here, nothing too crazy. So

**[05:13](https://youtube.com/watch?v=W5JgLGlY-6k&t=313s)** so I'm going to call this one, what did I call it, maths, maths on okey dot JSON, I think,

**[05:19](https://youtube.com/watch?v=W5JgLGlY-6k&t=319s)** and just like that, we've got all of the files on our remote system that we need to actually get started.

**[05:24](https://youtube.com/watch?v=W5JgLGlY-6k&t=324s)** Another nice thing that you can do with the VS code extension is you can hover over the node itself

**[05:28](https://youtube.com/watch?v=W5JgLGlY-6k&t=328s)** and bring up a shell in any of these directories. So in my case, I want to be in the compose.yaml

**[05:34](https://youtube.com/watch?v=W5JgLGlY-6k&t=334s)** directory. So I'm going to go to containers and then hover over this and click on terminal.

**[05:40](https://youtube.com/watch?v=W5JgLGlY-6k&t=340s)** And this is going to open a terminal directly in VS code in the remote location on that remote node.

**[05:45](https://youtube.com/watch?v=W5JgLGlY-6k&t=345s)** And I can type Docker compose up. And what's going to happen there is it's going to create both

**[05:50](https://youtube.com/watch?v=W5JgLGlY-6k&t=350s)** containers. It's going to join the TS Matzonoki container to my tailnet as well as starting the

**[05:57](https://youtube.com/watch?v=W5JgLGlY-6k&t=357s)** Matzonoki service. So it's spinning up two containers and we can verify this by going back to my

**[06:02](https://youtube.com/watch?v=W5JgLGlY-6k&t=362s)** tailnet and looking for the images node right here. So I'm going to copy this images.Volossaraptor

**[06:09](https://youtube.com/watch?v=W5JgLGlY-6k&t=369s)** high for noodle fish. By the way, I should also point out, I've said this in many Docker videos,

**[06:14](https://youtube.com/watch?v=W5JgLGlY-6k&t=374s)** but I can't pre-suppose you've watched all of those videos. So just very quickly,

**[06:19](https://youtube.com/watch?v=W5JgLGlY-6k&t=379s)** my tailnet name is set here under the DNS tab and you can rename your tailnet from the default

**[06:25](https://youtube.com/watch?v=W5JgLGlY-6k&t=385s)** name, which will look like this, to have a name that looks like a tail, something with a tail

**[06:29](https://youtube.com/watch?v=W5JgLGlY-6k&t=389s)** and something with scales. And then at the bottom, we want to make sure that magic DNS is enabled

**[06:34](https://youtube.com/watch?v=W5JgLGlY-6k&t=394s)** along with HTTPS. And once we've done that, I should be able to just copy and paste into my browser.

**[06:41](https://youtube.com/watch?v=W5JgLGlY-6k&t=401s)** And voila, I have a full HTTPS certificate for this service running on my tailnet, which means I can

**[06:50](https://youtube.com/watch?v=W5JgLGlY-6k&t=410s)** access this service from any other device on my tailnet anywhere in the world. So you could throw

**[06:56](https://youtube.com/watch?v=W5JgLGlY-6k&t=416s)** this on a Raspberry Pi, under your stairs, or you could throw it at friends or a family member's

**[07:00](https://youtube.com/watch?v=W5JgLGlY-6k&t=420s)** house, or we could throw this on a VPS in the middle of the Pacific Ocean if you wanted to.

**[07:04](https://youtube.com/watch?v=W5JgLGlY-6k&t=424s)** And you could access it from anywhere. That's the magic of tailscales natural virtual technology.

**[07:09](https://youtube.com/watch?v=W5JgLGlY-6k&t=429s)** Now, if you want to find out more about tailscale and how you can bring us to work,

**[07:12](https://youtube.com/watch?v=W5JgLGlY-6k&t=432s)** you can head over to tailscale.com slash BTW and join over 10,000 paying customers.

**[07:18](https://youtube.com/watch?v=W5JgLGlY-6k&t=438s)** As always, thank you so much for watching and until next time, I've been Alex from tailscale.

---

*Automatically generated transcript. May contain errors.*
