---
video_id: "QHWNu_in0Zc"
title: "Put your gaming GPU to work! Remote machine learning on Windows with Docker and WSL2 from anywhere."
description: "In today's video we explore sharing an NVIDIA GPU from Windows 11, running a containerized workload with docker for windows, over Tailscale to connect Immich - a self-hosted photo library - to hardwar..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-04-24"
duration_seconds: 1092
youtube_url: "https://www.youtube.com/watch?v=QHWNu_in0Zc"
thumbnail_url: "https://i.ytimg.com/vi/QHWNu_in0Zc/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T15:57:26.162175"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 3456
transcription_time_seconds: 30.2
---

# Put your gaming GPU to work! Remote machine learning on Windows with Docker and WSL2 from anywhere.

**[00:00](https://youtube.com/watch?v=QHWNu_in0Zc&t=0s)** You know that gaming computer that sat in the corner, not doing a whole bunch during the day? Wouldn't it be fun if you could take the GPU from any computer and feed it into some kind of machine learning system? Well, in today's video, I'm going to show you how to use Image, a self-hosted Google photos clone, and connect it to practically any gaming rig that you have lying around, be that at your house, a friend's house, or whatever, using Tailscale. And we're going to do this on Windows.

**[00:30](https://youtube.com/watch?v=QHWNu_in0Zc&t=30s)** To do hardware accelerated GPU hardware accelerated workloads on top of Windows in a Docker container. As usual, all the resources for today's video will be linked in the description down below, so things like Docker Compose files, as well as reference to blog posts, that kind of thing. Also, if you've been watching the Tailscale channel for the last few months, you'll know that I've been covering a lot of Docker stuff lately. So things like sidecar proxy containers so that you can run individual services on your tail,

**[01:00](https://youtube.com/watch?v=QHWNu_in0Zc&t=60s)** and that all of that will be linked down below for you. So join me in today's video as we configure image to use a remote GPU for machine learning on Windows.

**[01:10](https://youtube.com/watch?v=QHWNu_in0Zc&t=70s)** For many years now, Google photos absolute killer feature has been its search. You store visual information in your mind, like pictures with keywords, and it's just natural that we do this as humans. So I think to myself, right, I want pictures of a red truck, for example.

**[01:27](https://youtube.com/watch?v=QHWNu_in0Zc&t=87s)** Search red truck and Google photos returns pictures of red trucks. Same thing might be true of a blue car, say something like that.

**[01:36](https://youtube.com/watch?v=QHWNu_in0Zc&t=96s)** Now with image and these new AI models that they've added to it through the open AI clip stuff that I'll show you in a second, you can now search your local photos with almost as much accuracy as we used to get through the proprietary Google photo service.

**[01:51](https://youtube.com/watch?v=QHWNu_in0Zc&t=111s)** Now this is my personal instance of image and I want to show you how to set this up from scratch today. So I have another instance here.

**[01:58](https://youtube.com/watch?v=QHWNu_in0Zc&t=118s)** This is running on my demo tailnet that I always use in these videos for a tail and scales at gmail.com. You can see that up here.

**[02:06](https://youtube.com/watch?v=QHWNu_in0Zc&t=126s)** Now, I only have one image loaded into this instance of image so that I can show you machine learning in action.

**[02:13](https://youtube.com/watch?v=QHWNu_in0Zc&t=133s)** First things we've got to do is just take a quick look at the machine learning settings in the image administration panel up here on the top right.

**[02:20](https://youtube.com/watch?v=QHWNu_in0Zc&t=140s)** Over here on the left under settings, there is a machine learning settings area.

**[02:25](https://youtube.com/watch?v=QHWNu_in0Zc&t=145s)** Now you can see out of the box, the URL that's here is actually expecting to find another container within the same docker network, presumably on the same host, where it can run all of its machine learning stuff.

**[02:38](https://youtube.com/watch?v=QHWNu_in0Zc&t=158s)** The machine learning is a very compute heavy task. I don't happen to have an Nvidia GPU to run the CUDA library underneath in my server but I do have an Nvidia GPU in my gaming system next door or maybe I know a friend with a gaming system and I could get them to share that with me over tail scale.

**[02:58](https://youtube.com/watch?v=QHWNu_in0Zc&t=178s)** So what we can do here is we can customize this URL to point to a tail scale node where the image machine learning container is running.

**[03:06](https://youtube.com/watch?v=QHWNu_in0Zc&t=186s)** Now, before we do that, I'm just going to jump very quickly into the smart search settings that are here.

**[03:10](https://youtube.com/watch?v=QHWNu_in0Zc&t=190s)** You can see the different models. There are a bunch of them listed here. I won't go through them in any amount of detail. You can see they're all listed on hugging face, which is a sort of directory of AI models that are available.

**[03:21](https://youtube.com/watch?v=QHWNu_in0Zc&t=201s)** And then underneath here, we've got the facial recognition model stuff in there, which is actually using Buffalo as a couple of different options too.

**[03:28](https://youtube.com/watch?v=QHWNu_in0Zc&t=208s)** Basically, the quality of the facial recognition and smart object search is defined by the quality of these models. So as time goes by, new models are released and things get better and improve.

**[03:41](https://youtube.com/watch?v=QHWNu_in0Zc&t=221s)** So one of the things that's really interesting about this whole solution is that we probably don't need a graphics card in our server full time to handle this workload.

**[03:51](https://youtube.com/watch?v=QHWNu_in0Zc&t=231s)** But under initial ingestion, where we're ingesting 100,000 photos, maybe that you've accumulated over the decades.

**[03:57](https://youtube.com/watch?v=QHWNu_in0Zc&t=237s)** Or you've just been on a big trip and you're adding a few thousand pictures that you took on Safari or wherever you've been.

**[04:03](https://youtube.com/watch?v=QHWNu_in0Zc&t=243s)** That's where you're going to want to run the object detection and really stress a graphics card, for example, that's perfect for a gaming rig that's mostly sat there doing nothing during the day.

**[04:12](https://youtube.com/watch?v=QHWNu_in0Zc&t=252s)** And you think, well, I'm going to put you to work for a few hours here, a few hours there. Now we're going to run this VIT B32 open AI model today.

**[04:19](https://youtube.com/watch?v=QHWNu_in0Zc&t=259s)** And we're going to do that using WSL 2 on Windows in Docker through remote desktop.

**[04:26](https://youtube.com/watch?v=QHWNu_in0Zc&t=266s)** There's a lot of layers going on here, but essentially all image needs is a URL to point at. So what we're going to give it is the tail scale IP of a node where the image machine learning container is available.

**[04:39](https://youtube.com/watch?v=QHWNu_in0Zc&t=279s)** Now if we jump into remote desktop over here, you can see I've prepared my gaming desktop, which is next door, but it's on a completely separate network.

**[04:47](https://youtube.com/watch?v=QHWNu_in0Zc&t=287s)** This laptop that you're looking at is in what's called a VLAN, a virtual local area network. And it's segregated from the network that this system is actually living on.

**[04:57](https://youtube.com/watch?v=QHWNu_in0Zc&t=297s)** That part's not important. I'm just wanted to show you that you can use tail scale to bridge the barriers between different networks and kind of connect things together.

**[05:07](https://youtube.com/watch?v=QHWNu_in0Zc&t=307s)** So theoretically, this graphics card could be in a completely different building and a completely different continent and you could connect to it over tail scale as if it was local.

**[05:17](https://youtube.com/watch?v=QHWNu_in0Zc&t=317s)** Now the first thing we need to do is go ahead and download and install Docker desktop for windows. I've already gone ahead and downloaded it and there's one very important thing I want to draw your attention to.

**[05:26](https://youtube.com/watch?v=QHWNu_in0Zc&t=326s)** This checkbox here where it says use WSL to WSL is windows subsystem for Linux. Possibly the worst name for any kind of subsystem there's ever been because basically it just let you run a Linux virtual machine on top of windows in the background.

**[05:44](https://youtube.com/watch?v=QHWNu_in0Zc&t=344s)** This is really useful for doing AI and machine learning accelerated workloads on windows. I used it for a long time just to actually have a usable development experience on windows in VS code.

**[05:56](https://youtube.com/watch?v=QHWNu_in0Zc&t=356s)** So go ahead and make sure that that WSL to checkbox is selected in the installer in the background is going to create a virtual machine where all of your containers will live on top of windows.

**[06:06](https://youtube.com/watch?v=QHWNu_in0Zc&t=366s)** And then it's going to make sure that all of the Docker command line stuff so you can actually do Docker run like you would on Linux in a windows power shell terminal environment works correctly.

**[06:17](https://youtube.com/watch?v=QHWNu_in0Zc&t=377s)** And most importantly for us, that means we can use Docker compose on top of windows.

**[06:22](https://youtube.com/watch?v=QHWNu_in0Zc&t=382s)** All right, and with the installation complete, we're going to open the windows terminal.

**[06:27](https://youtube.com/watch?v=QHWNu_in0Zc&t=387s)** This is the new fancy windows terminal you can get from the app store within windows.

**[06:32](https://youtube.com/watch?v=QHWNu_in0Zc&t=392s)** And what I want to do here is just type WSL dash dash list and just check that we have things here while we don't right now.

**[06:40](https://youtube.com/watch?v=QHWNu_in0Zc&t=400s)** So what we have to do is open up Docker desktop for windows. This is going to start the WSL to virtual machine in the background and largely speaking, most of this stuff, Docker desktop will take care of for you.

**[06:53](https://youtube.com/watch?v=QHWNu_in0Zc&t=413s)** Now I'm going to continue without signing in because I'm allergic to creating accounts unless I absolutely need to in the background, it's creating the virtual machines where all of the containers will live.

**[07:04](https://youtube.com/watch?v=QHWNu_in0Zc&t=424s)** And we can see right here that the Docker engine is running. So if we go back now to our windows terminal window, we can see that it's created a Linux distribution called Docker desktop in the background.

**[07:16](https://youtube.com/watch?v=QHWNu_in0Zc&t=436s)** So let's just do the quick Docker test, Docker run dash dash RM Hello world is going to pull down the Docker Hello world image and voila.

**[07:27](https://youtube.com/watch?v=QHWNu_in0Zc&t=447s)** We are running Docker on top of windows. Now the tricky part comes when we want to do things like GPU acceleration, typically with insider Docker container.

**[07:36](https://youtube.com/watch?v=QHWNu_in0Zc&t=456s)** So let's take a look at that using this utility GPU Z. I want to just show you this gaming rig has an RTX 3080 in it.

**[07:45](https://youtube.com/watch?v=QHWNu_in0Zc&t=465s)** It's important. It's a fairly recent and video GPU. So it supports the latest driver, as well as the latest CUDA libraries.

**[07:53](https://youtube.com/watch?v=QHWNu_in0Zc&t=473s)** The more RAM you can throw at these workloads, the better for things like Obama, for example, for AI, the more RAM, the better for things like image, I don't know if huge amounts of RAM are terribly useful.

**[08:07](https://youtube.com/watch?v=QHWNu_in0Zc&t=487s)** Obviously more the better, but we're doing lots of small operations here, rather than loading an entirely huge model into memory all at once.

**[08:16](https://youtube.com/watch?v=QHWNu_in0Zc&t=496s)** So there's a little command here. We can use just to check that the GPU situation is going to work correctly for us inside of our Docker environment. So I'm going to do Docker run dash IT GPUs all, and it's just going to do this benchmark right here is going to pull down a quick CUDA sample container and do a very quick benchmark of the 3080 GPU.

**[08:35](https://youtube.com/watch?v=QHWNu_in0Zc&t=515s)** And you can see it's got direct access to the GPU resources underneath. Well, fantastic.

**[08:41](https://youtube.com/watch?v=QHWNu_in0Zc&t=521s)** So next thing we want to do is take a quick look at our image machine learning container. This is the one that's going to actually do all of that image processing for us.

**[08:49](https://youtube.com/watch?v=QHWNu_in0Zc&t=529s)** Now under this line here, it's really important that you select release hyphen CUDA. That's an Nvidia specific image that's been built with the necessary Nvidia libraries inside of it.

**[09:01](https://youtube.com/watch?v=QHWNu_in0Zc&t=541s)** All the rest of it, I think you can largely leave alone this deploy section here is important that it's included to that gives the Docker container permission to access the underlying GPU resources on the host.

**[09:12](https://youtube.com/watch?v=QHWNu_in0Zc&t=552s)** Remember containers are aware of isolating things so you have to be very explicit when you're providing permissions.

**[09:18](https://youtube.com/watch?v=QHWNu_in0Zc&t=558s)** And then talking about being explicit, we need to make sure we've got the port here allocated as 3000 and three.

**[09:25](https://youtube.com/watch?v=QHWNu_in0Zc&t=565s)** The image project itself has pretty good documentation on the subject down here under guides on the left and then remote machine learning.

**[09:31](https://youtube.com/watch?v=QHWNu_in0Zc&t=571s)** You'll find everything that you need to know from the image project. Now this file lives in my documents directory.

**[09:36](https://youtube.com/watch?v=QHWNu_in0Zc&t=576s)** So I'm just going to literally do a Docker compose pull and it's going to pull down the machine learning container. It is I think three gig or so.

**[09:44](https://youtube.com/watch?v=QHWNu_in0Zc&t=584s)** So it will take a moment to download an unpack it. Right. And once that's downloaded, I'm going to go ahead and just do a Docker compose up.

**[09:52](https://youtube.com/watch?v=QHWNu_in0Zc&t=592s)** I'm not going to run it in the background. If you wanted to run this permanently in the background on this machine, you do a hyphen D to put it in the background for demon mode.

**[10:00](https://youtube.com/watch?v=QHWNu_in0Zc&t=600s)** I'm just going to leave this in the foreground by taking that off and it's going to run the machine learning container on this host.

**[10:06](https://youtube.com/watch?v=QHWNu_in0Zc&t=606s)** Now this host has an IP of 10. What is it 10.42.7.221. I don't have access to that IP address from where image is running.

**[10:17](https://youtube.com/watch?v=QHWNu_in0Zc&t=617s)** But I do have tail scale installed on this machine. You can see down here. This is connected to my personal tail net on Alex KTZ.

**[10:25](https://youtube.com/watch?v=QHWNu_in0Zc&t=625s)** So what I want to do is go ahead and go to my tail scale admin dashboard and share this node with the tail net that image is actually running on.

**[10:33](https://youtube.com/watch?v=QHWNu_in0Zc&t=633s)** So if I jump back over here and go to my machines page for my personal tail net and go to I want to search for win 11.

**[10:42](https://youtube.com/watch?v=QHWNu_in0Zc&t=642s)** I think, yep, here we go. And then click on the share button over here on the right.

**[10:47](https://youtube.com/watch?v=QHWNu_in0Zc&t=647s)** I'm going to get a share link and I'm going to do copy share link just here. Click copy share link and then change into my other browser session.

**[10:56](https://youtube.com/watch?v=QHWNu_in0Zc&t=656s)** I know there's a lot of browser sessions going on. It's just the nature of doing these demos sometimes.

**[11:00](https://youtube.com/watch?v=QHWNu_in0Zc&t=660s)** This one is where the tail and scales at Gmail tail net lives. That's the one I use for all of these demos.

**[11:06](https://youtube.com/watch?v=QHWNu_in0Zc&t=666s)** Now if I go ahead and paste this link into that particular browser session is going to say that Alex wants to share a device with you.

**[11:13](https://youtube.com/watch?v=QHWNu_in0Zc&t=673s)** This is the Windows 11 gaming rig. I'm going to go ahead and accept that invite. And you can see that this machine is now added to a tail and scales tail net as a shared in device.

**[11:25](https://youtube.com/watch?v=QHWNu_in0Zc&t=685s)** That means I can go and copy this IP address. Go to my terminal, for example, let me just drag this in from over here.

**[11:32](https://youtube.com/watch?v=QHWNu_in0Zc&t=692s)** And I can now ping this IP address. So I now have access to that container that's running on a completely separate network.

**[11:41](https://youtube.com/watch?v=QHWNu_in0Zc&t=701s)** Now I need to plug this IP address into my image machine learning settings. So let's go ahead and just replace this with the correct IP address.

**[11:50](https://youtube.com/watch?v=QHWNu_in0Zc&t=710s)** You could, by the way, I always get folks saying to me, do I have to use the IP address? No, you don't.

**[11:55](https://youtube.com/watch?v=QHWNu_in0Zc&t=715s)** But when a node is shared in, you must use the fully qualified domain name of that tail net. For example, here is ktz.ts.net.

**[12:03](https://youtube.com/watch?v=QHWNu_in0Zc&t=723s)** For example, now if I go ahead and where was it, image is over here. See sometimes even I get confused.

**[12:11](https://youtube.com/watch?v=QHWNu_in0Zc&t=731s)** I've put in the IP address just to keep things simple for now. I'm going to click save.

**[12:16](https://youtube.com/watch?v=QHWNu_in0Zc&t=736s)** And in the background, I actually have the compose running over here.

**[12:21](https://youtube.com/watch?v=QHWNu_in0Zc&t=741s)** You can see there was a few things happened with magic soft and tail scale discovery in the background to actually connect those devices together.

**[12:27](https://youtube.com/watch?v=QHWNu_in0Zc&t=747s)** So now I'm going to try and arrange these windows in such a way that you can see everything that's going on all at once.

**[12:33](https://youtube.com/watch?v=QHWNu_in0Zc&t=753s)** Let me get rid of this one in the background. Remember, we have windows running through remote desktop.

**[12:40](https://youtube.com/watch?v=QHWNu_in0Zc&t=760s)** But that bit's not important. You could just just as well be set at the physical console of the machine.

**[12:45](https://youtube.com/watch?v=QHWNu_in0Zc&t=765s)** I'm just using remote desktop. So it's all in one place. So it's easier for this video.

**[12:49](https://youtube.com/watch?v=QHWNu_in0Zc&t=769s)** Now, we can see that we've got the image machine learning container running in Docker on the windows host back down here on the left.

**[12:56](https://youtube.com/watch?v=QHWNu_in0Zc&t=776s)** You can see the utilization of the graphics card currently is 1%, basically zero.

**[13:02](https://youtube.com/watch?v=QHWNu_in0Zc&t=782s)** And then over here, I've saved that into image. Now if I go into administration and under jobs.

**[13:08](https://youtube.com/watch?v=QHWNu_in0Zc&t=788s)** If I run, for example, smart search, it's going to now go into the machine learning container that's running on windows in another location.

**[13:18](https://youtube.com/watch?v=QHWNu_in0Zc&t=798s)** Remember and go ahead and download that open AI model to do the image detection.

**[13:23](https://youtube.com/watch?v=QHWNu_in0Zc&t=803s)** This can take a little while and if you have a slow internet connection, you might find you need to tweak the timeouts for the image download permission.

**[13:31](https://youtube.com/watch?v=QHWNu_in0Zc&t=811s)** Luckily, I've got gigabit down. So it's not a problem here. Now, I think I spoke a little bit too soon.

**[13:37](https://youtube.com/watch?v=QHWNu_in0Zc&t=817s)** Just their hugging face, which is the repository that hosts all of these machine learning models.

**[13:43](https://youtube.com/watch?v=QHWNu_in0Zc&t=823s)** I've been having downtime this afternoon. Luckily, the other image instance that I'm running on my personal box.

**[13:50](https://youtube.com/watch?v=QHWNu_in0Zc&t=830s)** I was able to copy the models out of there and put them into the demo environment. So we're all good.

**[13:56](https://youtube.com/watch?v=QHWNu_in0Zc&t=836s)** Now I did run into a couple of other things that didn't even occur to me until I was making this video.

**[14:01](https://youtube.com/watch?v=QHWNu_in0Zc&t=841s)** I want to share them with you because they're really quite important in making this solution work.

**[14:06](https://youtube.com/watch?v=QHWNu_in0Zc&t=846s)** So you can see here we've got a couple of nodes. We've got the windows 11 gaming rig that shared into the tail net.

**[14:12](https://youtube.com/watch?v=QHWNu_in0Zc&t=852s)** That's owned by Alex KTZ. So the owner of that node is my personal tail net.

**[14:19](https://youtube.com/watch?v=QHWNu_in0Zc&t=859s)** Now I did have image owned by a tag. So I was using the OAuth secret rather than the auth key,

**[14:27](https://youtube.com/watch?v=QHWNu_in0Zc&t=867s)** which meant that the container was being owned by the tag container tag owner. It's a little bit confusing, but that's the way it works.

**[14:36](https://youtube.com/watch?v=QHWNu_in0Zc&t=876s)** And then what that meant was that the image container couldn't actually see the shared in node because you can only view a shared node in the receiving tail net.

**[14:48](https://youtube.com/watch?v=QHWNu_in0Zc&t=888s)** If you are the user that received that invite. So that basically means if you are the user tag container, you can't see the windows 11 gaming rig.

**[15:00](https://youtube.com/watch?v=QHWNu_in0Zc&t=900s)** Using an OAuth client secret as I detail in this contain yourself blog post using an OAuth secret here to authenticate your container.

**[15:11](https://youtube.com/watch?v=QHWNu_in0Zc&t=911s)** You must use a tag as the only option available to you. However, if you use an auth key, you don't have to use a tag.

**[15:19](https://youtube.com/watch?v=QHWNu_in0Zc&t=919s)** I just wasted half an hour and I do this every day. So there's a little gotcha and hopefully you won't run into that one.

**[15:28](https://youtube.com/watch?v=QHWNu_in0Zc&t=928s)** Now back on the image side of things what I want to do here is just prove to you that this actually works.

**[15:34](https://youtube.com/watch?v=QHWNu_in0Zc&t=934s)** I'm using the gaming GPU that sat in my desktop on the other side of the house over tail scale between different VLANs.

**[15:43](https://youtube.com/watch?v=QHWNu_in0Zc&t=943s)** Everything is not able to talk to each other unless all of this is set up correctly. So if I go to this upload button here, I've got a few pictures pre-staged 61 pictures.

**[15:53](https://youtube.com/watch?v=QHWNu_in0Zc&t=953s)** And as they are ingested by image, you'll see in the background over here on the left that CUDA is doing its thing.

**[15:59](https://youtube.com/watch?v=QHWNu_in0Zc&t=959s)** It's loading in the Buffalo model for face detection. And then it'll do the open AI, VIT B model for everything else.

**[16:06](https://youtube.com/watch?v=QHWNu_in0Zc&t=966s)** And you can see the utilization of the GPU is spiking just here. And so what this proves to us is that the GPU in the gaming rig is being connected to from image, which is in a totally different place.

**[16:20](https://youtube.com/watch?v=QHWNu_in0Zc&t=980s)** Now if you want to verify that the machine learning has been doing its thing in the background, it already did. We already saw it, but just in case you want to change models or verify things are actually working as you hope.

**[16:31](https://youtube.com/watch?v=QHWNu_in0Zc&t=991s)** You can go into the jobs section over here under the administration tabs, jobs. And then you can force image to run the machine learning on all of these images.

**[16:40](https://youtube.com/watch?v=QHWNu_in0Zc&t=1000s)** So for example, if I click on all here, you see it goes through and it reacts the job, the GPU spikes, and it does its thing.

**[16:46](https://youtube.com/watch?v=QHWNu_in0Zc&t=1006s)** Now if I want to go and just do a search, for example, let's search for bison, because there are some yellowstone pictures here.

**[16:52](https://youtube.com/watch?v=QHWNu_in0Zc&t=1012s)** You can see it's not perfect, but there are only a few handful of pictures here to go through.

**[16:57](https://youtube.com/watch?v=QHWNu_in0Zc&t=1017s)** If you have an entire 100,000 image library text search like this using the object detection is the only way to go.

**[17:06](https://youtube.com/watch?v=QHWNu_in0Zc&t=1026s)** So let's recap what we've done here. We have connected a gaming desktop running windows and Docker desktop for windows with WSL2 underneath.

**[17:15](https://youtube.com/watch?v=QHWNu_in0Zc&t=1035s)** So lots of layers there, but we've got a physical 3080 in video 3080 GPU connected to WSL2 connected to Docker desktop connected to tail scale on that node.

**[17:31](https://youtube.com/watch?v=QHWNu_in0Zc&t=1051s)** Tail scale then talks back to image or well technically image in a completely different location or low power system talks back to the gaming rig does all the machine learning stuff and then passes that back to the main image server.

**[17:45](https://youtube.com/watch?v=QHWNu_in0Zc&t=1065s)** And in this way, you're able to avoid sticking a GPU into your server full time and just use it occasionally when you need to.

**[17:54](https://youtube.com/watch?v=QHWNu_in0Zc&t=1074s)** You don't have to leave the Docker running 100% of the time all that will happen on the image side is that those machine learning jobs will fail until the GPU becomes available next time.

**[18:05](https://youtube.com/watch?v=QHWNu_in0Zc&t=1085s)** And so as usual, I hope you found some utility in today's video. Thank you so much for watching. I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
