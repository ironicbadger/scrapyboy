---
video_id: "5lJrXEXF8eM"
title: "No more docker sidecars! TSDProxy for Tailscale"
description: "In today's video we feature an awesome project by one of our community members. TSDProxy is a simple way to access your Tailscale services running docker without creating an individual sidecar contain..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-11-26"
duration_seconds: 559
youtube_url: "https://www.youtube.com/watch?v=5lJrXEXF8eM"
thumbnail_url: "https://i.ytimg.com/vi_webp/5lJrXEXF8eM/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T15:58:04.815992"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1828
transcription_time_seconds: 15.9
---

# No more docker sidecars! TSDProxy for Tailscale

**[00:00](https://youtube.com/watch?v=5lJrXEXF8eM&t=0s)** So I was browsing Reddit the other day, and I came across this app called TSD Proxy. This

**[00:05](https://youtube.com/watch?v=5lJrXEXF8eM&t=5s)** purports to be the easiest way to add applications to your tailnet. No more sidecar containers,

**[00:11](https://youtube.com/watch?v=5lJrXEXF8eM&t=11s)** just a couple of labels on your Docker Compose file. What's not to like? In today's video,

**[00:15](https://youtube.com/watch?v=5lJrXEXF8eM&t=15s)** we're going to jump into setting up TSD Proxy on your tailnet. So what exactly is TSD Proxy?

**[00:24](https://youtube.com/watch?v=5lJrXEXF8eM&t=24s)** You can think of it a little bit like a simple reverse proxy for your tailnet. Now,

**[00:28](https://youtube.com/watch?v=5lJrXEXF8eM&t=28s)** caveat time, this is a community project and it's not an officially sanctioned tailscale

**[00:33](https://youtube.com/watch?v=5lJrXEXF8eM&t=33s)** solution. However, I think it's really cool and I wanted to share it with you today.

**[00:38](https://youtube.com/watch?v=5lJrXEXF8eM&t=38s)** So what we would recommend on the tailscale side is one container so it could be sterling

**[00:44](https://youtube.com/watch?v=5lJrXEXF8eM&t=44s)** PDF, for example, and then a sidecar container running tailscale. You then merge those together

**[00:49](https://youtube.com/watch?v=5lJrXEXF8eM&t=49s)** underneath so that they can actually talk to each other and sterling PDF appears on your tailnet.

**[00:55](https://youtube.com/watch?v=5lJrXEXF8eM&t=55s)** Now that works fine, but the downside is you've got one container extra per service that you want

**[01:00](https://youtube.com/watch?v=5lJrXEXF8eM&t=60s)** to run. Now each tailscale sidecar only takes about 20 to 30 megabytes to run, but for some people,

**[01:06](https://youtube.com/watch?v=5lJrXEXF8eM&t=66s)** that's too much bloke. And if that's you, and actually if you just like simplicity,

**[01:10](https://youtube.com/watch?v=5lJrXEXF8eM&t=70s)** then TSD Proxy might be the solution for you. So rather than having a sidecar container per service,

**[01:17](https://youtube.com/watch?v=5lJrXEXF8eM&t=77s)** TSD Proxy is actually just a service in and of itself. It listens to the Docker socket on a

**[01:23](https://youtube.com/watch?v=5lJrXEXF8eM&t=83s)** specific Docker host and then it routes all the traffic around using Docker networking internally

**[01:29](https://youtube.com/watch?v=5lJrXEXF8eM&t=89s)** on that host. So if you have multiple Docker hosts, you're going to need one of these TSD proxy

**[01:34](https://youtube.com/watch?v=5lJrXEXF8eM&t=94s)** instances per host, but rather than having one sidecar container per service, you've just got TSD

**[01:41](https://youtube.com/watch?v=5lJrXEXF8eM&t=101s)** proxy per host. Under the covers, TSD proxy uses something called TSnet. This is a way to bake

**[01:47](https://youtube.com/watch?v=5lJrXEXF8eM&t=107s)** tailscale directly into the source code of your applications. And so essentially what this software

**[01:53](https://youtube.com/watch?v=5lJrXEXF8eM&t=113s)** does is it automatically notices a new container appears on the Docker socket and adds that as a node

**[02:00](https://youtube.com/watch?v=5lJrXEXF8eM&t=120s)** automatically to your tailnet using go code. All you need to do is provide an auth key

**[02:06](https://youtube.com/watch?v=5lJrXEXF8eM&t=126s)** and TSD proxy kind of just handles the rest. And so if we take a look at my screen over here,

**[02:10](https://youtube.com/watch?v=5lJrXEXF8eM&t=130s)** we can see that I have a Docker compose file loaded up in VS code. This is using the tailscale

**[02:16](https://youtube.com/watch?v=5lJrXEXF8eM&t=136s)** VS code extension to edit a file directly on a node on my tailnet. In this case, I've got a node

**[02:22](https://youtube.com/watch?v=5lJrXEXF8eM&t=142s)** on my tailnet called TSD proxy itself. I've also installed tailscale on that node. If you're

**[02:27](https://youtube.com/watch?v=5lJrXEXF8eM&t=147s)** curious of how I'm running that, I'm just using an LXC container on top of Proxmox and running a

**[02:32](https://youtube.com/watch?v=5lJrXEXF8eM&t=152s)** Ubuntu server. Nothing too fancy going on here. So underneath, I have a fairly standard Docker

**[02:39](https://youtube.com/watch?v=5lJrXEXF8eM&t=159s)** compose YAML file. I have Sterling PDF. I have an audiobook server using audiobook shelf. And

**[02:47](https://youtube.com/watch?v=5lJrXEXF8eM&t=167s)** my absolute favorite app at the moment, searching for a self-hosted privacy respecting meta-search

**[02:52](https://youtube.com/watch?v=5lJrXEXF8eM&t=172s)** engine. You can check the card up here for my latest video about Search XNG. You may have noticed

**[02:58](https://youtube.com/watch?v=5lJrXEXF8eM&t=178s)** that in this file, there are just a couple of labels enabled. This is how TSD proxy knows what to

**[03:06](https://youtube.com/watch?v=5lJrXEXF8eM&t=186s)** do with your application because it's listening to the Docker socket. And by that, I mean this line

**[03:10](https://youtube.com/watch?v=5lJrXEXF8eM&t=190s)** here. So line 16, the Docker host. You actually mount the Docker socket. And this is where Docker

**[03:16](https://youtube.com/watch?v=5lJrXEXF8eM&t=196s)** publishes everything that is doing because everything in Linux is just a file after all. It says,

**[03:21](https://youtube.com/watch?v=5lJrXEXF8eM&t=201s)** I've just created this new container with all of this metadata. So whenever you do a Docker

**[03:25](https://youtube.com/watch?v=5lJrXEXF8eM&t=205s)** inspect on a container and it prints out that huge list of information, that's the stuff that's

**[03:30](https://youtube.com/watch?v=5lJrXEXF8eM&t=210s)** getting published to the Docker socket. And all TSD proxy is doing is listening to that list of

**[03:36](https://youtube.com/watch?v=5lJrXEXF8eM&t=216s)** stuff that's going by and says, oh, I'm going to check out that label that says TSD proxy.enable

**[03:42](https://youtube.com/watch?v=5lJrXEXF8eM&t=222s)** equals true. You can also then give it a custom name in my case. I've named Sterling PDF,

**[03:47](https://youtube.com/watch?v=5lJrXEXF8eM&t=227s)** a different name from the service itself. So TSD proxy.name is now PDF. And so on and so forth.

**[03:55](https://youtube.com/watch?v=5lJrXEXF8eM&t=235s)** You can see I've got books here for audio books and then searches again, just search here.

**[03:59](https://youtube.com/watch?v=5lJrXEXF8eM&t=239s)** So how hard does it to actually get started with this thing? Turns out, not very. Just a few lines

**[04:05](https://youtube.com/watch?v=5lJrXEXF8eM&t=245s)** of Docker compose YAML and you can spin up the TSD proxy image. You do want to make sure you've

**[04:10](https://youtube.com/watch?v=5lJrXEXF8eM&t=250s)** got a little bit of persistence here. So I have a Docker volume defined on slash data.

**[04:15](https://youtube.com/watch?v=5lJrXEXF8eM&t=255s)** You can find a link to this Docker compose file by the way in the description down below.

**[04:19](https://youtube.com/watch?v=5lJrXEXF8eM&t=259s)** And then we want to generate an auth key. We've done this a few times on the channel,

**[04:22](https://youtube.com/watch?v=5lJrXEXF8eM&t=262s)** but just for the sake of completeness, if you go to tailscale.com and make sure that you're logged

**[04:27](https://youtube.com/watch?v=5lJrXEXF8eM&t=267s)** in, go to admin console and then go to settings. When you're there, go to personal settings down

**[04:33](https://youtube.com/watch?v=5lJrXEXF8eM&t=273s)** here on the bottom left and click on keys. You'll then want to generate an auth key. In my case,

**[04:38](https://youtube.com/watch?v=5lJrXEXF8eM&t=278s)** it doesn't, the name and description doesn't really matter. You know, I can call it blah, blah, whatever.

**[04:43](https://youtube.com/watch?v=5lJrXEXF8eM&t=283s)** Reusable. You might want to do that for this one because TSD proxy is going to be spinning things up

**[04:48](https://youtube.com/watch?v=5lJrXEXF8eM&t=288s)** and taking them down all the time. You also might want to consider ephemeral. Normally, I leave

**[04:54](https://youtube.com/watch?v=5lJrXEXF8eM&t=294s)** these options alone, but here today, ephemeral is quite useful because as you spin up a new service

**[04:59](https://youtube.com/watch?v=5lJrXEXF8eM&t=299s)** and a new container, it will add it automatically to your tailnet, but it won't clean it up. Whereas if

**[05:05](https://youtube.com/watch?v=5lJrXEXF8eM&t=305s)** you have an ephemeral setting set on the auth key that you're generating, the containers will clean

**[05:11](https://youtube.com/watch?v=5lJrXEXF8eM&t=311s)** themselves up after a few minutes of being inactive on your tailnet. Once you've generated that key,

**[05:17](https://youtube.com/watch?v=5lJrXEXF8eM&t=317s)** simply copy it to your clipboard and then just paste it into the Docker Compose YAML file that's

**[05:21](https://youtube.com/watch?v=5lJrXEXF8eM&t=321s)** here and press save. Then it should just be a case of making sure that you're in the correct

**[05:27](https://youtube.com/watch?v=5lJrXEXF8eM&t=327s)** directory. Now, I'm connected to this host over tailscale SSH and you can see I have my

**[05:32](https://youtube.com/watch?v=5lJrXEXF8eM&t=332s)** Compose.YAML file sat right here in the base of my home directory. I'm going to do a Docker

**[05:38](https://youtube.com/watch?v=5lJrXEXF8eM&t=338s)** Compose pull. This is the first thing that I like to do on a remote host just to get the latest

**[05:43](https://youtube.com/watch?v=5lJrXEXF8eM&t=343s)** fresh images down from Docker Hub or whichever Docker registry you're using these days.

**[05:47](https://youtube.com/watch?v=5lJrXEXF8eM&t=347s)** Once that's done, we can do a very simple Docker Compose up minus D. When we do that,

**[05:53](https://youtube.com/watch?v=5lJrXEXF8eM&t=353s)** I want to jump back to my tailnet real quick because you'll notice that right away look

**[05:59](https://youtube.com/watch?v=5lJrXEXF8eM&t=359s)** books is now added and connected. PDF is now added and connected and so is search. If I want to

**[06:06](https://youtube.com/watch?v=5lJrXEXF8eM&t=366s)** go to any of these domain names, I can just click and copy this to my clipboard here, the fully

**[06:10](https://youtube.com/watch?v=5lJrXEXF8eM&t=370s)** qualified domain name. Make sure I'm going to HTTPS. It's going to generate a new certificate the

**[06:16](https://youtube.com/watch?v=5lJrXEXF8eM&t=376s)** first time. I've already done this in a demo but if this is the first time you're loading this

**[06:21](https://youtube.com/watch?v=5lJrXEXF8eM&t=381s)** service, it might take up to 30 seconds to load for the first time depending on how busy

**[06:27](https://youtube.com/watch?v=5lJrXEXF8eM&t=387s)** Let's Encrypt is because we're generating these certificates on an as needed basis rather than

**[06:31](https://youtube.com/watch?v=5lJrXEXF8eM&t=391s)** just spamming the Let's Encrypt API every time. But as you can see, look, that's it. This service

**[06:37](https://youtube.com/watch?v=5lJrXEXF8eM&t=397s)** is now on my tailnet. It's so simple to get started compared to the sidecar container approach

**[06:43](https://youtube.com/watch?v=5lJrXEXF8eM&t=403s)** where you had to do multiple containers and I actually really prefer this option. I know it's

**[06:48](https://youtube.com/watch?v=5lJrXEXF8eM&t=408s)** not the officially supported route to go but I think I'm going to be converting all of my TSNET

**[06:54](https://youtube.com/watch?v=5lJrXEXF8eM&t=414s)** Docker containers to using TSD proxy after taking a look at this. Let's just go over some of the

**[07:00](https://youtube.com/watch?v=5lJrXEXF8eM&t=420s)** stuff you can actually do with TSD proxy one more time. Notice here that I have Enable is true

**[07:05](https://youtube.com/watch?v=5lJrXEXF8eM&t=425s)** and the name is PDF. But if we take a look at the TSD proxy documentation, you can see there's quite

**[07:10](https://youtube.com/watch?v=5lJrXEXF8eM&t=430s)** a few other bells and whistles that we can do. Things like ephemeral, for example, now I said in

**[07:16](https://youtube.com/watch?v=5lJrXEXF8eM&t=436s)** your auth key, you had to define ephemeral, you can also just define it here as a label on the container

**[07:22](https://youtube.com/watch?v=5lJrXEXF8eM&t=442s)** itself if you would prefer. Now, if you have a so TSD proxy is looking at the default port and

**[07:28](https://youtube.com/watch?v=5lJrXEXF8eM&t=448s)** this is what is exposed in the Docker file using the exposed command. It's a very boring implementation

**[07:34](https://youtube.com/watch?v=5lJrXEXF8eM&t=454s)** detail but if for some reason this doesn't pick the correct port of the service that you're trying

**[07:38](https://youtube.com/watch?v=5lJrXEXF8eM&t=458s)** to proxy, you can actually explicitly define a port here using the container port variable.

**[07:43](https://youtube.com/watch?v=5lJrXEXF8eM&t=463s)** Now there are a bunch more interesting configuration options in this services configuration documentation.

**[07:48](https://youtube.com/watch?v=5lJrXEXF8eM&t=468s)** I'll put a link to that in the description down below, of course. A couple of things I want to

**[07:52](https://youtube.com/watch?v=5lJrXEXF8eM&t=472s)** point out to you. Tailscale funnel, which is a way of putting these containers directly onto

**[07:57](https://youtube.com/watch?v=5lJrXEXF8eM&t=477s)** the public internet, is as simple as enabling that with one line of configuration. In the labels,

**[08:02](https://youtube.com/watch?v=5lJrXEXF8eM&t=482s)** stands are just here. TSD proxy.funnel equals true. Now, under the advanced section in the documentation,

**[08:08](https://youtube.com/watch?v=5lJrXEXF8eM&t=488s)** there's a couple of things I tried doing the research for this video that I was wanting to make

**[08:12](https://youtube.com/watch?v=5lJrXEXF8eM&t=492s)** you aware of that might still need a little more time in the oven. The first of which is the

**[08:17](https://youtube.com/watch?v=5lJrXEXF8eM&t=497s)** dashboard. It even says on the web page here, it's still in very early stages of development.

**[08:22](https://youtube.com/watch?v=5lJrXEXF8eM&t=502s)** I couldn't get my dashboard to load. Also, Docker secrets. For some reason, the auth key file option

**[08:27](https://youtube.com/watch?v=5lJrXEXF8eM&t=507s)** here that's required to use the Docker secrets option doesn't seem to work yet either and has been

**[08:33](https://youtube.com/watch?v=5lJrXEXF8eM&t=513s)** reported on the project's GitHub. So hopefully that this will be fixed fairly soon. Also, I want to

**[08:38](https://youtube.com/watch?v=5lJrXEXF8eM&t=518s)** draw your attention to the fact you can use headscale with this. So if you're using the self-hosted

**[08:42](https://youtube.com/watch?v=5lJrXEXF8eM&t=522s)** tailscale control server project called headscale, then you can do that by inputting your custom URL

**[08:48](https://youtube.com/watch?v=5lJrXEXF8eM&t=528s)** here. Also, if you're using a service with a network mode of host, there's a couple of options

**[08:53](https://youtube.com/watch?v=5lJrXEXF8eM&t=533s)** here just for you as well. I just wanted to take a second and say thank you very much to Paolo

**[08:58](https://youtube.com/watch?v=5lJrXEXF8eM&t=538s)** Almeda, who is the awesome community member who, over on GitHub, made this project possible.

**[09:04](https://youtube.com/watch?v=5lJrXEXF8eM&t=544s)** Of course, if you want to embed tailscale directly into your applications, like Paolo did,

**[09:08](https://youtube.com/watch?v=5lJrXEXF8eM&t=548s)** you can have a look at the TSNet documentation for our API linked in the description down below.

**[09:14](https://youtube.com/watch?v=5lJrXEXF8eM&t=554s)** Until next time, thank you so much for watching. I've been Alex from Tailscale.

---

*Automatically generated transcript. May contain errors.*
