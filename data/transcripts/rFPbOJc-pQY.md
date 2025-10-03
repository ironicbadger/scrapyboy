---
video_id: "rFPbOJc-pQY"
title: "This recipe manager is really useful! Mealie overview and setup guide"
description: "In today's video Alex walks you through the self-hosted recipe manager app called Mealie. We'll cover what the app is and does before moving onto how to deploy it to your Tailnet using docker. Then, t..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-06-27"
duration_seconds: 1735
youtube_url: "https://www.youtube.com/watch?v=rFPbOJc-pQY"
thumbnail_url: "https://i.ytimg.com/vi/rFPbOJc-pQY/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:56:26.251209"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 5522
transcription_time_seconds: 51.0
---

# This recipe manager is really useful! Mealie overview and setup guide

**[00:00](https://youtube.com/watch?v=rFPbOJc-pQY&t=0s)** How many times have you been looking for a recipe online, only to be bombarded by adverts

**[00:05](https://youtube.com/watch?v=rFPbOJc-pQY&t=5s)** or somebody's life story with a massive long exposition at the beginning of the article,

**[00:10](https://youtube.com/watch?v=rFPbOJc-pQY&t=10s)** mostly so they can inject more ads into the article, by the way.

**[00:13](https://youtube.com/watch?v=rFPbOJc-pQY&t=13s)** Well, Migly is a self-hosted recipe manager that strips all that stuff away for you.

**[00:18](https://youtube.com/watch?v=rFPbOJc-pQY&t=18s)** So I'm going to show you in today's video how to deploy Migly onto your tailnet and

**[00:22](https://youtube.com/watch?v=rFPbOJc-pQY&t=22s)** access it from anywhere using Tailscale.

**[00:26](https://youtube.com/watch?v=rFPbOJc-pQY&t=26s)** So I'm going to split this video up into a few sections.

**[00:28](https://youtube.com/watch?v=rFPbOJc-pQY&t=28s)** In this first few minutes, we'll be looking at the application itself.

**[00:31](https://youtube.com/watch?v=rFPbOJc-pQY&t=31s)** The second half, we'll be looking at how to deploy Migly using Docker Compose.

**[00:36](https://youtube.com/watch?v=rFPbOJc-pQY&t=36s)** And then at the end, there's a one more thing, because you can actually make AI do stuff

**[00:41](https://youtube.com/watch?v=rFPbOJc-pQY&t=41s)** with Migly now.

**[00:42](https://youtube.com/watch?v=rFPbOJc-pQY&t=42s)** It's a fairly new feature, but it kind of works.

**[00:44](https://youtube.com/watch?v=rFPbOJc-pQY&t=44s)** So there'll be chapters down below, along with all the links to all the Docker Compose

**[00:48](https://youtube.com/watch?v=rFPbOJc-pQY&t=48s)** file and all that kind of stuff, you need in the description.

**[00:51](https://youtube.com/watch?v=rFPbOJc-pQY&t=51s)** So let's add something to this, because I know you haven't seen this before.

**[00:56](https://youtube.com/watch?v=rFPbOJc-pQY&t=56s)** Look, Sammon Teriyaki, Teriyaki recipe, I don't know.

**[01:02](https://youtube.com/watch?v=rFPbOJc-pQY&t=62s)** Let's just pick a random one and see how much of a life story.

**[01:10](https://youtube.com/watch?v=rFPbOJc-pQY&t=70s)** The allure of Teriyaki smokes, goodness.

**[01:13](https://youtube.com/watch?v=rFPbOJc-pQY&t=73s)** I just want the recipe, okay, I'm going to copy that URL to my clipboard, and then going

**[01:18](https://youtube.com/watch?v=rFPbOJc-pQY&t=78s)** to go to create and import from URL, I'm going to create this recipe inside my little

**[01:24](https://youtube.com/watch?v=rFPbOJc-pQY&t=84s)** Migly, my little Migly Vault right here.

**[01:27](https://youtube.com/watch?v=rFPbOJc-pQY&t=87s)** So this goes out to recipesaver.com, recipesaver.com, and scrapes the contents of the website, puts

**[01:34](https://youtube.com/watch?v=rFPbOJc-pQY&t=94s)** all the steps, one by one, in here for me, gets me all the ingredients, how nice is this.

**[01:41](https://youtube.com/watch?v=rFPbOJc-pQY&t=101s)** I can register that I made this, for example, two weeks ago, fishy, that's how it was,

**[01:49](https://youtube.com/watch?v=rFPbOJc-pQY&t=109s)** add that to the timeline, and then I can actually look at all the different times I made

**[01:52](https://youtube.com/watch?v=rFPbOJc-pQY&t=112s)** this dish.

**[01:53](https://youtube.com/watch?v=rFPbOJc-pQY&t=113s)** Isn't that fun?

**[01:55](https://youtube.com/watch?v=rFPbOJc-pQY&t=115s)** Yeah, there you go, pretty fun.

**[01:58](https://youtube.com/watch?v=rFPbOJc-pQY&t=118s)** Under the edit option is a bunch of other stuff here, you can be like total time is two hours,

**[02:03](https://youtube.com/watch?v=rFPbOJc-pQY&t=123s)** for example, prep time is 20 minutes, 20 minutes, and then two hours, whatever.

**[02:10](https://youtube.com/watch?v=rFPbOJc-pQY&t=130s)** You can modify all sorts of stuff under here, you can make it show in a landscape view,

**[02:14](https://youtube.com/watch?v=rFPbOJc-pQY&t=134s)** so that the picture of the fish shows at the top, I actually kind of like that view

**[02:18](https://youtube.com/watch?v=rFPbOJc-pQY&t=138s)** better, but yeah, entirely up to you, it's a self-hosted application, so you are in full

**[02:24](https://youtube.com/watch?v=rFPbOJc-pQY&t=144s)** control, I love that.

**[02:26](https://youtube.com/watch?v=rFPbOJc-pQY&t=146s)** You can add a bunch of ingredients, you can add tags, if there's a special thing, so for

**[02:31](https://youtube.com/watch?v=rFPbOJc-pQY&t=151s)** example, I don't know, fish hook, for example, on-hand, let's create that, tags, I'm going

**[02:39](https://youtube.com/watch?v=rFPbOJc-pQY&t=159s)** to put salmon, there's a tag, why not, oh, salmon, yeah, create the tag, and then a category

**[02:46](https://youtube.com/watch?v=rFPbOJc-pQY&t=166s)** I'm going to put as fish, which did that same mistake twice with the UX, didn't I?

**[02:55](https://youtube.com/watch?v=rFPbOJc-pQY&t=175s)** Okay, so that's how the application itself does the basics, and let's just save those

**[02:59](https://youtube.com/watch?v=rFPbOJc-pQY&t=179s)** changes, and see how they get presented now, you can see that I've got all the prep time

**[03:03](https://youtube.com/watch?v=rFPbOJc-pQY&t=183s)** stuff right here, in fact, actually, I think I might prefer the non-landscape view, I might

**[03:09](https://youtube.com/watch?v=rFPbOJc-pQY&t=189s)** be full of it, let's just put it back to non-landscape view, and click on save, there we go, yeah,

**[03:16](https://youtube.com/watch?v=rFPbOJc-pQY&t=196s)** actually, I think I prefer that one, so you've got a picture there, and then you've got

**[03:19](https://youtube.com/watch?v=rFPbOJc-pQY&t=199s)** all the stuff just here, now if you're in a cook mode, and you want to just literally

**[03:24](https://youtube.com/watch?v=rFPbOJc-pQY&t=204s)** have the basics on the screen in front of you, that's what that button does there, and

**[03:28](https://youtube.com/watch?v=rFPbOJc-pQY&t=208s)** I think it's really nicely laid out, so that's the basic recipe stuff, like I can give

**[03:32](https://youtube.com/watch?v=rFPbOJc-pQY&t=212s)** it stars and put it in my favourites all the rest of it, now let's look at the meal

**[03:36](https://youtube.com/watch?v=rFPbOJc-pQY&t=216s)** planner, because this one's actually got a real amount of utility, like people integrate

**[03:40](https://youtube.com/watch?v=rFPbOJc-pQY&t=220s)** this with home assistance, so you can actually have dashboards up on your fridge, or a little

**[03:44](https://youtube.com/watch?v=rFPbOJc-pQY&t=224s)** tablet on the wall or something, or even just pull out your phone when you're at the grocery

**[03:47](https://youtube.com/watch?v=rFPbOJc-pQY&t=227s)** store and say like, what's for dinner in three days time, maybe I should buy some fresh

**[03:51](https://youtube.com/watch?v=rFPbOJc-pQY&t=231s)** veg whilst I'm here, for example, I'm going to go in here and click edit, and I'm going

**[03:55](https://youtube.com/watch?v=rFPbOJc-pQY&t=235s)** to roll the dice for lunch, why not, it's going to give me chocolate cookies, it's going

**[04:02](https://youtube.com/watch?v=rFPbOJc-pQY&t=242s)** to give me pork with roasted carrots and rice for breakfast, alright, whatever, random dinner,

**[04:09](https://youtube.com/watch?v=rFPbOJc-pQY&t=249s)** chocolate cookies again, yeah, here we go, alright, so you get the idea, you can create

**[04:14](https://youtube.com/watch?v=rFPbOJc-pQY&t=254s)** a meal plan, and then this way the entire family can look ahead and see what's coming

**[04:18](https://youtube.com/watch?v=rFPbOJc-pQY&t=258s)** throughout the week, and they can dive in and all that kind of stuff, the meal planner

**[04:23](https://youtube.com/watch?v=rFPbOJc-pQY&t=263s)** is fantastic and it's probably the single biggest reason to use meal over something like

**[04:29](https://youtube.com/watch?v=rFPbOJc-pQY&t=269s)** a paper recipe card or something like that, I mean yes you can write on a little chalkboard

**[04:34](https://youtube.com/watch?v=rFPbOJc-pQY&t=274s)** on the side of the fridge or whatever, but this is pretty nice, now the shopping list

**[04:39](https://youtube.com/watch?v=rFPbOJc-pQY&t=279s)** option is also pretty useful, and it's called ABC, and then you and household party

**[04:46](https://youtube.com/watch?v=rFPbOJc-pQY&t=286s)** can be in like I need milk and eggs and all that kind of stuff, you know, I have shopping

**[04:50](https://youtube.com/watch?v=rFPbOJc-pQY&t=290s)** list works, pretty interesting, the timeline here, this is like a global view of all the

**[04:56](https://youtube.com/watch?v=rFPbOJc-pQY&t=296s)** recipes that you've had, and you can see that I made cookies and brisket and salmon and

**[05:01](https://youtube.com/watch?v=rFPbOJc-pQY&t=301s)** a bunch of other stuff, I'm getting hungry, making this video, but then the cookbooks

**[05:05](https://youtube.com/watch?v=rFPbOJc-pQY&t=305s)** on the left, you can create so, for example, I'll show you later in the video, my wife has

**[05:09](https://youtube.com/watch?v=rFPbOJc-pQY&t=309s)** a bunch of these hello fresh recipe cards, for example, I could literally make a hello

**[05:13](https://youtube.com/watch?v=rFPbOJc-pQY&t=313s)** fresh specific cookbook if I wanted to or a barbecue smoking cookbook or whatever, and

**[05:21](https://youtube.com/watch?v=rFPbOJc-pQY&t=321s)** then there are a bunch of different ways to organize these things within Mealy as well.

**[05:25](https://youtube.com/watch?v=rFPbOJc-pQY&t=325s)** That's Mealy, really, there's a bunch of stuff on the settings which for the most part

**[05:29](https://youtube.com/watch?v=rFPbOJc-pQY&t=329s)** you don't really have to worry about, I mean I made a video a couple of weeks ago on

**[05:33](https://youtube.com/watch?v=rFPbOJc-pQY&t=333s)** Pocket ID, for Open ID Connect, so this integrates with that nicely too, I didn't configure

**[05:38](https://youtube.com/watch?v=rFPbOJc-pQY&t=338s)** it, but you can also have this configured to send out emails through SMTP, I don't know

**[05:43](https://youtube.com/watch?v=rFPbOJc-pQY&t=343s)** what that purpose would serve, maybe you could email yourself a shopping list, but with

**[05:48](https://youtube.com/watch?v=rFPbOJc-pQY&t=348s)** tailscarly you can just access this from anywhere, notice that this is on a fully qualified

**[05:52](https://youtube.com/watch?v=rFPbOJc-pQY&t=352s)** domain name as it is, there's a bunch of stuff here with users, I suppose that one could

**[05:57](https://youtube.com/watch?v=rFPbOJc-pQY&t=357s)** be useful, you want to create a user for you, your partner, or maybe a kid or whatever,

**[06:02](https://youtube.com/watch?v=rFPbOJc-pQY&t=362s)** but yeah, I mean there is a bunch of stuff under the hood with Mealy that you could get into,

**[06:05](https://youtube.com/watch?v=rFPbOJc-pQY&t=365s)** but really the core of the application really is just looking at recipes and finding a good

**[06:11](https://youtube.com/watch?v=rFPbOJc-pQY&t=371s)** way to surface them, so you can search with a keyboard shortcut of a forward slash and just type

**[06:17](https://youtube.com/watch?v=rFPbOJc-pQY&t=377s)** brisket, for example, there it is, there's my brisket recipe, for example, so yeah I think with

**[06:23](https://youtube.com/watch?v=rFPbOJc-pQY&t=383s)** that quick overview of the Mealy application out the way, it's time to move on to how to deploy

**[06:27](https://youtube.com/watch?v=rFPbOJc-pQY&t=387s)** it with Docker Compose, now I'm sure this will come as a huge surprise to those of you familiar

**[06:32](https://youtube.com/watch?v=rFPbOJc-pQY&t=392s)** with the channel, but we're going to deploy Mealy today using Docker. In fact, we're going to deploy

**[06:38](https://youtube.com/watch?v=rFPbOJc-pQY&t=398s)** it on that little Dell one liter small form factor PC that I featured in all of the self-hosting,

**[06:43](https://youtube.com/watch?v=rFPbOJc-pQY&t=403s)** that gets started with self-hosting series that we've been doing on the channel lately,

**[06:46](https://youtube.com/watch?v=rFPbOJc-pQY&t=406s)** there's a link to that video series up there, that playlist. Now if we head over to Mealy.io,

**[06:51](https://youtube.com/watch?v=rFPbOJc-pQY&t=411s)** the project itself recommends that you use Docker to deploy it as well, in fact if we go to the

**[06:56](https://youtube.com/watch?v=rFPbOJc-pQY&t=416s)** installation checklist, just here, you can see at the top of their documentation, they have a wonderful

**[07:01](https://youtube.com/watch?v=rFPbOJc-pQY&t=421s)** step-by-step guide here, honestly. If you're new to all this stuff, you'll actually learn quite a bit

**[07:05](https://youtube.com/watch?v=rFPbOJc-pQY&t=425s)** in this documentation, or you can just copy and paste the Docker Compose YAML file, which I have

**[07:11](https://youtube.com/watch?v=rFPbOJc-pQY&t=431s)** customized for our needs just here. And this file, by the way, is linked into the description down

**[07:17](https://youtube.com/watch?v=rFPbOJc-pQY&t=437s)** below in my code snippets repo that accompanies pretty much every video that we make on this channel.

**[07:23](https://youtube.com/watch?v=rFPbOJc-pQY&t=443s)** So there's a lot going on in this file. Let's break it down a little bit. First of all,

**[07:28](https://youtube.com/watch?v=rFPbOJc-pQY&t=448s)** we have the MealyTS container. This essentially is called a sidecar container. So you have the

**[07:34](https://youtube.com/watch?v=rFPbOJc-pQY&t=454s)** main app over here, and you have a little tiny sidecar app over here that's just running

**[07:39](https://youtube.com/watch?v=rFPbOJc-pQY&t=459s)** tail scale because Mealy itself doesn't have tail scale installed in it. So we wouldn't be able

**[07:44](https://youtube.com/watch?v=rFPbOJc-pQY&t=464s)** to access it over our townnet remotely without this sidecar container. So that's what this first

**[07:49](https://youtube.com/watch?v=rFPbOJc-pQY&t=469s)** sort of set of stuff here is doing. We need to get ourselves an off key to put into this file here,

**[07:55](https://youtube.com/watch?v=rFPbOJc-pQY&t=475s)** which is really easily done by heading over to tailscale.com, go to settings and then keys,

**[08:01](https://youtube.com/watch?v=rFPbOJc-pQY&t=481s)** and then generate an off key. And I'm going quickly, but I do this a lot on the channel. So please

**[08:07](https://youtube.com/watch?v=rFPbOJc-pQY&t=487s)** pause, rewind, whatever you need to do to make this this work for you. But I'm going to create this

**[08:12](https://youtube.com/watch?v=rFPbOJc-pQY&t=492s)** key here called Mealy. That's optional. I'm going to select reusable because I am doing a demo,

**[08:17](https://youtube.com/watch?v=rFPbOJc-pQY&t=497s)** so I will likely tear this up and down a few times. Exploration. This is only the length of time

**[08:22](https://youtube.com/watch?v=rFPbOJc-pQY&t=502s)** this key is allowed to authorize services to your townnet. If you authorize a service and

**[08:29](https://youtube.com/watch?v=rFPbOJc-pQY&t=509s)** it lives longer than 90 days, the service will stay authenticated. But if you want to re-authenticate

**[08:34](https://youtube.com/watch?v=rFPbOJc-pQY&t=514s)** the service, you'll need to regenerate this off key after 90 days. If emerald, if the service

**[08:39](https://youtube.com/watch?v=rFPbOJc-pQY&t=519s)** goes offline, it will also disappear from your townnet and then tags. We're not going to talk

**[08:44](https://youtube.com/watch?v=rFPbOJc-pQY&t=524s)** about tags today, but they're very powerful and you can learn more about those over at the tailscale

**[08:48](https://youtube.com/watch?v=rFPbOJc-pQY&t=528s)** documentation. So I'm going to generate a key and then just copy that to my clipboard,

**[08:53](https://youtube.com/watch?v=rFPbOJc-pQY&t=533s)** go back to VS code and just paste in that value right here. And that's all we need to do for the

**[09:00](https://youtube.com/watch?v=rFPbOJc-pQY&t=540s)** tailscale TS sidecar container, except I suppose in my case in the self-hosted series, this is where

**[09:08](https://youtube.com/watch?v=rFPbOJc-pQY&t=548s)** I have put all of the app data for all of our containers. So mount SSD1 app data and then the name

**[09:15](https://youtube.com/watch?v=rFPbOJc-pQY&t=555s)** of the app Miele and then I've got a tailscale sub directory under that. So you will want to

**[09:19](https://youtube.com/watch?v=rFPbOJc-pQY&t=559s)** customize this little portion here so that it matches in both places as your sort of app data path

**[09:27](https://youtube.com/watch?v=rFPbOJc-pQY&t=567s)** and that's what you need to do for the sidecar. So we can actually collapse this now. This is a

**[09:30](https://youtube.com/watch?v=rFPbOJc-pQY&t=570s)** YAML file, by the way, if we're not familiar with what we're looking at here, you have a bunch of,

**[09:35](https://youtube.com/watch?v=rFPbOJc-pQY&t=575s)** I guess, like top-level keys and each item in this, I think it's a dictionary underneath this key

**[09:41](https://youtube.com/watch?v=rFPbOJc-pQY&t=581s)** belongs to this kind of like parent here. So if you look on the left here in VS code, you can

**[09:47](https://youtube.com/watch?v=rFPbOJc-pQY&t=587s)** actually collapse the entire sidecar container to kind of clean up your view a little bit. Now Miele

**[09:53](https://youtube.com/watch?v=rFPbOJc-pQY&t=593s)** itself is another straightforward deployment here. You can see that we've got the image we're using

**[09:58](https://youtube.com/watch?v=rFPbOJc-pQY&t=598s)** from the GitHub container registry. This is the current tag at the time of filming 2.8.0 and that

**[10:06](https://youtube.com/watch?v=rFPbOJc-pQY&t=606s)** comes from the Miele project itself from their documentation as you can see right here. So I

**[10:14](https://youtube.com/watch?v=rFPbOJc-pQY&t=614s)** assume this updates. In fact, let's just go and check that. So in fact, yeah, you can see V2.8

**[10:20](https://youtube.com/watch?v=rFPbOJc-pQY&t=620s)** is the latest one, but where do we go these days? Releases, packages, probably. No, releases,

**[10:28](https://youtube.com/watch?v=rFPbOJc-pQY&t=628s)** where did you put, they used to be at the top. There you go. 2.8 is the most recent one, March 18th

**[10:36](https://youtube.com/watch?v=rFPbOJc-pQY&t=636s)** and today's June the 24th. So not the most fresh release, but yeah, it's totally fine. So

**[10:40](https://youtube.com/watch?v=rFPbOJc-pQY&t=640s)** in a couple of months. Okay, so that's where we get that from. That's where we get this sort of tag

**[10:46](https://youtube.com/watch?v=rFPbOJc-pQY&t=646s)** from here. Container name, this is optional, but it just keeps things clean on the remote host if

**[10:51](https://youtube.com/watch?v=rFPbOJc-pQY&t=651s)** you don't have a randomly generated name for your container. I'll always like this one here. Restart

**[10:56](https://youtube.com/watch?v=rFPbOJc-pQY&t=656s)** unless stopped. Yeah, I've actually since my Linux server.io days in those early containers that we

**[11:03](https://youtube.com/watch?v=rFPbOJc-pQY&t=663s)** wrote always preferred unless stopped. I mean, so some people put always in here. If I've stopped

**[11:09](https://youtube.com/watch?v=rFPbOJc-pQY&t=669s)** the container and I reboot the host, I don't want it to always restart. So that's why I put unless

**[11:14](https://youtube.com/watch?v=rFPbOJc-pQY&t=674s)** stopped in there. This line is where we connect the sidecar container of melee TS to our main

**[11:21](https://youtube.com/watch?v=rFPbOJc-pQY&t=681s)** application of melee. So this is how we sort of merge those two containers together and put this

**[11:26](https://youtube.com/watch?v=rFPbOJc-pQY&t=686s)** thing on your tailnet. This name here of service melee TS must match the top level key of the previous

**[11:33](https://youtube.com/watch?v=rFPbOJc-pQY&t=693s)** Yamol block, I suppose. It's a line two here, this key here of melee TS. That's how Docker compose

**[11:40](https://youtube.com/watch?v=rFPbOJc-pQY&t=700s)** knows how to reference that other service is with that string there. Okay, so this is a bunch of

**[11:47](https://youtube.com/watch?v=rFPbOJc-pQY&t=707s)** stuff that comes from the melee project itself about limiting the memory usage to one gig. Sure,

**[11:52](https://youtube.com/watch?v=rFPbOJc-pQY&t=712s)** fine, whatever. The Linux kernel is pretty good at managing this stuff itself, but it's not going

**[11:56](https://youtube.com/watch?v=rFPbOJc-pQY&t=716s)** to hurt to have a limit. So we may as well leave it there. This path again is where we store the

**[12:01](https://youtube.com/watch?v=rFPbOJc-pQY&t=721s)** persistent data. So this is where the recipes themselves are actually going to live on your

**[12:06](https://youtube.com/watch?v=rFPbOJc-pQY&t=726s)** little computer that you're using to do this self hosted project. And now we come to the fun part,

**[12:11](https://youtube.com/watch?v=rFPbOJc-pQY&t=731s)** the environment variables. So allow sign up false. This might seem like a little bit of a weird one,

**[12:15](https://youtube.com/watch?v=rFPbOJc-pQY&t=735s)** but we don't want anybody to be able to sign up to this willy nilly, but out of the box,

**[12:22](https://youtube.com/watch?v=rFPbOJc-pQY&t=742s)** it comes with a default admin user, which we can change to username and password later. This PGID

**[12:27](https://youtube.com/watch?v=rFPbOJc-pQY&t=747s)** and PUID thing here, 1000 numbers, refer to the user ID, the Linux user ID that's going to own the

**[12:35](https://youtube.com/watch?v=rFPbOJc-pQY&t=755s)** files in the bind mounted volumes that you've set here. So under this volume's line right here,

**[12:42](https://youtube.com/watch?v=rFPbOJc-pQY&t=762s)** this 1000 option is that's the use that's going to own those files. Time zone obviously set that

**[12:48](https://youtube.com/watch?v=rFPbOJc-pQY&t=768s)** accordingly, you know, America, New York for me on these coast. Then base URL. This is an interesting

**[12:54](https://youtube.com/watch?v=rFPbOJc-pQY&t=774s)** one. Okay, so where do we get this piece of information? Well, we are going to use the tail scale

**[13:00](https://youtube.com/watch?v=rFPbOJc-pQY&t=780s)** melee sidecar container as a reverse proxy for melee. And what's the reverse proxy? So when we

**[13:07](https://youtube.com/watch?v=rFPbOJc-pQY&t=787s)** want to access this web application, typically you go to an IP address number and a port number,

**[13:12](https://youtube.com/watch?v=rFPbOJc-pQY&t=792s)** but I hate that. I hate ports. It's insecure. You can't verify the identity. We can do better.

**[13:19](https://youtube.com/watch?v=rFPbOJc-pQY&t=799s)** Okay, so we're going to use tail scale as our reverse proxy today. But where did we get the value

**[13:25](https://youtube.com/watch?v=rFPbOJc-pQY&t=805s)** of melee dot velociraptor hyphen noodle fish? Well, if we look back at line four, you'll notice

**[13:30](https://youtube.com/watch?v=rFPbOJc-pQY&t=810s)** that host name variable here was set to melee. So if I called this, I don't know, goldfish,

**[13:36](https://youtube.com/watch?v=rFPbOJc-pQY&t=816s)** the name that this container would get on my tail net would actually be goldfish.

**[13:41](https://youtube.com/watch?v=rFPbOJc-pQY&t=821s)** Okay, so you see how those two things link together now. But what about the rest of it? Where does

**[13:45](https://youtube.com/watch?v=rFPbOJc-pQY&t=825s)** the velociraptor bit come from? Well, that comes from my tail scale admin console.

**[13:50](https://youtube.com/watch?v=rFPbOJc-pQY&t=830s)** So if I go to the DNS options right here, you'll see that my tail net has a nice name of velociraptor

**[13:55](https://youtube.com/watch?v=rFPbOJc-pQY&t=835s)** hyphen noodle fish dot TS dot net. Now, I can rename this tail net at any time if I want to. In fact,

**[14:00](https://youtube.com/watch?v=rFPbOJc-pQY&t=840s)** out of the box, tail scale provides a free, it's not the most pretty name in the world if I'm honest,

**[14:05](https://youtube.com/watch?v=rFPbOJc-pQY&t=845s)** but that's why we provide you the option to reroll the dice and rename your tail net with

**[14:09](https://youtube.com/watch?v=rFPbOJc-pQY&t=849s)** something a bit more, a bit more aloof, perhaps. So we've got something with a tail and something

**[14:15](https://youtube.com/watch?v=rFPbOJc-pQY&t=855s)** with scales. Very good. Okay, so down here also, we need to make sure we've got magic DNS enabled

**[14:21](https://youtube.com/watch?v=rFPbOJc-pQY&t=861s)** as well as HTTPS certificates. So that's all of the tail scale stuff taken care of. That's all you

**[14:27](https://youtube.com/watch?v=rFPbOJc-pQY&t=867s)** have to do, except copy this one file across here too. Mealy runs on the port 9000. Remember how

**[14:34](https://youtube.com/watch?v=rFPbOJc-pQY&t=874s)** it's talking about IP addresses and port numbers? We have to know what port mealy is running on,

**[14:38](https://youtube.com/watch?v=rFPbOJc-pQY&t=878s)** and in this case, this application runs on port 9000. So you'll want to modify this serve.json file

**[14:44](https://youtube.com/watch?v=rFPbOJc-pQY&t=884s)** to be the port of the application that you're running. So in our case, as I say, it's 9000.

**[14:49](https://youtube.com/watch?v=rFPbOJc-pQY&t=889s)** If it was a different application, you would just literally modify the port number to be whatever

**[14:54](https://youtube.com/watch?v=rFPbOJc-pQY&t=894s)** the application is using. So we're going to leave that one at 9000. We're also going to proxy TCP

**[15:00](https://youtube.com/watch?v=rFPbOJc-pQY&t=900s)** port 443. So for HTTPS requests and have them come through to this reverse proxy. So all we

**[15:08](https://youtube.com/watch?v=rFPbOJc-pQY&t=908s)** need to do now is connect to our remote host. And as I mentioned, I'm using the little delbox

**[15:15](https://youtube.com/watch?v=rFPbOJc-pQY&t=915s)** that we used in the first few parts of this self-hosting playlist. And this box has a few prerequisites

**[15:22](https://youtube.com/watch?v=rFPbOJc-pQY&t=922s)** that if you didn't follow those videos, you're going to need to make sure are installed and ready to go.

**[15:26](https://youtube.com/watch?v=rFPbOJc-pQY&t=926s)** You need to make sure you've got Docker on this host and also make sure that you've got tail scale.

**[15:31](https://youtube.com/watch?v=rFPbOJc-pQY&t=931s)** So Docker is going to be our application runtime and tail scale is on there mostly so that we can

**[15:36](https://youtube.com/watch?v=rFPbOJc-pQY&t=936s)** use tail scale SSH to connect to that remote host without worrying about SSH keys, but also it

**[15:42](https://youtube.com/watch?v=rFPbOJc-pQY&t=942s)** has a trick up its sleeve. In VS code, there is a tail scale extension and you can get that by going

**[15:48](https://youtube.com/watch?v=rFPbOJc-pQY&t=948s)** to the extensions page right here typing in tail scale and installing the tail scale extension into

**[15:54](https://youtube.com/watch?v=rFPbOJc-pQY&t=954s)** a VS code. Then make sure you're logged in to tail scale on your client. So this is a macOS laptop,

**[16:00](https://youtube.com/watch?v=rFPbOJc-pQY&t=960s)** of course. I'm logged in to my tail nets on that MacBook. The VS code extension will then pick up

**[16:07](https://youtube.com/watch?v=rFPbOJc-pQY&t=967s)** that authentication and I can now connect to my remote host at pve.whatever it was pve.philoceraptor.

**[16:14](https://youtube.com/watch?v=rFPbOJc-pQY&t=974s)** It can now connect to that and the file system on that node in VS code. And so under pve, if I right

**[16:20](https://youtube.com/watch?v=rFPbOJc-pQY&t=980s)** click on this, I've got a bunch of options. You can change your SSH user name if you need to.

**[16:24](https://youtube.com/watch?v=rFPbOJc-pQY&t=984s)** I'm just SSH in as root because it's easier for videos. It's perhaps not the best security practice

**[16:30](https://youtube.com/watch?v=rFPbOJc-pQY&t=990s)** but it's just me. It's a single user system so root, as I would say, to my foyerot. You have to deal

**[16:37](https://youtube.com/watch?v=rFPbOJc-pQY&t=997s)** with it. All right, change root directory. This one might be useful actually here so I'm going to

**[16:41](https://youtube.com/watch?v=rFPbOJc-pQY&t=1001s)** select slash MNT. So that way I don't have access to the entire file system of the computer.

**[16:47](https://youtube.com/watch?v=rFPbOJc-pQY&t=1007s)** And then under app data, I've got to make sure I've got a few things created here. So I actually

**[16:52](https://youtube.com/watch?v=rFPbOJc-pQY&t=1012s)** want to just open a terminal window at the melee directory under app data. So if we look in our

**[16:57](https://youtube.com/watch?v=rFPbOJc-pQY&t=1017s)** compose file, we'll see that all of these paths need to exist. So if I do a PWD, we can see that

**[17:04](https://youtube.com/watch?v=rFPbOJc-pQY&t=1024s)** we're currently in Mount SSD1 app data melee. Now, I need to make sure that I have a file now under,

**[17:13](https://youtube.com/watch?v=rFPbOJc-pQY&t=1033s)** where is it here, melee tail scale. So I need to do make DIR minus peak. So I'm going to do more

**[17:18](https://youtube.com/watch?v=rFPbOJc-pQY&t=1038s)** than one directory deep that doesn't exist. So make DIR minus peak tail scale slash config.

**[17:25](https://youtube.com/watch?v=rFPbOJc-pQY&t=1045s)** So what I now need to do is copy the contents of serve.json to the remote host. So I'm going to do

**[17:31](https://youtube.com/watch?v=rFPbOJc-pQY&t=1051s)** a command A to copy the entire file contents, command C to copy it to my clipboard, right click on

**[17:36](https://youtube.com/watch?v=rFPbOJc-pQY&t=1056s)** the config directory and just type in serve.json. That's now going to create a empty file on the remote

**[17:43](https://youtube.com/watch?v=rFPbOJc-pQY&t=1063s)** host into which I can just paste my tail scale serve configuration. And that's it. That's all we

**[17:48](https://youtube.com/watch?v=rFPbOJc-pQY&t=1068s)** need to worry about with the serve configuration. That's that bit that's configured here by the way.

**[17:54](https://youtube.com/watch?v=rFPbOJc-pQY&t=1074s)** And then in my compose.json file, I'm just going to paste this in in the remote host as well.

**[17:59](https://youtube.com/watch?v=rFPbOJc-pQY&t=1079s)** We're actually ready to go. So I'm going to come back out to level. So I'm in the route of the melee

**[18:03](https://youtube.com/watch?v=rFPbOJc-pQY&t=1083s)** directory. I want to be in the same context path as the or same directory as the compose.json file.

**[18:10](https://youtube.com/watch?v=rFPbOJc-pQY&t=1090s)** I can then do a Docker compose pull. This is going to pull down the tail scale image which

**[18:14](https://youtube.com/watch?v=rFPbOJc-pQY&t=1094s)** probably should already exist because I'm using it for other images on this other containers on

**[18:19](https://youtube.com/watch?v=rFPbOJc-pQY&t=1099s)** this host. And then it's also going to pull down the melee container as well. So I want the record

**[18:24](https://youtube.com/watch?v=rFPbOJc-pQY&t=1104s)** to show that melee currently doesn't exist on this tail net. But simply by doing a Docker compose

**[18:30](https://youtube.com/watch?v=rFPbOJc-pQY&t=1110s)** up, I'm actually going to do a logs minus F as well. Docker compose logs minus F to follow the

**[18:36](https://youtube.com/watch?v=rFPbOJc-pQY&t=1116s)** logs of what's going on here. You can see that we're now proxying port 9000 from within the

**[18:41](https://youtube.com/watch?v=rFPbOJc-pQY&t=1121s)** melee container out onto our tail net. So if we go back to the dashboard here, look, we've got

**[18:47](https://youtube.com/watch?v=rFPbOJc-pQY&t=1127s)** melee. All right. So let's get a fully qualified domain name here of melee.vulasser app to hyphen

**[18:52](https://youtube.com/watch?v=rFPbOJc-pQY&t=1132s)** noodle fish and paste that into our web browser. The first time you do this, it will take 10 to 20

**[19:00](https://youtube.com/watch?v=rFPbOJc-pQY&t=1140s)** seconds to generate a TLS certificate because tail scale serve in the background. You don't have to

**[19:05](https://youtube.com/watch?v=rFPbOJc-pQY&t=1145s)** do anything, but it's reaching out to let's encrypt to generate a full TLS certificate for this

**[19:12](https://youtube.com/watch?v=rFPbOJc-pQY&t=1152s)** instance. Now sometimes because I mess about with demos and stuff, I end up needing to go into

**[19:16](https://youtube.com/watch?v=rFPbOJc-pQY&t=1156s)** incognito mode just to create stuff because it kind of gets a bit confused. So hopefully that won't

**[19:21](https://youtube.com/watch?v=rFPbOJc-pQY&t=1161s)** happen to you, but if it does and you get an insecure message here, don't worry, it's probably working.

**[19:27](https://youtube.com/watch?v=rFPbOJc-pQY&t=1167s)** If you're just going to incognito mode, you can verify it's working by going to certificate is

**[19:32](https://youtube.com/watch?v=rFPbOJc-pQY&t=1172s)** valid. Let's encrypt. And if you see this all stuff here of issued on today and then expires on

**[19:38](https://youtube.com/watch?v=rFPbOJc-pQY&t=1178s)** whenever you're good to go. All right. So the first login, as I talked about, you need to enter a

**[19:44](https://youtube.com/watch?v=rFPbOJc-pQY&t=1184s)** username and a password, which is the default settings. It's then going to ask you to create a

**[19:52](https://youtube.com/watch?v=rFPbOJc-pQY&t=1192s)** user in this sort of onboarding wizard. So I'm just going to create z4d and then once I finish filling

**[19:57](https://youtube.com/watch?v=rFPbOJc-pQY&t=1197s)** out that form, I'm just going to click on the next button, enable public access. This one actually

**[20:01](https://youtube.com/watch?v=rFPbOJc-pQY&t=1201s)** is pretty worth talking about because a lot of times when you want to access a recipe, you don't

**[20:07](https://youtube.com/watch?v=rFPbOJc-pQY&t=1207s)** really want to have to log in or at least I don't. I want to grab my iPad, I want to go to the URL

**[20:12](https://youtube.com/watch?v=rFPbOJc-pQY&t=1212s)** and pull up the recipe. So by enabling public access, I'm able to do that without having to log in

**[20:19](https://youtube.com/watch?v=rFPbOJc-pQY&t=1219s)** to see the, I mean, there's nothing, you know, it's not four knocks. So my story recipes in here and

**[20:23](https://youtube.com/watch?v=rFPbOJc-pQY&t=1223s)** you know, nothing crazy. So I'm going to submit that and then hopefully user updated. Good. I actually

**[20:29](https://youtube.com/watch?v=rFPbOJc-pQY&t=1229s)** think we are ready to go. I'm going to click on the home button. As you would expect, there are no

**[20:34](https://youtube.com/watch?v=rFPbOJc-pQY&t=1234s)** recipes right now. So I don't know, the best cookie recipe ever. Let's just pick one at random.

**[20:43](https://youtube.com/watch?v=rFPbOJc-pQY&t=1243s)** This one, I have no idea how much life story have we got in this one? Yeah.

**[20:52](https://youtube.com/watch?v=rFPbOJc-pQY&t=1252s)** Where is the actual recipe? If this is all just so they can serve you more ads, you can tell I've

**[20:59](https://youtube.com/watch?v=rFPbOJc-pQY&t=1259s)** got my ad blocker working on this network. I've got an ad guard home instance on this network.

**[21:05](https://youtube.com/watch?v=rFPbOJc-pQY&t=1265s)** Anyway, I digress slightly import by URL. So I'm going to create my first recipe by importing via

**[21:12](https://youtube.com/watch?v=rFPbOJc-pQY&t=1272s)** URL. So let's create that. It's now going to strip all of the life story. It's going to strip out

**[21:18](https://youtube.com/watch?v=rFPbOJc-pQY&t=1278s)** just the useful bit and look at that. Isn't that wonderful? So we can see now that you've got all

**[21:23](https://youtube.com/watch?v=rFPbOJc-pQY&t=1283s)** the steps here of preheat the other and here's all your ingredients, et cetera, et cetera.

**[21:27](https://youtube.com/watch?v=rFPbOJc-pQY&t=1287s)** What does a checkbox do? I often wonder that. But there's a bunch of stuff you can do. So opening

**[21:32](https://youtube.com/watch?v=rFPbOJc-pQY&t=1292s)** the timeline, you can see when you created it. Now, let's do a make because this is really

**[21:37](https://youtube.com/watch?v=rFPbOJc-pQY&t=1297s)** interesting. If I do, can I say I made it tomorrow? Beautiful. Let's go with that. I can add an

**[21:46](https://youtube.com/watch?v=rFPbOJc-pQY&t=1306s)** image, I can add it, I can literally, wow, okay, that's fun. So I've got the I created the recipe

**[21:53](https://youtube.com/watch?v=rFPbOJc-pQY&t=1313s)** and then Z-Fod, Z-Fod made this. I guess it's like you scrap booking your own cooking.

**[21:58](https://youtube.com/watch?v=rFPbOJc-pQY&t=1318s)** That's kind of fun. Add that to favorites. Yes, sure. Why not? Then under the edit option here,

**[22:04](https://youtube.com/watch?v=rFPbOJc-pQY&t=1324s)** there's a whole bunch of stuff you can say like four hours prep time is five minutes,

**[22:13](https://youtube.com/watch?v=rFPbOJc-pQY&t=1333s)** cook time is therefore three hours, 55 minutes, if my maths is correct. Here's a tried and true

**[22:22](https://youtube.com/watch?v=rFPbOJc-pQY&t=1342s)** chocolate chip cookie recipe that will impress everybody because that's important,

**[22:25](https://youtube.com/watch?v=rFPbOJc-pQY&t=1345s)** impressing other people is very important, apparently. Landscape nutrition values. There's

**[22:31](https://youtube.com/watch?v=rFPbOJc-pQY&t=1351s)** just so much stuff going on in this in Mealy. It really is fantastic. Categories. Let's create one

**[22:36](https://youtube.com/watch?v=rFPbOJc-pQY&t=1356s)** of sweet treats, for example. There we go. So I think we get the idea, right? We can now add

**[22:45](https://youtube.com/watch?v=rFPbOJc-pQY&t=1365s)** recipes, we can edit them and really, I think it looks, as Jamie Oliver would say in the UK,

**[22:51](https://youtube.com/watch?v=rFPbOJc-pQY&t=1371s)** it looks pucker. It looks pucker mate. That's what it looks like to me. I love this app. There's

**[22:57](https://youtube.com/watch?v=rFPbOJc-pQY&t=1377s)** a bunch of other stuff you can do, which I probably order, showed you at the beginning of this video.

**[23:00](https://youtube.com/watch?v=rFPbOJc-pQY&t=1380s)** So I guess we've got one more thing to do. One more thing, Steve Jobs style one more thing. It's

**[23:08](https://youtube.com/watch?v=rFPbOJc-pQY&t=1388s)** not quite that good. But what we can do is we can actually upload and add images via AI. So I tried

**[23:17](https://youtube.com/watch?v=rFPbOJc-pQY&t=1397s)** about an hour, maybe two, to get this working with Olama locally over my town. I tried the FIFI4

**[23:25](https://youtube.com/watch?v=rFPbOJc-pQY&t=1405s)** fee for model. I tried the Quen 2.5 vision learning model as well with Olama locally on this MacBook.

**[23:34](https://youtube.com/watch?v=rFPbOJc-pQY&t=1414s)** And unfortunately, it was just not able to extract the images. So during the pandemic, during

**[23:40](https://youtube.com/watch?v=rFPbOJc-pQY&t=1420s)** COVID, my wife was a subscriber to HelloFresh. In fact, she has a whole, a whole binder full of

**[23:49](https://youtube.com/watch?v=rFPbOJc-pQY&t=1429s)** recipe cards that she's acquired over the years. And so I thought it'd be kind of fun to like

**[23:55](https://youtube.com/watch?v=rFPbOJc-pQY&t=1435s)** digitize them as a project. And so I took a couple of pictures. In fact, let's do that with you now

**[24:02](https://youtube.com/watch?v=rFPbOJc-pQY&t=1442s)** in real time, so to speak. And because these cards are too sided, I'm not sure how well it's

**[24:07](https://youtube.com/watch?v=rFPbOJc-pQY&t=1447s)** going to work because I think image, or image, I think Miele can only process one picture at a time.

**[24:14](https://youtube.com/watch?v=rFPbOJc-pQY&t=1454s)** So I'll just take this one of the of the ingredients right here. And then I'm going to use tail drop

**[24:19](https://youtube.com/watch?v=rFPbOJc-pQY&t=1459s)** to send those pictures from my phone to my computer because they're both logged into the same

**[24:26](https://youtube.com/watch?v=rFPbOJc-pQY&t=1466s)** tailnet. It's actually really easy. So if I click on the select button up there and then I got

**[24:31](https://youtube.com/watch?v=rFPbOJc-pQY&t=1471s)** these two, and I do this, I can then click on the tail scale option right there and select

**[24:37](https://youtube.com/watch?v=rFPbOJc-pQY&t=1477s)** ball trick. That's now going to send those two files from my phone. Yes, technically, it's an

**[24:42](https://youtube.com/watch?v=rFPbOJc-pQY&t=1482s)** iPhone to a MacBook. I could just use air drop. But this would work to any device anywhere in the

**[24:48](https://youtube.com/watch?v=rFPbOJc-pQY&t=1488s)** world over tail scale because tail scales are some. I hope you think I know that by now. But

**[24:55](https://youtube.com/watch?v=rFPbOJc-pQY&t=1495s)** genuinely, before I worked at this company, I was massively into self hosting and you know,

**[25:00](https://youtube.com/watch?v=rFPbOJc-pQY&t=1500s)** doing docker stuff and a podcast in the world of self hosting and all that kind of stuff.

**[25:04](https://youtube.com/watch?v=rFPbOJc-pQY&t=1504s)** And remote access was just a constant pain. It was port forwarding. It was like creating your own

**[25:10](https://youtube.com/watch?v=rFPbOJc-pQY&t=1510s)** hand cranked wire guard configs for a little bit. Open VPN this was just a nightmare. And honestly,

**[25:17](https://youtube.com/watch?v=rFPbOJc-pQY&t=1517s)** now we don't have to worry about any of that with tail scale. So lots of people ask me, Alex, why

**[25:21](https://youtube.com/watch?v=rFPbOJc-pQY&t=1521s)** do you like tail scale so much? And honestly, for me, it's because, well, it sounds like a bit of

**[25:25](https://youtube.com/watch?v=rFPbOJc-pQY&t=1525s)** sales pitch, but it just makes my life easier. And I hope you guys. I hope you find it to make

**[25:31](https://youtube.com/watch?v=rFPbOJc-pQY&t=1531s)** sure lives easier too. So we've sent those images from our phone now to our computer. Let's bring

**[25:37](https://youtube.com/watch?v=rFPbOJc-pQY&t=1537s)** up the finder just to see what's going on. And here they are. In fact, I did some earlier, which I've

**[25:43](https://youtube.com/watch?v=rFPbOJc-pQY&t=1543s)** already rotated. So you can see we've got those. It's a lovely pork katsu recipe, but as you can see,

**[25:49](https://youtube.com/watch?v=rFPbOJc-pQY&t=1549s)** it's a double sided thing. So what I'm going to do is just bring up me Lee now, and I'm going to

**[25:56](https://youtube.com/watch?v=rFPbOJc-pQY&t=1556s)** click on create, create from image, and then I'm going to upload the, well, I should probably do

**[26:01](https://youtube.com/watch?v=rFPbOJc-pQY&t=1561s)** the backside because that's the one that's got all of the instructions on it. And now it's going

**[26:06](https://youtube.com/watch?v=rFPbOJc-pQY&t=1566s)** to go out to open API, which I generated an API key for at platform. Open API.com API keys. So I

**[26:16](https://youtube.com/watch?v=rFPbOJc-pQY&t=1576s)** actually did this as a test earlier, and it used 4,700 tokens, which cost me 1 cent. So if you

**[26:24](https://youtube.com/watch?v=rFPbOJc-pQY&t=1584s)** worried about racking up a huge bill here, I mean, I limit this to $10 a month, and you can see I'm

**[26:28](https://youtube.com/watch?v=rFPbOJc-pQY&t=1588s)** nowhere near. This will be when I was trying out Karakeep the other day too, I assume. So if you

**[26:33](https://youtube.com/watch?v=rFPbOJc-pQY&t=1593s)** want to generate yourself an open API key, do that and put it into your compose YAML file,

**[26:38](https://youtube.com/watch?v=rFPbOJc-pQY&t=1598s)** like so, and then Mealy will detect that automatically in its environment variables, and then you can

**[26:43](https://youtube.com/watch?v=rFPbOJc-pQY&t=1603s)** click on create. Now I'm going to bring up, yeah, in fact, if we leave that terminal window,

**[26:56](https://youtube.com/watch?v=rFPbOJc-pQY&t=1616s)** now it did take some time to process this earlier, maybe a minute or two. So it's not done

**[27:04](https://youtube.com/watch?v=rFPbOJc-pQY&t=1624s)** a perfect job because the ingredients are sort of laid out without quantities and stuff.

**[27:10](https://youtube.com/watch?v=rFPbOJc-pQY&t=1630s)** The ingredients on the front are perfect. Like, if Mealy, if you're watching this, if you can make

**[27:14](https://youtube.com/watch?v=rFPbOJc-pQY&t=1634s)** it, so I cut up two images, that would be the move right there. But you can see it's got all the

**[27:21](https://youtube.com/watch?v=rFPbOJc-pQY&t=1641s)** ingredients. It just hasn't got the quantities quite right, but if you're looking to just sort of

**[27:26](https://youtube.com/watch?v=rFPbOJc-pQY&t=1646s)** digitize things, like you could go in and modify these ingredients if you want to, or indeed,

**[27:31](https://youtube.com/watch?v=rFPbOJc-pQY&t=1651s)** probably something that just occurred to me, probably threaten to chat GPT in the first place,

**[27:35](https://youtube.com/watch?v=rFPbOJc-pQY&t=1655s)** and then get the ingredients into a format that Mealy would like. Well there you go. I mean,

**[27:41](https://youtube.com/watch?v=rFPbOJc-pQY&t=1661s)** I know the AI stuff at the end was a little bit of a digression. But really, this app is,

**[27:46](https://youtube.com/watch?v=rFPbOJc-pQY&t=1666s)** it's one that you probably lose an evening to messing about with finding all the little features

**[27:50](https://youtube.com/watch?v=rFPbOJc-pQY&t=1670s)** and little nooks and crannies where they've hidden stuff. And just the ability of like how to

**[27:55](https://youtube.com/watch?v=rFPbOJc-pQY&t=1675s)** smoke a brisket, you know, be able to go to any website. Yes, ads. More ads.

**[28:06](https://youtube.com/watch?v=rFPbOJc-pQY&t=1686s)** But the ability of just being able to go to any website and then just paste in the URL,

**[28:12](https://youtube.com/watch?v=rFPbOJc-pQY&t=1692s)** for me, that alone makes this, this self-hosted application an absolute keeper. Like, you own

**[28:18](https://youtube.com/watch?v=rFPbOJc-pQY&t=1698s)** the data until the end of time, like this is yours, you will always own this data. So even if,

**[28:24](https://youtube.com/watch?v=rFPbOJc-pQY&t=1704s)** even if smokedmeatsunday.com goes away, you've now got, I know you could print this out also,

**[28:31](https://youtube.com/watch?v=rFPbOJc-pQY&t=1711s)** you've kind of owned that forever too. But sometimes it is better to just have your phone.

**[28:36](https://youtube.com/watch?v=rFPbOJc-pQY&t=1716s)** Sometimes it's better to just have a tablet, whatever. Not sure if I'll get this app into production

**[28:41](https://youtube.com/watch?v=rFPbOJc-pQY&t=1721s)** in this household, but I'm, I'm trying. I'm fighting the good fight. So there you go. That's how

**[28:46](https://youtube.com/watch?v=rFPbOJc-pQY&t=1726s)** you deploy Mealy and put it on your tailnet. Thank you so much for watching. And until next time,

**[28:50](https://youtube.com/watch?v=rFPbOJc-pQY&t=1730s)** I've been Alex from TaleScale.

---

*Automatically generated transcript. May contain errors.*
