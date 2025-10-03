---
video_id: "YTjYXii4WzI"
title: "Get started with Docker and Tailscale"
description: "In today's video, Alex walks you through the basics of installing docker and connecting your first container to Tailscale. He also covers the built-in functionality that generates automated TLS certif..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-07-22"
duration_seconds: 844
youtube_url: "https://www.youtube.com/watch?v=YTjYXii4WzI"
thumbnail_url: "https://i.ytimg.com/vi_webp/YTjYXii4WzI/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T18:07:41.511985"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2688
transcription_time_seconds: 26.1
---

# Get started with Docker and Tailscale

**[00:00](https://youtube.com/watch?v=YTjYXii4WzI&t=0s)** Hello internet, it's Alex from Tailscale here. Now back in the spring, we released a deep dive on container networking with Docker and Tailscale, and we covered every corner of that topic in excruciating detail. But in today's Docker Quick Start video, I wanted to give you just the basics, the things that you need to know to get off the ground as quickly as possible. If you'd like to dive deeper on any of the topics we cover today, the full length video and deep dive blog post from the spring will be linked down below.

**[00:30](https://youtube.com/watch?v=YTjYXii4WzI&t=30s)** So this is the way to connect your devices and services together, wherever they are. And I want to help you today get your containers directly onto your townnet, our name for a Tailscale network of devices.

**[00:39](https://youtube.com/watch?v=YTjYXii4WzI&t=39s)** That's so that they become available to you anywhere regardless of the network topology between you and them. Take your existing containers and throw up a tailscale sidecar proxy for each and boom, you can now access these services via Tailscale from anywhere.

**[00:55](https://youtube.com/watch?v=YTjYXii4WzI&t=55s)** anywhere. So I have here a completely fresh install of a Ubuntu

**[01:00](https://youtube.com/watch?v=YTjYXii4WzI&t=60s)** server. It doesn't have Docker. It doesn't have tail scale. So we're

**[01:04](https://youtube.com/watch?v=YTjYXii4WzI&t=64s)** going to need to set up a couple of things just to make our lives

**[01:07](https://youtube.com/watch?v=YTjYXii4WzI&t=67s)** easier and actually be able to run some applications. So first

**[01:10](https://youtube.com/watch?v=YTjYXii4WzI&t=70s)** thing we're going to do is install Docker. I like to do this

**[01:13](https://youtube.com/watch?v=YTjYXii4WzI&t=73s)** using the get.docker.com script. So if we look down here, there

**[01:17](https://youtube.com/watch?v=YTjYXii4WzI&t=77s)** is a line under step one called download the script. So I'm

**[01:22](https://youtube.com/watch?v=YTjYXii4WzI&t=82s)** going to paste this into my terminal on my Ubuntu VM. Then

**[01:25](https://youtube.com/watch?v=YTjYXii4WzI&t=85s)** we're going to very quickly just verify this looks about right.

**[01:29](https://youtube.com/watch?v=YTjYXii4WzI&t=89s)** You can see that this pretty much matches what exactly matches

**[01:32](https://youtube.com/watch?v=YTjYXii4WzI&t=92s)** what we've seen on get.docker.com. So that's good. I'm now

**[01:36](https://youtube.com/watch?v=YTjYXii4WzI&t=96s)** going to do a pseudo SH install Docker.sh. It's going to ask me

**[01:40](https://youtube.com/watch?v=YTjYXii4WzI&t=100s)** for my pseudo password. And now it's going to go ahead and install

**[01:44](https://youtube.com/watch?v=YTjYXii4WzI&t=104s)** Docker. It only takes a minute or so. And then once that's

**[01:47](https://youtube.com/watch?v=YTjYXii4WzI&t=107s)** done, we want to just modify the user group that z4d our Linux

**[01:52](https://youtube.com/watch?v=YTjYXii4WzI&t=112s)** user is part of with z4d and docker. No, I always get the

**[01:57](https://youtube.com/watch?v=YTjYXii4WzI&t=117s)** wrong way around always every time. Okay, use a mod and then

**[02:00](https://youtube.com/watch?v=YTjYXii4WzI&t=120s)** docker z4d and then going to need to log out and then in

**[02:03](https://youtube.com/watch?v=YTjYXii4WzI&t=123s)** again, so that the Linux grouping system picks up those

**[02:08](https://youtube.com/watch?v=YTjYXii4WzI&t=128s)** changes. I can now do a docker run dash dash RM hello world

**[02:12](https://youtube.com/watch?v=YTjYXii4WzI&t=132s)** just to verify that the docker engine is installed all

**[02:14](https://youtube.com/watch?v=YTjYXii4WzI&t=134s)** correctly. Excellent. Let's move on to the next step, which

**[02:18](https://youtube.com/watch?v=YTjYXii4WzI&t=138s)** is creating our first tail scale container. Note that we

**[02:21](https://youtube.com/watch?v=YTjYXii4WzI&t=141s)** still don't have tail scale installed on the host. And that's

**[02:24](https://youtube.com/watch?v=YTjYXii4WzI&t=144s)** by design for right now. Anyway, I mean, you could install

**[02:26](https://youtube.com/watch?v=YTjYXii4WzI&t=146s)** tail scale on the host and have it in the container as well.

**[02:29](https://youtube.com/watch?v=YTjYXii4WzI&t=149s)** If you'd like to, but let's not over complicate things right

**[02:32](https://youtube.com/watch?v=YTjYXii4WzI&t=152s)** now. Let's just create a docker compose YAML file. I'm going

**[02:36](https://youtube.com/watch?v=YTjYXii4WzI&t=156s)** to use them for this, but you could just as well use nano or any

**[02:39](https://youtube.com/watch?v=YTjYXii4WzI&t=159s)** other text editor that you would prefer. Now, we're going to

**[02:42](https://youtube.com/watch?v=YTjYXii4WzI&t=162s)** copy and paste some code. This is all linked in a repo down in

**[02:46](https://youtube.com/watch?v=YTjYXii4WzI&t=166s)** the description with some sample code for you. And you can see

**[02:50](https://youtube.com/watch?v=YTjYXii4WzI&t=170s)** here that I've got a couple of containers. We've got first

**[02:53](https://youtube.com/watch?v=YTjYXii4WzI&t=173s)** of all, we've got a tail scale container. This, these few

**[02:57](https://youtube.com/watch?v=YTjYXii4WzI&t=177s)** lines here are the official tail scale docker image that

**[03:00](https://youtube.com/watch?v=YTjYXii4WzI&t=180s)** we publish. We're going to need to make some very minor tweaks

**[03:04](https://youtube.com/watch?v=YTjYXii4WzI&t=184s)** just to put this all together. You can see here I've got an

**[03:06](https://youtube.com/watch?v=YTjYXii4WzI&t=186s)** auth key. This is essentially like a password. And this is

**[03:09](https://youtube.com/watch?v=YTjYXii4WzI&t=189s)** what allows this container to connect to my tail net, well,

**[03:13](https://youtube.com/watch?v=YTjYXii4WzI&t=193s)** your, your tail net, by suppose. And where do we get this from?

**[03:16](https://youtube.com/watch?v=YTjYXii4WzI&t=196s)** Well, we can go to the tail scale admin dashboard.

**[03:19](https://youtube.com/watch?v=YTjYXii4WzI&t=199s)** You'll look like this. You'll probably log in and land on the

**[03:22](https://youtube.com/watch?v=YTjYXii4WzI&t=202s)** machine's page. Along the top menu up here, look under settings

**[03:27](https://youtube.com/watch?v=YTjYXii4WzI&t=207s)** and then go to keys on the left hand side. Click on generate

**[03:30](https://youtube.com/watch?v=YTjYXii4WzI&t=210s)** auth key and course, whatever you like. I'm going to call mine

**[03:33](https://youtube.com/watch?v=YTjYXii4WzI&t=213s)** banana. I'm going to leave these all alone except for reusable

**[03:37](https://youtube.com/watch?v=YTjYXii4WzI&t=217s)** just because we're doing a demo right now. What you choose to do

**[03:40](https://youtube.com/watch?v=YTjYXii4WzI&t=220s)** this up to you generate key copy that to my clipboard. And then

**[03:46](https://youtube.com/watch?v=YTjYXii4WzI&t=226s)** I'm going to modify this line here with a C and then a dollar

**[03:49](https://youtube.com/watch?v=YTjYXii4WzI&t=229s)** sign to do a change until end of line with them. And then I'm

**[03:55](https://youtube.com/watch?v=YTjYXii4WzI&t=235s)** just going to write that change with a colon W. I need to make

**[03:59](https://youtube.com/watch?v=YTjYXii4WzI&t=239s)** one more change just down here. I've just spotted a small

**[04:01](https://youtube.com/watch?v=YTjYXii4WzI&t=241s)** mistake. So under service, this must match the name of the

**[04:05](https://youtube.com/watch?v=YTjYXii4WzI&t=245s)** service that you want to proxy through the tail scale container.

**[04:09](https://youtube.com/watch?v=YTjYXii4WzI&t=249s)** So in my case, you can see that this is the service name up here,

**[04:13](https://youtube.com/watch?v=YTjYXii4WzI&t=253s)** tail scale, auth key one, this must match this name here must

**[04:18](https://youtube.com/watch?v=YTjYXii4WzI&t=258s)** match the name of the service that you want to proxy. Okay, so

**[04:21](https://youtube.com/watch?v=YTjYXii4WzI&t=261s)** what this is going to do is going to make engine X, which is a

**[04:24](https://youtube.com/watch?v=YTjYXii4WzI&t=264s)** web server available on your tail net on port 80. Also note the

**[04:30](https://youtube.com/watch?v=YTjYXii4WzI&t=270s)** host name I've set here of banana. We just went to watch the

**[04:33](https://youtube.com/watch?v=YTjYXii4WzI&t=273s)** minions movie. So bananas are on the brain, I suppose. And what I

**[04:38](https://youtube.com/watch?v=YTjYXii4WzI&t=278s)** want this to do is put a engine X container on my tail net with

**[04:42](https://youtube.com/watch?v=YTjYXii4WzI&t=282s)** the host name of banana. Now we should be good to go here.

**[04:45](https://youtube.com/watch?v=YTjYXii4WzI&t=285s)** So let's do a right quit and then do a docker compose up minus

**[04:50](https://youtube.com/watch?v=YTjYXii4WzI&t=290s)** D. And it's going to pull all of these containers in the

**[04:52](https://youtube.com/watch?v=YTjYXii4WzI&t=292s)** background. I say all two containers in the background. And we

**[04:57](https://youtube.com/watch?v=YTjYXii4WzI&t=297s)** should now be able to go to our admin console under the

**[05:00](https://youtube.com/watch?v=YTjYXii4WzI&t=300s)** machines page and see that we have banana. There we go. So I'm

**[05:04](https://youtube.com/watch?v=YTjYXii4WzI&t=304s)** going to do HTTP colon banana and voila. We've just added a

**[05:09](https://youtube.com/watch?v=YTjYXii4WzI&t=309s)** banana to our tail net. So now the question becomes what do we

**[05:13](https://youtube.com/watch?v=YTjYXii4WzI&t=313s)** do when we want to have a second or a third or a fourth

**[05:16](https://youtube.com/watch?v=YTjYXii4WzI&t=316s)** application? Well, let's dig into that. So let's deploy a

**[05:20](https://youtube.com/watch?v=YTjYXii4WzI&t=320s)** second application. I'm just going to deploy this alongside

**[05:22](https://youtube.com/watch?v=YTjYXii4WzI&t=322s)** the engine X container. We just deployed. Remember, there are

**[05:26](https://youtube.com/watch?v=YTjYXii4WzI&t=326s)** code snippets in the description down below for you. Now you

**[05:29](https://youtube.com/watch?v=YTjYXii4WzI&t=329s)** need to group all of the volumes for your various containers

**[05:32](https://youtube.com/watch?v=YTjYXii4WzI&t=332s)** together at the bottom of a docker compose file. I'm going to need

**[05:35](https://youtube.com/watch?v=YTjYXii4WzI&t=335s)** three different volumes for this specific deployment. So I've

**[05:38](https://youtube.com/watch?v=YTjYXii4WzI&t=338s)** got one for the tail scale container to persist the state of

**[05:41](https://youtube.com/watch?v=YTjYXii4WzI&t=341s)** the container itself. Then I've got two here for the sterling

**[05:45](https://youtube.com/watch?v=YTjYXii4WzI&t=345s)** PDF container. Now sterling PDF, by the way, is an awesome

**[05:48](https://youtube.com/watch?v=YTjYXii4WzI&t=348s)** self hosted PDF Swiss Army knife toolkit thing. If you've ever

**[05:54](https://youtube.com/watch?v=YTjYXii4WzI&t=354s)** had to use Adobe Acrobat for anything like converting a

**[05:56](https://youtube.com/watch?v=YTjYXii4WzI&t=356s)** PDF, merging them, signing them, sterling PDF can do it, and you

**[06:01](https://youtube.com/watch?v=YTjYXii4WzI&t=361s)** can host this as a self hosted app on your tail net. Now, I'm

**[06:04](https://youtube.com/watch?v=YTjYXii4WzI&t=364s)** just going to copy and paste the relevant part into my docker

**[06:06](https://youtube.com/watch?v=YTjYXii4WzI&t=366s)** compose file. So let's just put in these lines here and just

**[06:12](https://youtube.com/watch?v=YTjYXii4WzI&t=372s)** walk you through what's going on. Now if I scroll up a little

**[06:15](https://youtube.com/watch?v=YTjYXii4WzI&t=375s)** bit, you can see, first of all, we've got the sterling TS

**[06:19](https://youtube.com/watch?v=YTjYXii4WzI&t=379s)** container. This is the tail scale container. This is the one

**[06:21](https://youtube.com/watch?v=YTjYXii4WzI&t=381s)** that actually does the heavy lifting and connects to your

**[06:23](https://youtube.com/watch?v=YTjYXii4WzI&t=383s)** tail net. Next up, we've got the image name for tail scale

**[06:27](https://youtube.com/watch?v=YTjYXii4WzI&t=387s)** slash tail scale. And the container name is sterling

**[06:30](https://youtube.com/watch?v=YTjYXii4WzI&t=390s)** hyphen, TS. Now my host name is PDF. As you remember from

**[06:34](https://youtube.com/watch?v=YTjYXii4WzI&t=394s)** above, banana is the name we gave to the engine X container,

**[06:37](https://youtube.com/watch?v=YTjYXii4WzI&t=397s)** PDF is the name this node will appear with on my tail net. Next

**[06:42](https://youtube.com/watch?v=YTjYXii4WzI&t=402s)** up, we've got a few environment variables, things like the

**[06:44](https://youtube.com/watch?v=YTjYXii4WzI&t=404s)** TS O or client secret, we generate this in much the same way as

**[06:49](https://youtube.com/watch?v=YTjYXii4WzI&t=409s)** we would do the auth key. So we go to our machines page over on

**[06:52](https://youtube.com/watch?v=YTjYXii4WzI&t=412s)** tail scale.com settings, go to O or clients, and then

**[06:56](https://youtube.com/watch?v=YTjYXii4WzI&t=416s)** generate OAuth clients. I'm just going to call this one PDF,

**[07:00](https://youtube.com/watch?v=YTjYXii4WzI&t=420s)** the name's not important. And then under devices, all we need

**[07:03](https://youtube.com/watch?v=YTjYXii4WzI&t=423s)** to give it is the right scope. This is particularly useful if

**[07:06](https://youtube.com/watch?v=YTjYXii4WzI&t=426s)** you have auditors in your life because they love things to be

**[07:09](https://youtube.com/watch?v=YTjYXii4WzI&t=429s)** scoped tokens. And then we need to give it a tag of container.

**[07:14](https://youtube.com/watch?v=YTjYXii4WzI&t=434s)** Once we've done that, click on generate client, copy the client

**[07:17](https://youtube.com/watch?v=YTjYXii4WzI&t=437s)** secret and put that into your configuration file with a CT

**[07:24](https://youtube.com/watch?v=YTjYXii4WzI&t=444s)** question mark, change to a question mark in them at least.

**[07:28](https://youtube.com/watch?v=YTjYXii4WzI&t=448s)** If you don't have a tag set up in your ACLs already, you'll

**[07:32](https://youtube.com/watch?v=YTjYXii4WzI&t=452s)** need to first go over to access controls and add this line here,

**[07:36](https://youtube.com/watch?v=YTjYXii4WzI&t=456s)** tag, colon container with an auto group of admin or whatever

**[07:41](https://youtube.com/watch?v=YTjYXii4WzI&t=461s)** groupings you feel most comfortable with. There is quite a lot

**[07:45](https://youtube.com/watch?v=YTjYXii4WzI&t=465s)** of nuance between the auth key and the OAuth client, check out

**[07:49](https://youtube.com/watch?v=YTjYXii4WzI&t=469s)** the long form Docker video. There's chapter markers in that

**[07:52](https://youtube.com/watch?v=YTjYXii4WzI&t=472s)** big video, if you want the full details and of the differences

**[07:55](https://youtube.com/watch?v=YTjYXii4WzI&t=475s)** between those two authentication methods. For right now, we

**[07:59](https://youtube.com/watch?v=YTjYXii4WzI&t=479s)** should be good to go in terms of connecting this to our tailnet.

**[08:02](https://youtube.com/watch?v=YTjYXii4WzI&t=482s)** We need to just add another line here of TS extra args. This

**[08:06](https://youtube.com/watch?v=YTjYXii4WzI&t=486s)** one advertises the tag container. So this is how tail scale

**[08:11](https://youtube.com/watch?v=YTjYXii4WzI&t=491s)** knows which tag to request to authenticate as we then need to

**[08:15](https://youtube.com/watch?v=YTjYXii4WzI&t=495s)** make sure that our state is persisted in value of tail scale.

**[08:18](https://youtube.com/watch?v=YTjYXii4WzI&t=498s)** So there must be a Docker volume created or defined for this

**[08:22](https://youtube.com/watch?v=YTjYXii4WzI&t=502s)** value. And then these three or four lines here, devnet

**[08:25](https://youtube.com/watch?v=YTjYXii4WzI&t=505s)** ton are all to do with how tail scale mounts the network device.

**[08:30](https://youtube.com/watch?v=YTjYXii4WzI&t=510s)** And finally, we've got the actual sterling PDF application

**[08:33](https://youtube.com/watch?v=YTjYXii4WzI&t=513s)** itself. Remember, the only super important thing is to make sure

**[08:37](https://youtube.com/watch?v=YTjYXii4WzI&t=517s)** that this name here matches the name of the service further up in

**[08:40](https://youtube.com/watch?v=YTjYXii4WzI&t=520s)** the file. So this key here must match the service key that you

**[08:45](https://youtube.com/watch?v=YTjYXii4WzI&t=525s)** define under the network mode setting in the application itself.

**[08:48](https://youtube.com/watch?v=YTjYXii4WzI&t=528s)** Now, also note, we don't have any ports exposed whatsoever. I mean,

**[08:52](https://youtube.com/watch?v=YTjYXii4WzI&t=532s)** typically, you might do something like this in a Docker

**[08:55](https://youtube.com/watch?v=YTjYXii4WzI&t=535s)** compose file, which exposes port 8080 onto the Linux host itself.

**[08:59](https://youtube.com/watch?v=YTjYXii4WzI&t=539s)** We don't want to do that. We want to keep everything encapsulated

**[09:02](https://youtube.com/watch?v=YTjYXii4WzI&t=542s)** within side the container and put on to our tailnet. From there,

**[09:07](https://youtube.com/watch?v=YTjYXii4WzI&t=547s)** we should be good to go. So let's give this a world shall we?

**[09:10](https://youtube.com/watch?v=YTjYXii4WzI&t=550s)** Let's do Docker compose up minus D. So you're just going to pull

**[09:15](https://youtube.com/watch?v=YTjYXii4WzI&t=555s)** down the sterling PDF container. It's seven hundred megabytes.

**[09:18](https://youtube.com/watch?v=YTjYXii4WzI&t=558s)** So we'll take a minute or two. Once that's done, we can do Docker

**[09:23](https://youtube.com/watch?v=YTjYXii4WzI&t=563s)** compose logs minus F and just see what's going on. Scroll back up.

**[09:29](https://youtube.com/watch?v=YTjYXii4WzI&t=569s)** I don't see any dangerous looking stuff. Awesome. Cool.

**[09:33](https://youtube.com/watch?v=YTjYXii4WzI&t=573s)** So if I go back now to my machines page, hopefully we will see PDF.

**[09:37](https://youtube.com/watch?v=YTjYXii4WzI&t=577s)** Absolutely. There it is. Note that it's available through not only a

**[09:41](https://youtube.com/watch?v=YTjYXii4WzI&t=581s)** fully qualified domain name of Velociraptor Hyphen noodle fish.

**[09:45](https://youtube.com/watch?v=YTjYXii4WzI&t=585s)** And we can check that in the DNS tab over here as to what my

**[09:48](https://youtube.com/watch?v=YTjYXii4WzI&t=588s)** tailnet name should be. But if I now go to HTTP colon slash slash PDF,

**[09:54](https://youtube.com/watch?v=YTjYXii4WzI&t=594s)** hyphen port 80 because it's listing on port 80 remember, we've now

**[09:58](https://youtube.com/watch?v=YTjYXii4WzI&t=598s)** added sterling PDF to our tailnet alongside remember that banana is

**[10:03](https://youtube.com/watch?v=YTjYXii4WzI&t=603s)** still running on that same host. Look, you can actually see in the background

**[10:07](https://youtube.com/watch?v=YTjYXii4WzI&t=607s)** because we've got the logs running. You can actually see that it's doing

**[10:11](https://youtube.com/watch?v=YTjYXii4WzI&t=611s)** the requests in real time. How fun is that? Same with sterling PDF as well.

**[10:16](https://youtube.com/watch?v=YTjYXii4WzI&t=616s)** So this is a fantastic app. I can't recommend sterling PDF enough to you.

**[10:22](https://youtube.com/watch?v=YTjYXii4WzI&t=622s)** But there you go. That's that's really the general principle of how you

**[10:25](https://youtube.com/watch?v=YTjYXii4WzI&t=625s)** connect multiple containers on the same host using an O off client as well

**[10:30](https://youtube.com/watch?v=YTjYXii4WzI&t=630s)** as an off key using Docker. Now for those of you that don't want to type

**[10:34](https://youtube.com/watch?v=YTjYXii4WzI&t=634s)** PDF colon 8080 if you hate port numbers as much as I do, you just want to

**[10:38](https://youtube.com/watch?v=YTjYXii4WzI&t=638s)** have a TLS certificate and have this all taken care of for you using

**[10:42](https://youtube.com/watch?v=YTjYXii4WzI&t=642s)** let's encrypt. Well, I'm going to show you how to do that. And the first step

**[10:46](https://youtube.com/watch?v=YTjYXii4WzI&t=646s)** is to go into your tailscale admin console under DNS. We need to go all the

**[10:51](https://youtube.com/watch?v=YTjYXii4WzI&t=651s)** way down to the bottom and click on enable HTTPS certificates. Next, we want

**[10:56](https://youtube.com/watch?v=YTjYXii4WzI&t=656s)** to go into our Linux host and see where it's storing app data. So in our

**[11:01](https://youtube.com/watch?v=YTjYXii4WzI&t=661s)** Docker compose file, I defined a directory for our tailscale container for

**[11:05](https://youtube.com/watch?v=YTjYXii4WzI&t=665s)** sterling PDF for something called TS underscore serve underscore config.

**[11:11](https://youtube.com/watch?v=YTjYXii4WzI&t=671s)** This is a JSON file. Again, there'll be a link in the description down

**[11:14](https://youtube.com/watch?v=YTjYXii4WzI&t=674s)** below for the configuration for something called tailscale serve.

**[11:17](https://youtube.com/watch?v=YTjYXii4WzI&t=677s)** This is a feature built into tailscale that lets you automatically get TLS

**[11:21](https://youtube.com/watch?v=YTjYXii4WzI&t=681s)** certificates for any service hosted on your tailnet without having to

**[11:26](https://youtube.com/watch?v=YTjYXii4WzI&t=686s)** worry about things like reverse proxies and API keys and owning a DNS

**[11:31](https://youtube.com/watch?v=YTjYXii4WzI&t=691s)** name, all that kind of stuff. Super simple, super easy. Now, I'm going

**[11:35](https://youtube.com/watch?v=YTjYXii4WzI&t=695s)** to uncomment this line here of TS serve config and go into the config

**[11:40](https://youtube.com/watch?v=YTjYXii4WzI&t=700s)** directory, which we created a moment ago. And then I'm just going to create

**[11:43](https://youtube.com/watch?v=YTjYXii4WzI&t=703s)** sterling.json. In here, I'm going to paste in these few lines of code and

**[11:49](https://youtube.com/watch?v=YTjYXii4WzI&t=709s)** notice that we have some magic variables in here. This means you don't need

**[11:53](https://youtube.com/watch?v=YTjYXii4WzI&t=713s)** to hard code anything at all, except for the port number of the service

**[11:57](https://youtube.com/watch?v=YTjYXii4WzI&t=717s)** that you want to proxy. So in our case, sterling PDF runs on 8080. If

**[12:02](https://youtube.com/watch?v=YTjYXii4WzI&t=722s)** your application runs on a different port, you'll want to change this to

**[12:05](https://youtube.com/watch?v=YTjYXii4WzI&t=725s)** match the port of the service that you want to proxy. That's the only

**[12:08](https://youtube.com/watch?v=YTjYXii4WzI&t=728s)** thing you've got to change. Now, once you've made those changes, the

**[12:12](https://youtube.com/watch?v=YTjYXii4WzI&t=732s)** easiest way to get the domain that's been exposed, you know, just double

**[12:15](https://youtube.com/watch?v=YTjYXii4WzI&t=735s)** check what's going on is to use this Docker exec command here. So we'll

**[12:19](https://youtube.com/watch?v=YTjYXii4WzI&t=739s)** do Docker exec hyphen it and then the name of the sterling PDF tailscale

**[12:26](https://youtube.com/watch?v=YTjYXii4WzI&t=746s)** container, not the PDF container itself. Remember the sidecar tailscale

**[12:29](https://youtube.com/watch?v=YTjYXii4WzI&t=749s)** container. Then we'll just do tailscale serve status. And you can see here

**[12:33](https://youtube.com/watch?v=YTjYXii4WzI&t=753s)** that we're proxying a local host inside the container off from port 80 on to

**[12:39](https://youtube.com/watch?v=YTjYXii4WzI&t=759s)** HTTPS PDF velociraptor hyphen noodle fish. Now, this will take a few

**[12:45](https://youtube.com/watch?v=YTjYXii4WzI&t=765s)** seconds because underneath we're actually going out to let's encrypt,

**[12:49](https://youtube.com/watch?v=YTjYXii4WzI&t=769s)** generating the certificate and then installing it in the local system. That

**[12:52](https://youtube.com/watch?v=YTjYXii4WzI&t=772s)** can take anywhere from five to 30 seconds, depending on how busy the

**[12:56](https://youtube.com/watch?v=YTjYXii4WzI&t=776s)** let's encrypt API is. And you see in real time, whilst I was talking, we've

**[13:01](https://youtube.com/watch?v=YTjYXii4WzI&t=781s)** just generated the HTTPS certificate for this service on this domain name.

**[13:06](https://youtube.com/watch?v=YTjYXii4WzI&t=786s)** And you can see that we now have a secure connection backed by a

**[13:09](https://youtube.com/watch?v=YTjYXii4WzI&t=789s)** let's encrypt certificate. Note that you can do the same thing with tailscale

**[13:13](https://youtube.com/watch?v=YTjYXii4WzI&t=793s)** funnel, which is basically tailscale serve, but it exposes it to the internet.

**[13:18](https://youtube.com/watch?v=YTjYXii4WzI&t=798s)** There are some extra steps you'll need to follow in the ACLs, and I'll link

**[13:20](https://youtube.com/watch?v=YTjYXii4WzI&t=800s)** to the documentation for tailscale funnel down below. So there we have it.

**[13:25](https://youtube.com/watch?v=YTjYXii4WzI&t=805s)** That is the getting started guide for tailscale and Docker. Don't forget

**[13:29](https://youtube.com/watch?v=YTjYXii4WzI&t=809s)** down in the description down below, there are a whole bunch of links and resources

**[13:32](https://youtube.com/watch?v=YTjYXii4WzI&t=812s)** available for you, the GitHub repo with code snippets, as well as the original

**[13:36](https://youtube.com/watch?v=YTjYXii4WzI&t=816s)** blog post, and of course, the original YouTube video from the spring as well.

**[13:40](https://youtube.com/watch?v=YTjYXii4WzI&t=820s)** Don't forget to let us know how you're using tailscale in the comments down

**[13:43](https://youtube.com/watch?v=YTjYXii4WzI&t=823s)** below. Or indeed, ask us any questions we didn't cover in today's video.

**[13:47](https://youtube.com/watch?v=YTjYXii4WzI&t=827s)** We're going to be doing some Q&As and live streams and that kind of thing over

**[13:51](https://youtube.com/watch?v=YTjYXii4WzI&t=831s)** the coming weeks and months. So do let us know in the comments down below.

**[13:55](https://youtube.com/watch?v=YTjYXii4WzI&t=835s)** Thank you so much for watching. And until next time, I've been Alex from

**[13:58](https://youtube.com/watch?v=YTjYXii4WzI&t=838s)** tailscale.

---

*Automatically generated transcript. May contain errors.*
