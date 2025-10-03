---
video_id: "WjeVNsL1s9U"
title: "Behind the scenes of creating Octoprint and using Tailscale as an open source developer"
description: "Join us for a new series on the channel where we talk to the folks behind some of your favorite software projects.

- OctoPrint: https://octoprint.org
- The mentioned blog post: https://octoprint.org/..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-02-23"
duration_seconds: 1324
youtube_url: "https://www.youtube.com/watch?v=WjeVNsL1s9U"
thumbnail_url: "https://i.ytimg.com/vi/WjeVNsL1s9U/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T18:09:42.344286"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 3798
transcription_time_seconds: 32.3
---

# Behind the scenes of creating Octoprint and using Tailscale as an open source developer

**[00:00](https://youtube.com/watch?v=WjeVNsL1s9U&t=0s)** Late last year, I was browsing Twitter, and I found a post from a lady called Gina. She

**[00:05](https://youtube.com/watch?v=WjeVNsL1s9U&t=5s)** is the open source developer behind the project, Octoprint, an open source 3D printing

**[00:10](https://youtube.com/watch?v=WjeVNsL1s9U&t=10s)** web interface. We got talking, and I thought actually her story was pretty interesting.

**[00:15](https://youtube.com/watch?v=WjeVNsL1s9U&t=15s)** And so what follows in today's video is an interview with Gina talking about how she

**[00:19](https://youtube.com/watch?v=WjeVNsL1s9U&t=19s)** uses Tailscale as part of the open source build process for Octoprint, connecting the Raspberry

**[00:26](https://youtube.com/watch?v=WjeVNsL1s9U&t=26s)** price on her desk with GitHub actions in the cloud, and just bringing them all together.

**[00:31](https://youtube.com/watch?v=WjeVNsL1s9U&t=31s)** So join me in this new series on the channel where we interview developers from various projects

**[00:36](https://youtube.com/watch?v=WjeVNsL1s9U&t=36s)** across the internet with Gina from Octoprint. I'm delighted to welcome Gina from Octoprint to

**[00:43](https://youtube.com/watch?v=WjeVNsL1s9U&t=43s)** the channel. A few months ago, we got talking about how Octoprint has a very unique challenge

**[00:49](https://youtube.com/watch?v=WjeVNsL1s9U&t=49s)** around building infrastructure and testing software between GitHub actions and Raspberry

**[00:56](https://youtube.com/watch?v=WjeVNsL1s9U&t=56s)** Pies running on Gina's desk. So that's what we're going to talk about today is how we can connect

**[01:02](https://youtube.com/watch?v=WjeVNsL1s9U&t=62s)** different remote infrastructure building tools together using Tailscale under the hood. So

**[01:08](https://youtube.com/watch?v=WjeVNsL1s9U&t=68s)** welcome Gina. Hi there. So what got you first into building Octoprint? Actually, I should probably

**[01:16](https://youtube.com/watch?v=WjeVNsL1s9U&t=76s)** wind back for those people that don't know what Octoprint is in the first place. Let's do the elevator

**[01:20](https://youtube.com/watch?v=WjeVNsL1s9U&t=80s)** pitch of what is Octoprint. Yeah, so Octoprint is the snappy weapon interface for your 3D printer

**[01:27](https://youtube.com/watch?v=WjeVNsL1s9U&t=87s)** and it so happened that in November 2012, so over 10 years ago, 11 years ago, no actually,

**[01:35](https://youtube.com/watch?v=WjeVNsL1s9U&t=95s)** I got myself my first ever 3D printer and back then when those things where yeah, even less

**[01:42](https://youtube.com/watch?v=WjeVNsL1s9U&t=102s)** plug and play than they are today, you have to basically tee that into your computer all the time.

**[01:48](https://youtube.com/watch?v=WjeVNsL1s9U&t=108s)** Keep an eye on them like personally. You had this thing sitting in your in my case in your office.

**[01:57](https://youtube.com/watch?v=WjeVNsL1s9U&t=117s)** Basically taking up your PC all the time while it got fed the data that it needed to print.

**[02:04](https://youtube.com/watch?v=WjeVNsL1s9U&t=124s)** Then the print took hours, two days on end. It produced fumes. It produced noise all the time

**[02:10](https://youtube.com/watch?v=WjeVNsL1s9U&t=130s)** and all in all it was just quite annoying to have a tie up PC all the whole time. Sit on your

**[02:16](https://youtube.com/watch?v=WjeVNsL1s9U&t=136s)** office all the time and such and you're not being able to use the room anymore for anything else,

**[02:21](https://youtube.com/watch?v=WjeVNsL1s9U&t=141s)** or the PC for anything else anymore. I so happened to had a vacation coming up then over Christmas.

**[02:31](https://youtube.com/watch?v=WjeVNsL1s9U&t=151s)** The Raspberry Pi had just come out in that year and so what I did was I sat down and

**[02:38](https://youtube.com/watch?v=WjeVNsL1s9U&t=158s)** yeah, basically created myself a little web interface that would allow me to monitor the 3D printer

**[02:44](https://youtube.com/watch?v=WjeVNsL1s9U&t=164s)** through a web camera connected to a Raspberry Pi. The Raspberry Pi directly hooked up to the printer,

**[02:49](https://youtube.com/watch?v=WjeVNsL1s9U&t=169s)** feeding it data, getting a full feedback loop going there knowing when the job would be done

**[02:58](https://youtube.com/watch?v=WjeVNsL1s9U&t=178s)** seeing if there were any errors and errors on all that and basically just allowing me to put that

**[03:02](https://youtube.com/watch?v=WjeVNsL1s9U&t=182s)** thing in my spare bathroom instead of tying up my office here. That's the way to do it. I can't

**[03:10](https://youtube.com/watch?v=WjeVNsL1s9U&t=190s)** actually imagine a 3D printer without a remote control these days. If you look at some of the

**[03:15](https://youtube.com/watch?v=WjeVNsL1s9U&t=195s)** new ones, they come with all this stuff baked in, but it's important to note that I guess,

**[03:19](https://youtube.com/watch?v=WjeVNsL1s9U&t=199s)** if you're talking about Raspberry Pi 1, that was 2012-ish. It had just come out in that

**[03:26](https://youtube.com/watch?v=WjeVNsL1s9U&t=206s)** very year when I decided to try that with that thing. Yeah, that's going back in time and these

**[03:32](https://youtube.com/watch?v=WjeVNsL1s9U&t=212s)** things were not, you know, they were not internet connected back then. They usually didn't even have an

**[03:38](https://youtube.com/watch?v=WjeVNsL1s9U&t=218s)** SD card slot. So usually these days, unless you have one of the newfangled ones that directly have

**[03:44](https://youtube.com/watch?v=WjeVNsL1s9U&t=224s)** a network connection built in, you take a USB stick or you take an SD card and put that into the

**[03:50](https://youtube.com/watch?v=WjeVNsL1s9U&t=230s)** printer and the printer will read what is on there and print that on its own. You will still have to

**[03:56](https://youtube.com/watch?v=WjeVNsL1s9U&t=236s)** keep an eye on things of course, but it at least will no longer tie up a PC necessarily. Back then,

**[04:01](https://youtube.com/watch?v=WjeVNsL1s9U&t=241s)** the add-on alone that would have allowed me to do that for my printer back then would have set

**[04:05](https://youtube.com/watch?v=WjeVNsL1s9U&t=245s)** me back 100 bucks and so I figured 35 for Raspberry Pi is, you know, less expensive and it gives

**[04:12](https://youtube.com/watch?v=WjeVNsL1s9U&t=252s)** me so much more. Back when the Raspberry Pi's were actually cheap and affordable, remember those days?

**[04:17](https://youtube.com/watch?v=WjeVNsL1s9U&t=257s)** Yeah, yeah, back then when. I should add that Octoprint does not only run on a Raspberry Pi, it runs

**[04:23](https://youtube.com/watch?v=WjeVNsL1s9U&t=263s)** basically everywhere where Pi's and runs so you don't have to use a Raspberry Pi, you can use

**[04:26](https://youtube.com/watch?v=WjeVNsL1s9U&t=266s)** an orange Pi or you can use an old laptop or whatever. It's an important distinction because I think

**[04:32](https://youtube.com/watch?v=WjeVNsL1s9U&t=272s)** over the years it's kind of got diluted by the Octopi project. I think certainly that's how I came

**[04:37](https://youtube.com/watch?v=WjeVNsL1s9U&t=277s)** across it in the first place. Yeah. So Octoprint is what? It's a collection of Python scripts.

**[04:43](https://youtube.com/watch?v=WjeVNsL1s9U&t=283s)** It's basically one giant Python script, I would say. It's a web server written in Python and the front

**[04:49](https://youtube.com/watch?v=WjeVNsL1s9U&t=289s)** and yeah, you're using the web technology from 11 years ago and a plug-in interface that also

**[04:58](https://youtube.com/watch?v=WjeVNsL1s9U&t=298s)** allows you to extend it in various directions. I think we currently have something like 350 plus

**[05:04](https://youtube.com/watch?v=WjeVNsL1s9U&t=304s)** plug-ins on the official plug-in repository and the plug-in repository is also why we still have a web

**[05:10](https://youtube.com/watch?v=WjeVNsL1s9U&t=310s)** technology connection stack from 10 years ago because of course plug-ins also bring along some front

**[05:17](https://youtube.com/watch?v=WjeVNsL1s9U&t=317s)** end parts and just swapping something out there means you render all of the old plug-ins

**[05:22](https://youtube.com/watch?v=WjeVNsL1s9U&t=322s)** obsolete. So there is a path of migration here that needs to be walked but that is still ongoing.

**[05:28](https://youtube.com/watch?v=WjeVNsL1s9U&t=328s)** So you've got the Windows or the x86 problem going on right there. You want to maintain the legacy

**[05:35](https://youtube.com/watch?v=WjeVNsL1s9U&t=335s)** but at the same time moving things forward in a decade web standards have moved on a little bit.

**[05:41](https://youtube.com/watch?v=WjeVNsL1s9U&t=341s)** I would argue that the plug-in architectures is what's made Octoprint have that longevity in the

**[05:46](https://youtube.com/watch?v=WjeVNsL1s9U&t=346s)** first place without being able to extend it like that. If I think about it, I want to

**[05:52](https://youtube.com/watch?v=WjeVNsL1s9U&t=352s)** for example have the lights around my printer change color via MQTT in Home Assistant

**[05:58](https://youtube.com/watch?v=WjeVNsL1s9U&t=358s)** and I can do all of these things thanks to different plug-ins that you haven't had to write.

**[06:03](https://youtube.com/watch?v=WjeVNsL1s9U&t=363s)** Yeah, the part with you haven't had to write was actually one of the most important things or the

**[06:09](https://youtube.com/watch?v=WjeVNsL1s9U&t=369s)** reasons why I created this the sole plug-in architecture because so I started working on that I think

**[06:15](https://youtube.com/watch?v=WjeVNsL1s9U&t=375s)** in 2014 or 2015 so that's also quite quite a while now and back then when I was the only

**[06:24](https://youtube.com/watch?v=WjeVNsL1s9U&t=384s)** maintainer I still am the only maintainer but I had a whole ton of people who were asking for

**[06:30](https://youtube.com/watch?v=WjeVNsL1s9U&t=390s)** the one or other very specific feature, very specific to the workflow or the hardware and such

**[06:36](https://youtube.com/watch?v=WjeVNsL1s9U&t=396s)** and I found myself more and more in this situation that while I could see why something was

**[06:42](https://youtube.com/watch?v=WjeVNsL1s9U&t=402s)** a good idea to have for certain people or with certain hardware I simply was not able to test it

**[06:49](https://youtube.com/watch?v=WjeVNsL1s9U&t=409s)** in any way and such not really able to maintain it and so I figured I should give people a way to do

**[06:58](https://youtube.com/watch?v=WjeVNsL1s9U&t=418s)** that themselves and yeah I mean plug-ins are just the prime solution for something like that.

**[07:04](https://youtube.com/watch?v=WjeVNsL1s9U&t=424s)** It is interesting when I listen to a lot of development podcasts and stuff particularly in the Apple

**[07:08](https://youtube.com/watch?v=WjeVNsL1s9U&t=428s)** ecosystem you hear people you know clamoring to buy you know this week has been the vision pro has

**[07:13](https://youtube.com/watch?v=WjeVNsL1s9U&t=433s)** been everywhere I think they need to buy these things to build their apps to test them and all

**[07:17](https://youtube.com/watch?v=WjeVNsL1s9U&t=437s)** this kind of stuff which you know hardware testing can be really difficult and this leads us nicely

**[07:23](https://youtube.com/watch?v=WjeVNsL1s9U&t=443s)** into the the meat of the conversation I think so you build your software using GitHub actions

**[07:30](https://youtube.com/watch?v=WjeVNsL1s9U&t=450s)** right which is a cloud hosted build environment. I wouldn't say that I necessarily build my software

**[07:36](https://youtube.com/watch?v=WjeVNsL1s9U&t=456s)** with that but I certainly use it a lot to test things I have a full-fledged test to that also

**[07:41](https://youtube.com/watch?v=WjeVNsL1s9U&t=461s)** involves and to end tests unit tests the whole bunch of stuff it also packages things up makes

**[07:48](https://youtube.com/watch?v=WjeVNsL1s9U&t=468s)** on releases takes things loads them up to pi pi and such but all in all yeah so I basically have

**[07:56](https://youtube.com/watch?v=WjeVNsL1s9U&t=476s)** this huge build workflow that runs on GitHub actions that makes takes care of a whole bunch of

**[08:05](https://youtube.com/watch?v=WjeVNsL1s9U&t=485s)** things of basically checking that everything up is all right that syntax is okay linting and

**[08:11](https://youtube.com/watch?v=WjeVNsL1s9U&t=491s)** and all of that and then finally pushes it out if it is a release and otherwise just says yes or no

**[08:19](https://youtube.com/watch?v=WjeVNsL1s9U&t=499s)** but yeah that is only octoprint I yeah prior to releases I have the challenge that I have to

**[08:29](https://youtube.com/watch?v=WjeVNsL1s9U&t=509s)** basically run through the whole update scenario of getting a base state of an earlier version

**[08:42](https://youtube.com/watch?v=WjeVNsL1s9U&t=522s)** on a specific python environment on a specific system environment and see if the update runs

**[08:49](https://youtube.com/watch?v=WjeVNsL1s9U&t=529s)** through flawlessly because in the past I made the experience that with certain stuff out in the

**[08:56](https://youtube.com/watch?v=WjeVNsL1s9U&t=536s)** field updates would fail even though they would work just fine here and I obviously want to avoid

**[09:02](https://youtube.com/watch?v=WjeVNsL1s9U&t=542s)** that from happening so I had to find some way to do that and this is where I yeah we're basically I

**[09:11](https://youtube.com/watch?v=WjeVNsL1s9U&t=551s)** I built myself a little test trick that consists of three Raspberry Pi 3s 3 yeah how could I say

**[09:20](https://youtube.com/watch?v=WjeVNsL1s9U&t=560s)** that how how should I call that I forgot how they think how how they are actually called by basically

**[09:26](https://youtube.com/watch?v=WjeVNsL1s9U&t=566s)** three little devices that pretend that they are an SD card unless via a USB SCSI command you tell

**[09:35](https://youtube.com/watch?v=WjeVNsL1s9U&t=575s)** them no you are no please going to be a USB storage and then you can flash that thing switch it back over

**[09:42](https://youtube.com/watch?v=WjeVNsL1s9U&t=582s)** into being in a SD card and that is what I use to remotely flash these three Raspberry Pi's in my

**[09:50](https://youtube.com/watch?v=WjeVNsL1s9U&t=590s)** test rig and and thus I'm able to to go through various test scenarios without having to constantly

**[09:59](https://youtube.com/watch?v=WjeVNsL1s9U&t=599s)** swap SD cards back and forth which is something that I did up until maybe 2021 and which was driving

**[10:05](https://youtube.com/watch?v=WjeVNsL1s9U&t=605s)** me absolutely insane on every single release hike and release candidate cycle like imagine going

**[10:11](https://youtube.com/watch?v=WjeVNsL1s9U&t=611s)** through something like eight to 10 test scenarios and for everyone you need to flash an SD card so

**[10:16](https://youtube.com/watch?v=WjeVNsL1s9U&t=616s)** you need to power down the Pi manually you need to unplug the Raspberry the SD card manually you

**[10:22](https://youtube.com/watch?v=WjeVNsL1s9U&t=622s)** need to plug it into a card reader you need to start up an image you need to wait until this

**[10:26](https://youtube.com/watch?v=WjeVNsL1s9U&t=626s)** image finishes then you have to do all of this in reverse and power the Pi back up wait until it's

**[10:31](https://youtube.com/watch?v=WjeVNsL1s9U&t=631s)** there now I just have a Python script that does all of this for me and that Python script runs in

**[10:37](https://youtube.com/watch?v=WjeVNsL1s9U&t=637s)** GitHub right and then it's actually so during the during the regular testing that still runs locally

**[10:44](https://youtube.com/watch?v=WjeVNsL1s9U&t=644s)** but I also have this this so I do manual manual steps here but once I have my my local tests all green

**[10:55](https://youtube.com/watch?v=WjeVNsL1s9U&t=655s)** for an update scenario what needs to be done is also a new new image build needs to happen so

**[11:02](https://youtube.com/watch?v=WjeVNsL1s9U&t=662s)** um you mentioned octopi that is currently the most common way to install octoprint even though as I

**[11:08](https://youtube.com/watch?v=WjeVNsL1s9U&t=668s)** mentioned not the only one but this is basically a pre-built Raspberry Pi image that has octopi on board

**[11:13](https://youtube.com/watch?v=WjeVNsL1s9U&t=673s)** a webcam streamer on board reverse proxy pre-configured and all of that so that you can just flash that and

**[11:21](https://youtube.com/watch?v=WjeVNsL1s9U&t=681s)** use the Raspberry Pi images configuration screen thingy to configure your Wi-Fi and then

**[11:27](https://youtube.com/watch?v=WjeVNsL1s9U&t=687s)** you're done basically and the thing is for a long while we had we we did an octopi release and then

**[11:37](https://youtube.com/watch?v=WjeVNsL1s9U&t=697s)** was that that was that then so that image never again was updated people were flashing octoprint

**[11:44](https://youtube.com/watch?v=WjeVNsL1s9U&t=704s)** versions from a half a year to a year or maybe more ago depending on when they pulled the image

**[11:49](https://youtube.com/watch?v=WjeVNsL1s9U&t=709s)** and then had to update and sometimes that would go wrong or something and basically they were

**[11:56](https://youtube.com/watch?v=WjeVNsL1s9U&t=716s)** installing stuff a new and it was outdated already so that was annoying and that was something that

**[12:01](https://youtube.com/watch?v=WjeVNsL1s9U&t=721s)** of course was also not that great from a from a security perspective and and such because

**[12:07](https://youtube.com/watch?v=WjeVNsL1s9U&t=727s)** would people actually update and and so so um at some point I created an update script that would

**[12:14](https://youtube.com/watch?v=WjeVNsL1s9U&t=734s)** take an octopi image and basically virtually booted um not really booted but like use a change route

**[12:23](https://youtube.com/watch?v=WjeVNsL1s9U&t=743s)** and go into it in a in a QE environment that would simulate the the architecture of the Raspberry Pi

**[12:30](https://youtube.com/watch?v=WjeVNsL1s9U&t=750s)** would update octoprint on it would also update update some some system images on it as system

**[12:36](https://youtube.com/watch?v=WjeVNsL1s9U&t=756s)** packages on it and and do some other fixes if needed and be done with it but of course

**[12:43](https://youtube.com/watch?v=WjeVNsL1s9U&t=763s)** whenever I wanted to release one of these images a new I would have to go through a whole

**[12:48](https://youtube.com/watch?v=WjeVNsL1s9U&t=768s)** gauntlet of testing again and so I now had this issue I had a full featured end-to-end test

**[12:56](https://youtube.com/watch?v=WjeVNsL1s9U&t=776s)** suit on one hand that uh ran on every single release on octoprint and I had this uh

**[13:05](https://youtube.com/watch?v=WjeVNsL1s9U&t=785s)** GitHub action-based image build that would update would would update an octopi image with the

**[13:11](https://youtube.com/watch?v=WjeVNsL1s9U&t=791s)** latest octoprint version and basically dumped myself an image uh on GitHub actions but that was

**[13:18](https://youtube.com/watch?v=WjeVNsL1s9U&t=798s)** untested which then had to manually load down update uh yeah flesh to to to one of the machines on

**[13:26](https://youtube.com/watch?v=WjeVNsL1s9U&t=806s)** the test rig manually click around look if everything was all right and at some point I just figured

**[13:31](https://youtube.com/watch?v=WjeVNsL1s9U&t=811s)** that there must be some way to automate that but of course there was the problem that this image

**[13:37](https://youtube.com/watch?v=WjeVNsL1s9U&t=817s)** triggered by every single release was created on GitHub actions so it was in the internet and the

**[13:45](https://youtube.com/watch?v=WjeVNsL1s9U&t=825s)** test rig is sitting like half a meter away from me right now on my desk I didn't want to put the

**[13:51](https://youtube.com/watch?v=WjeVNsL1s9U&t=831s)** test rig into the internet and I couldn't bring GitHub actions here on my desk so I needed to find a

**[13:58](https://youtube.com/watch?v=WjeVNsL1s9U&t=838s)** way to have each have have the two of each other talk to each other without me having to open up

**[14:04](https://youtube.com/watch?v=WjeVNsL1s9U&t=844s)** yeah holds in my file or whatever or anything like that and this is where I stumbled across

**[14:09](https://youtube.com/watch?v=WjeVNsL1s9U&t=849s)** scale so um what I'm doing now and quite successfully so though is imagine I prepare a new I

**[14:20](https://youtube.com/watch?v=WjeVNsL1s9U&t=860s)** prepare a new octoprint release uh the whole build suit runs through uh the unit tests are Katie

**[14:25](https://youtube.com/watch?v=WjeVNsL1s9U&t=865s)** and her and tests are okay the linter says everything is fine uh all my update tests before that we

**[14:31](https://youtube.com/watch?v=WjeVNsL1s9U&t=871s)** are also fine so and you release a stack upload to pipi uh everyone is happy what now happens is

**[14:39](https://youtube.com/watch?v=WjeVNsL1s9U&t=879s)** this this build uh this build will also now ping the image build the image build will now pull in

**[14:47](https://youtube.com/watch?v=WjeVNsL1s9U&t=887s)** the latest octoprint version create a new image based on that update everything else that needs updating

**[14:53](https://youtube.com/watch?v=WjeVNsL1s9U&t=893s)** and fixing everything that needs fixing and all that and in the end an image file falls out and that

**[14:58](https://youtube.com/watch?v=WjeVNsL1s9U&t=898s)** now will trigger another workflow that pulls in this so first of all that opens and opens a

**[15:05](https://youtube.com/watch?v=WjeVNsL1s9U&t=905s)** tailscale connection to an internal tailscale network in which the I call it the flesh holes so

**[15:10](https://youtube.com/watch?v=WjeVNsL1s9U&t=910s)** basically the the controller machine of the of the test rig uh has one node and the github runner

**[15:19](https://youtube.com/watch?v=WjeVNsL1s9U&t=919s)** is now another node and the github runner will know the flesh holes hey by the way please pull

**[15:24](https://youtube.com/watch?v=WjeVNsL1s9U&t=924s)** an image from this url flesh it to this machine that is the first step and once this flashing

**[15:30](https://youtube.com/watch?v=WjeVNsL1s9U&t=930s)** is run through the runner will know okay that worked great so the next step comes it pulls down

**[15:36](https://youtube.com/watch?v=WjeVNsL1s9U&t=936s)** the octoprint sources and runs the hole end-to-end test suit against the image so when that is green

**[15:43](https://youtube.com/watch?v=WjeVNsL1s9U&t=943s)** I know apparently nothing terribly broke here it's still booting it's still getting Wi-Fi it's

**[15:50](https://youtube.com/watch?v=WjeVNsL1s9U&t=950s)** still uh octoprint is still coming up I can even fetch a snapshot from the webcam for example the

**[15:56](https://youtube.com/watch?v=WjeVNsL1s9U&t=956s)** I also check if the error lock has any error either the the octoprint lock has any errors in it I

**[16:01](https://youtube.com/watch?v=WjeVNsL1s9U&t=961s)** check if the java script console has any errors in it and so I go the full 90 yards basically

**[16:08](https://youtube.com/watch?v=WjeVNsL1s9U&t=968s)** um from the software release to a ready-flash device on my desk and all of that completely automated

**[16:17](https://youtube.com/watch?v=WjeVNsL1s9U&t=977s)** through github actions like after the release something like two hours later or so I get a ping

**[16:23](https://youtube.com/watch?v=WjeVNsL1s9U&t=983s)** in my notifications from github like there is a release waiting for you to say yes push this out

**[16:29](https://youtube.com/watch?v=WjeVNsL1s9U&t=989s)** I don't necessarily need this additional step I just feel better having it in there um

**[16:36](https://youtube.com/watch?v=WjeVNsL1s9U&t=996s)** and so once I confirm that the image goes live and can be fleshed by anyone worldwide

**[16:42](https://youtube.com/watch?v=WjeVNsL1s9U&t=1002s)** that's fantastic that's a very there I say complicated workflow you've had to sort of refine

**[16:49](https://youtube.com/watch?v=WjeVNsL1s9U&t=1009s)** over the years there I mean before tail scale came along I suppose it wouldn't have been

**[16:55](https://youtube.com/watch?v=WjeVNsL1s9U&t=1015s)** terribly easy for you to to link the two together you might have had to build a manual wire guard

**[17:00](https://youtube.com/watch?v=WjeVNsL1s9U&t=1020s)** tunnel or do some weirdness with port forwarding in your firewall that kind of stuff

**[17:05](https://youtube.com/watch?v=WjeVNsL1s9U&t=1025s)** and now like what happens is the the get-have-runners basically got full access you know in terms of

**[17:11](https://youtube.com/watch?v=WjeVNsL1s9U&t=1031s)** networking to resources elsewhere on your town now wherever they are right limited access I have

**[17:17](https://youtube.com/watch?v=WjeVNsL1s9U&t=1037s)** a very strong ACL because I oh good good I'm glad to hear that like the only thing that this this

**[17:24](https://youtube.com/watch?v=WjeVNsL1s9U&t=1044s)** runner is allowed to access are some are is basically a web host and point on the flesh holes

**[17:32](https://youtube.com/watch?v=WjeVNsL1s9U&t=1052s)** which then triggers some local stuff to happen but yeah this is the whole idea I

**[17:39](https://youtube.com/watch?v=WjeVNsL1s9U&t=1059s)** my goal was to find somewhere where I still would feel safe in my own local network here where I

**[17:45](https://youtube.com/watch?v=WjeVNsL1s9U&t=1065s)** would not have to worry about anything getting compromised by I don't know someone breaking into

**[17:52](https://youtube.com/watch?v=WjeVNsL1s9U&t=1072s)** GitHub runners someone also someone breaking into tail scale so that was basically the idea here

**[17:59](https://youtube.com/watch?v=WjeVNsL1s9U&t=1079s)** being very very safe and secure but still allowing me to put these two parts on completely

**[18:04](https://youtube.com/watch?v=WjeVNsL1s9U&t=1084s)** different parts of the world together virtually so that I could automate the final thing that was

**[18:12](https://youtube.com/watch?v=WjeVNsL1s9U&t=1092s)** stopping me from having the whole process be completely independent of me flashing things carrying

**[18:18](https://youtube.com/watch?v=WjeVNsL1s9U&t=1098s)** SD cards around or clicking on buttons beyond yes launch this release you are going to have to give

**[18:25](https://youtube.com/watch?v=WjeVNsL1s9U&t=1105s)** me a link to that SD card emulator switcher device that you talked about that sounds like one of

**[18:30](https://youtube.com/watch?v=WjeVNsL1s9U&t=1110s)** the coolest things in the world I think it was called SD marks they are quiet expensive they are done

**[18:36](https://youtube.com/watch?v=WjeVNsL1s9U&t=1116s)** by a little company a little yeah not not that little but like mid-sized company here in Germany

**[18:44](https://youtube.com/watch?v=WjeVNsL1s9U&t=1124s)** and I have a blog post written up about how I created the whole test trick that does not yet have

**[18:50](https://youtube.com/watch?v=WjeVNsL1s9U&t=1130s)** the whole integration with GitHub action runners in it but it at least has the part where

**[18:56](https://youtube.com/watch?v=WjeVNsL1s9U&t=1136s)** it saved me two hours or more on every single release and really scan it so yeah so it's expensive

**[19:04](https://youtube.com/watch?v=WjeVNsL1s9U&t=1144s)** but your time isn't free either you know it that was the thought I started with two Raspberry

**[19:08](https://youtube.com/watch?v=WjeVNsL1s9U&t=1148s)** pies and that was already rather great and then when I added this integration with automatically

**[19:14](https://youtube.com/watch?v=WjeVNsL1s9U&t=1154s)** flashing the image I added a third one so that I could always know that at least one would be free

**[19:21](https://youtube.com/watch?v=WjeVNsL1s9U&t=1161s)** but I still have not in there is something like scheduling so that the flesh holes would automatically

**[19:25](https://youtube.com/watch?v=WjeVNsL1s9U&t=1165s)** know when a request to flash in your image comes in on which one to put that so that is still always

**[19:30](https://youtube.com/watch?v=WjeVNsL1s9U&t=1170s)** the third one but so far it doesn't it hasn't had the need to be utterly utterly fancy so

**[19:39](https://youtube.com/watch?v=WjeVNsL1s9U&t=1179s)** the fact you call it a flesh host just has me giggling every time I didn't know how else to call it

**[19:47](https://youtube.com/watch?v=WjeVNsL1s9U&t=1187s)** meat space box I don't know yeah flesh host yeah so I can I can I can shoot you the link to the

**[19:53](https://youtube.com/watch?v=WjeVNsL1s9U&t=1193s)** blog post it also has an image of the test rig and yeah with a fancy laser cut frame and all of that

**[20:00](https://youtube.com/watch?v=WjeVNsL1s9U&t=1200s)** so so fancy speaking of links and things like that there'll be a plethora of links down in the

**[20:07](https://youtube.com/watch?v=WjeVNsL1s9U&t=1207s)** description down below a link to a talk Gina gave it to Nova 2022 detailing a lot more of the

**[20:13](https://youtube.com/watch?v=WjeVNsL1s9U&t=1213s)** specifics behind this along with some of the octoprint project links and the blog and where you can

**[20:18](https://youtube.com/watch?v=WjeVNsL1s9U&t=1218s)** find Gina as well on the internet so thank you very much for joining us today it was an absolute

**[20:25](https://youtube.com/watch?v=WjeVNsL1s9U&t=1225s)** pleasure and I'm delighted to nerd out with somebody who's just you know found found the real world

**[20:30](https://youtube.com/watch?v=WjeVNsL1s9U&t=1230s)** problem and solved it using tail scale I also have to say that I giggle uncontrollably every single

**[20:36](https://youtube.com/watch?v=WjeVNsL1s9U&t=1236s)** time that I put her out of release these days because of the whole I mean just like I celebrate

**[20:41](https://youtube.com/watch?v=WjeVNsL1s9U&t=1241s)** how how well the test rig works and when I then get this little release is ready notification

**[20:47](https://youtube.com/watch?v=WjeVNsL1s9U&t=1247s)** from from from the guitar runners always like yes you know I'm still writing the release notes

**[20:53](https://youtube.com/watch?v=WjeVNsL1s9U&t=1253s)** or the announcements and cross-posting them everywhere and I can hear the fan on the flesh

**[20:57](https://youtube.com/watch?v=WjeVNsL1s9U&t=1257s)** hole spinning up because it just got the the the the command to flesh the the third pie and stuff

**[21:04](https://youtube.com/watch?v=WjeVNsL1s9U&t=1264s)** and it's like everything is just working automatically automation is great when it works when it

**[21:10](https://youtube.com/watch?v=WjeVNsL1s9U&t=1270s)** doesn't it's horrible but when it's when it works it's amazing also I have almost isn't running

**[21:15](https://youtube.com/watch?v=WjeVNsL1s9U&t=1275s)** here myself and I for the longest time I've had the components relying around here to build myself

**[21:22](https://youtube.com/watch?v=WjeVNsL1s9U&t=1282s)** like a little button box to really physically press the launch this button oh and you need

**[21:29](https://youtube.com/watch?v=WjeVNsL1s9U&t=1289s)** you're going to need like a missile control switch over the top of it yes something like that

**[21:33](https://youtube.com/watch?v=WjeVNsL1s9U&t=1293s)** accidentally yeah I still haven't done it but but that's that's like that's like also an idea that

**[21:39](https://youtube.com/watch?v=WjeVNsL1s9U&t=1299s)** I still have to just really have this this physical component to to creating a software release

**[21:44](https://youtube.com/watch?v=WjeVNsL1s9U&t=1304s)** of something of pushing a button and then it goes out yeah it's wonderful to say thank you very

**[21:48](https://youtube.com/watch?v=WjeVNsL1s9U&t=1308s)** much for joining us and we'll also probably connect again in the future on the cell-hosted podcast

**[21:53](https://youtube.com/watch?v=WjeVNsL1s9U&t=1313s)** to talk about some other things besides tail scale but on this channel of course that's what

**[21:58](https://youtube.com/watch?v=WjeVNsL1s9U&t=1318s)** we talk about most of the time so until next time I've been Alex from tail scale

---

*Automatically generated transcript. May contain errors.*
