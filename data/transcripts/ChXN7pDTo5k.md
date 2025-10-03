---
video_id: "ChXN7pDTo5k"
title: "Monitor anything from anywhere with Prometheus, Grafana and Tailscale"
description: "In today's video Alex shows you how to monitor a UPS on the other side of the planet using Prometheus, Tailscale and Grafana.

Personal accounts are always free on Tailscale and can include up to 3 us..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-10-11"
duration_seconds: 832
youtube_url: "https://www.youtube.com/watch?v=ChXN7pDTo5k"
thumbnail_url: "https://i.ytimg.com/vi/ChXN7pDTo5k/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:38:14.883059"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2470
transcription_time_seconds: 22.2
---

# Monitor anything from anywhere with Prometheus, Grafana and Tailscale

**[00:00](https://youtube.com/watch?v=ChXN7pDTo5k&t=0s)** Now if anything like me, you probably love a good graph. In today's video we're going

**[00:04](https://youtube.com/watch?v=ChXN7pDTo5k&t=4s)** to look at Prometheus and Grafala. Prometheus is a time series database-based monitoring

**[00:11](https://youtube.com/watch?v=ChXN7pDTo5k&t=11s)** tool. What it does is every few seconds is it reaches out and scrapes a remote HTTP

**[00:16](https://youtube.com/watch?v=ChXN7pDTo5k&t=16s)** target for a bunch of monitoring information. In our case, I need to monitor a UPS that

**[00:22](https://youtube.com/watch?v=ChXN7pDTo5k&t=22s)** I just added to my UK backup server. I'm going to connect the two together, using, of

**[00:27](https://youtube.com/watch?v=ChXN7pDTo5k&t=27s)** course, Tailscale. Prometheus is running here in my home lab in Raleigh, and the node

**[00:32](https://youtube.com/watch?v=ChXN7pDTo5k&t=32s)** exporter for APS UPSD is running on my backup server in Norfolk in England. So we often

**[00:40](https://youtube.com/watch?v=ChXN7pDTo5k&t=40s)** say around these parts that Tailscale is the easiest way to connect your devices and

**[00:43](https://youtube.com/watch?v=ChXN7pDTo5k&t=43s)** services together, and indeed that's what I'm going to show you today. So I'm connected

**[00:50](https://youtube.com/watch?v=ChXN7pDTo5k&t=50s)** into my remote UK server using Tailscale SSH. You can find a link to a video about Tailscale

**[00:55](https://youtube.com/watch?v=ChXN7pDTo5k&t=55s)** SSH just up here. This means I don't need to manage SSH keys or worry about DNS or any

**[01:00](https://youtube.com/watch?v=ChXN7pDTo5k&t=60s)** of that kind of stuff. Tailscale just handles it all for me. Now I've connected via USB

**[01:05](https://youtube.com/watch?v=ChXN7pDTo5k&t=65s)** the APC UPS device to Snowball, and I can see that if I type LSUSB, I've got the American

**[01:12](https://youtube.com/watch?v=ChXN7pDTo5k&t=72s)** power conversion uninterruptible power supply. Now you can find a demon that will allow

**[01:17](https://youtube.com/watch?v=ChXN7pDTo5k&t=77s)** you to monitor and actually access the data that that USB connection is providing, and

**[01:22](https://youtube.com/watch?v=ChXN7pDTo5k&t=82s)** we can install that with a simple sudo app install APC UPSD. That's going to pull down

**[01:29](https://youtube.com/watch?v=ChXN7pDTo5k&t=89s)** a few packages. Now I'm running all of these commands on top of Proxmox. You might need

**[01:32](https://youtube.com/watch?v=ChXN7pDTo5k&t=92s)** to adjust a few things if you are running a different OS. Now you might notice here that

**[01:37](https://youtube.com/watch?v=ChXN7pDTo5k&t=97s)** I've already got an error message saying that I cannot communicate with the UPS. And that's

**[01:41](https://youtube.com/watch?v=ChXN7pDTo5k&t=101s)** because we need to configure the UPS demon to be able to connect to the device over USB.

**[01:47](https://youtube.com/watch?v=ChXN7pDTo5k&t=107s)** So I'm going to bring up VIM using sudo, VIM, ETC, APC, UPSD, APC, UPSD.conf. And in this

**[01:58](https://youtube.com/watch?v=ChXN7pDTo5k&t=118s)** file, I'm going to make just a couple of small edits. I'm going to give the UPS a name.

**[02:02](https://youtube.com/watch?v=ChXN7pDTo5k&t=122s)** This will make it easier in our queries later on in Prometheus. I'm just going to call

**[02:06](https://youtube.com/watch?v=ChXN7pDTo5k&t=126s)** this APC UPSNR. Maybe I should call it Snowball. How about that? I'm going to call it Snowball.

**[02:15](https://youtube.com/watch?v=ChXN7pDTo5k&t=135s)** I also need to modify there is a line somewhere down here that talks about connecting through

**[02:21](https://youtube.com/watch?v=ChXN7pDTo5k&t=141s)** a serial console. Just need to comment that out. Yeah, here we are. I think all I need

**[02:26](https://youtube.com/watch?v=ChXN7pDTo5k&t=146s)** to do is just remove this one line just here. And then restart, again using sudo, sudo system

**[02:33](https://youtube.com/watch?v=ChXN7pDTo5k&t=153s)** CTL, restart, APC, UPSD. Now if I type sudo, APC, access, I should be able to connect to

**[02:42](https://youtube.com/watch?v=ChXN7pDTo5k&t=162s)** all of the information that's being exposed to this host via the USB connection and the

**[02:48](https://youtube.com/watch?v=ChXN7pDTo5k&t=168s)** demon that we just installed. You can see the battery charge here is 100% at the current

**[02:53](https://youtube.com/watch?v=ChXN7pDTo5k&t=173s)** power usage levels. It reckons it's got about 50 minutes of runtime. The line voltage is

**[02:58](https://youtube.com/watch?v=ChXN7pDTo5k&t=178s)** 241 volts. And the backup modeling question, just in case you're curious, is the BX950MI.

**[03:05](https://youtube.com/watch?v=ChXN7pDTo5k&t=185s)** And so that's all the configuration that's required to get the host to talk to the actual physical

**[03:10](https://youtube.com/watch?v=ChXN7pDTo5k&t=190s)** UPS device over USB. You can just take a quick look at the APC UPSD service here and just have a

**[03:17](https://youtube.com/watch?v=ChXN7pDTo5k&t=197s)** look at what's going on. If you want to make any modifications, you can just modify this file over here

**[03:21](https://youtube.com/watch?v=ChXN7pDTo5k&t=201s)** to suit your needs for things like shutdown parameters and certain percentages to trigger shutdowns,

**[03:27](https://youtube.com/watch?v=ChXN7pDTo5k&t=207s)** that kind of thing. Next up, we're going to rely on a project from GitHub called APC UPSD

**[03:33](https://youtube.com/watch?v=ChXN7pDTo5k&t=213s)** exporter. And I'll be a link to this in the description down below, of course. We need to clone

**[03:39](https://youtube.com/watch?v=ChXN7pDTo5k&t=219s)** this Git repo, which is a fairly straightforward process these days. We click on the big green button

**[03:43](https://youtube.com/watch?v=ChXN7pDTo5k&t=223s)** up here and copy the URL to our clipboard. I'm going to make a directory called Git in the home

**[03:51](https://youtube.com/watch?v=ChXN7pDTo5k&t=231s)** directory of this particular user and then do git clone APC UPSD exporter. Git. Then I'm going

**[03:59](https://youtube.com/watch?v=ChXN7pDTo5k&t=239s)** to change into that directory. And I need to also make sure that I've got Go installed on this

**[04:04](https://youtube.com/watch?v=ChXN7pDTo5k&t=244s)** box as well. So I'm going to do sudo apt install go lang. And it's going to go out and fetch the

**[04:09](https://youtube.com/watch?v=ChXN7pDTo5k&t=249s)** latest dependencies. Now I already did this before I started recording the video. If you didn't,

**[04:14](https://youtube.com/watch?v=ChXN7pDTo5k&t=254s)** you'll need to make sure that Go is installed with that command. Next, we need to build the binary

**[04:19](https://youtube.com/watch?v=ChXN7pDTo5k&t=259s)** itself. And we do this with the following command, go build dot slash command slash APCD, APC UPSD

**[04:27](https://youtube.com/watch?v=ChXN7pDTo5k&t=267s)** underscore exporter. This is going to build us the statically compiled binary that we actually need

**[04:32](https://youtube.com/watch?v=ChXN7pDTo5k&t=272s)** to run. Next, this gets deposited in the root of the Git repo and we can run it with a dot slash

**[04:39](https://youtube.com/watch?v=ChXN7pDTo5k&t=279s)** and then the name of the binary itself. And you'll see that we now have an HTTP server running

**[04:44](https://youtube.com/watch?v=ChXN7pDTo5k&t=284s)** on port 9162. So what we can do now is grab the IP address of our host. So I'm going to go up to my

**[04:53](https://youtube.com/watch?v=ChXN7pDTo5k&t=293s)** devices, get snowballs, IP address, paste this in here and it was 9162. And we can see this is how

**[05:02](https://youtube.com/watch?v=ChXN7pDTo5k&t=302s)** the Prometheus exporter, the node exporter, presents information to Prometheus. So what Prometheus

**[05:08](https://youtube.com/watch?v=ChXN7pDTo5k&t=308s)** will do, we're going to configure that in a minute, it will reach out to this HTTP endpoint over

**[05:14](https://youtube.com/watch?v=ChXN7pDTo5k&t=314s)** tail scale and scrape all of this information every 30 seconds, every 60 seconds or so. We can

**[05:21](https://youtube.com/watch?v=ChXN7pDTo5k&t=321s)** then put that information into Grafana to create our graphs. Now at the present time, this HTTP

**[05:27](https://youtube.com/watch?v=ChXN7pDTo5k&t=327s)** server is running in the foreground. Long term, that won't do. So we need to create ourselves a

**[05:33](https://youtube.com/watch?v=ChXN7pDTo5k&t=333s)** system D unit file. We're going to put this under Etsy system D system and then APC UPSD.

**[05:42](https://youtube.com/watch?v=ChXN7pDTo5k&t=342s)** I feel like I've said that for you. You know when a word becomes a sound, that's kind of where I

**[05:47](https://youtube.com/watch?v=ChXN7pDTo5k&t=347s)** am with that right now. APC UPSD underscore exporter dot service. Then we're going to create the

**[05:54](https://youtube.com/watch?v=ChXN7pDTo5k&t=354s)** following unit file and just take note of this path user local bin and then the name of the binary.

**[06:00](https://youtube.com/watch?v=ChXN7pDTo5k&t=360s)** We're going to write and quit that file and then I'm going to move the binary that we built

**[06:05](https://youtube.com/watch?v=ChXN7pDTo5k&t=365s)** underscore exporter to user local bin as pseudo, of course. And so now if we do a pseudo system CTL

**[06:17](https://youtube.com/watch?v=ChXN7pDTo5k&t=377s)** demon reload, we can then do again, we can do start APC UPSD underscore exporter dash dash now. I'm

**[06:28](https://youtube.com/watch?v=ChXN7pDTo5k&t=388s)** actually going to change the word start to enable so that it both starts and enables the service

**[06:34](https://youtube.com/watch?v=ChXN7pDTo5k&t=394s)** right here and now. And so if I go to this URL, we should see that the metrics are now running

**[06:39](https://youtube.com/watch?v=ChXN7pDTo5k&t=399s)** in the background as a system D service. So the next step is going to be to configure Prometheus

**[06:45](https://youtube.com/watch?v=ChXN7pDTo5k&t=405s)** on the remote side. Now I'm using VS code here to access the node that's going to be running Prometheus

**[06:51](https://youtube.com/watch?v=ChXN7pDTo5k&t=411s)** in my tailnet. Just happens to be called Prometheus, funnily enough. And in the root of this user's

**[06:57](https://youtube.com/watch?v=ChXN7pDTo5k&t=417s)** home folder, I've put a folder called compose.yaml. In here, I've defined a couple of containers.

**[07:03](https://youtube.com/watch?v=ChXN7pDTo5k&t=423s)** The first of them you might expect is Prometheus and the second one is Grafana. So just a reminder,

**[07:09](https://youtube.com/watch?v=ChXN7pDTo5k&t=429s)** Prometheus is what's going to reach out and do the scraping from here in Raleigh over the tail

**[07:14](https://youtube.com/watch?v=ChXN7pDTo5k&t=434s)** scale tunnel that we have underneath to the server running in England running APC UPSD.

**[07:20](https://youtube.com/watch?v=ChXN7pDTo5k&t=440s)** And then Grafana will talk locally on the Prometheus box to Prometheus and query it for data to

**[07:26](https://youtube.com/watch?v=ChXN7pDTo5k&t=446s)** present it as a pretty graph based front end. So let's take a look at the configuration that's

**[07:32](https://youtube.com/watch?v=ChXN7pDTo5k&t=452s)** required for Prometheus first of all. Spinning up the container is really easy and there'll be

**[07:37](https://youtube.com/watch?v=ChXN7pDTo5k&t=457s)** code snippets in a link down below to a git repo that I have for all of the materials that you're

**[07:42](https://youtube.com/watch?v=ChXN7pDTo5k&t=462s)** going to need for today's video. The second file you're going to need to look at is this one that

**[07:47](https://youtube.com/watch?v=ChXN7pDTo5k&t=467s)** goes in opt apt data Prometheus. You can see I've got that mounted here as a volume

**[07:52](https://youtube.com/watch?v=ChXN7pDTo5k&t=472s)** to replace the volume of slash ETC Prometheus inside the container. Now this is where we define

**[07:58](https://youtube.com/watch?v=ChXN7pDTo5k&t=478s)** the target scrape configuration. You can see that I've got two targets configured here. The first

**[08:05](https://youtube.com/watch?v=ChXN7pDTo5k&t=485s)** of which is to scrape Prometheus itself. And then the second is to scrape my UPS. Now you may

**[08:11](https://youtube.com/watch?v=ChXN7pDTo5k&t=491s)** not know this, but this particular subnet here is the remote subnet in England. 192.16.10.

**[08:19](https://youtube.com/watch?v=ChXN7pDTo5k&t=499s)** So I've currently got this configured to be scraping that remote host over a subnet router.

**[08:24](https://youtube.com/watch?v=ChXN7pDTo5k&t=504s)** Even though Snowball is actually on my tailnet as well, I could just as easily replace this with

**[08:29](https://youtube.com/watch?v=ChXN7pDTo5k&t=509s)** the 100.ip address if I wanted to. But I was doing some testing before the video and it sort of

**[08:34](https://youtube.com/watch?v=ChXN7pDTo5k&t=514s)** occurred to me. Maybe that would be a nice thing to show everybody here is that you can scrape devices

**[08:40](https://youtube.com/watch?v=ChXN7pDTo5k&t=520s)** that aren't even on the tailnet by using subnet routing functionality as well. Just it's one of those

**[08:46](https://youtube.com/watch?v=ChXN7pDTo5k&t=526s)** things that like I said in the intro, tail scale is the easiest way to connect to devices and

**[08:51](https://youtube.com/watch?v=ChXN7pDTo5k&t=531s)** services together. And this is exactly what we mean by that. So once we have everything configured

**[08:57](https://youtube.com/watch?v=ChXN7pDTo5k&t=537s)** in terms of the Docker compose file and the configuration that needs to be put in place for

**[09:02](https://youtube.com/watch?v=ChXN7pDTo5k&t=542s)** Prometheus itself, it's time to go and spin these things up. So I'm going to do a Docker compose.

**[09:09](https://youtube.com/watch?v=ChXN7pDTo5k&t=549s)** By the way, this terminal window is logged in via SSH to the Prometheus box. I'm not running

**[09:13](https://youtube.com/watch?v=ChXN7pDTo5k&t=553s)** this on my local laptop or anything like that. I'm going to do Docker compose up and it's going to

**[09:18](https://youtube.com/watch?v=ChXN7pDTo5k&t=558s)** pull down the Grafana and the Prometheus containers as well. So now, if I go to Prometheus,

**[09:28](https://youtube.com/watch?v=ChXN7pDTo5k&t=568s)** I think it runs on port 9090 by default. You can see I'm able to use the host name here to connect

**[09:33](https://youtube.com/watch?v=ChXN7pDTo5k&t=573s)** and then port 9090. And I'm connected now into the Prometheus instance that we just created in

**[09:38](https://youtube.com/watch?v=ChXN7pDTo5k&t=578s)** the container. So if I now jump over to the status tab up here and just have a quick look at the

**[09:43](https://youtube.com/watch?v=ChXN7pDTo5k&t=583s)** targets that are being scraped, we can see that the state here is up of instance 1921x816.10

**[09:51](https://youtube.com/watch?v=ChXN7pDTo5k&t=591s)** of job UPS. The last scrape was 14 15 seconds ago and it took 90 milliseconds to do that scrape.

**[09:59](https://youtube.com/watch?v=ChXN7pDTo5k&t=599s)** Now, if we jump to this URL here, we can actually take a manual look at the endpoint. Again,

**[10:03](https://youtube.com/watch?v=ChXN7pDTo5k&t=603s)** note that I'm connected here through the subnet router, but we could just as easily use instead

**[10:09](https://youtube.com/watch?v=ChXN7pDTo5k&t=609s)** the exact same URL, but using the 100 dot tail scale IP address instead. It doesn't really matter

**[10:16](https://youtube.com/watch?v=ChXN7pDTo5k&t=616s)** what which one you pick. So let's try and query our first value. I want to know what my charge

**[10:21](https://youtube.com/watch?v=ChXN7pDTo5k&t=621s)** percentage is. And you can literally just type. You don't have to know much about Prometheus query

**[10:27](https://youtube.com/watch?v=ChXN7pDTo5k&t=627s)** language to get started with this stuff. Of course, if you want to do some more advanced stuff

**[10:31](https://youtube.com/watch?v=ChXN7pDTo5k&t=631s)** down the road, the world is your oyster as far as problem QL is concerned. You can do arithmetic

**[10:37](https://youtube.com/watch?v=ChXN7pDTo5k&t=637s)** operations and things like that and all sorts of craziness. But for today, I think we'll keep it simple.

**[10:42](https://youtube.com/watch?v=ChXN7pDTo5k&t=642s)** I just want to know what this value is. And you can see I can select things based on instance,

**[10:47](https://youtube.com/watch?v=ChXN7pDTo5k&t=647s)** job, UPS, the name. Remember, we can figure this on the server side in England, APS, UPS,

**[10:55](https://youtube.com/watch?v=ChXN7pDTo5k&t=655s)** Snowball, and we can see here that the value is 100. So that proves that Prometheus is

**[11:01](https://youtube.com/watch?v=ChXN7pDTo5k&t=661s)** connected over tail scale to the remote server in England. The next step is to try and create

**[11:07](https://youtube.com/watch?v=ChXN7pDTo5k&t=667s)** some beautiful graphs with Grafana. And by default, when you spin up Grafana for the first time,

**[11:13](https://youtube.com/watch?v=ChXN7pDTo5k&t=673s)** you're going to want to configure your username and password, all that kind of stuff. I think it's

**[11:17](https://youtube.com/watch?v=ChXN7pDTo5k&t=677s)** admin admin. I've just got a basic instance here with no data sources or anything configured.

**[11:23](https://youtube.com/watch?v=ChXN7pDTo5k&t=683s)** So we need to add a data source, first of all, something that Grafana can query

**[11:27](https://youtube.com/watch?v=ChXN7pDTo5k&t=687s)** to grab the data that we want to put into graph form. So data source is over here on the left.

**[11:33](https://youtube.com/watch?v=ChXN7pDTo5k&t=693s)** And then click on add data source. Next up, click on Prometheus. And we want to put the name,

**[11:38](https://youtube.com/watch?v=ChXN7pDTo5k&t=698s)** yeah, Prometheus is fine. And I'm going to grab the IP address of the Prometheus box just so there's

**[11:44](https://youtube.com/watch?v=ChXN7pDTo5k&t=704s)** no DNS weirdness going on. Not that I think there would be. But by clicking on that in the Mac

**[11:49](https://youtube.com/watch?v=ChXN7pDTo5k&t=709s)** client, by the way, you actually get the IP address. So I do HTTP and I get 100.67,

**[11:56](https://youtube.com/watch?v=ChXN7pDTo5k&t=716s)** 125.12. And then Prometheus is running on 1990, I think. No authentication right now. And I

**[12:04](https://youtube.com/watch?v=ChXN7pDTo5k&t=724s)** think if we do save and test, yeah, you successfully query the Prometheus API. Fantastic. So

**[12:10](https://youtube.com/watch?v=ChXN7pDTo5k&t=730s)** I'm going to now build a dashboard. I just want to add a visualization using the Prometheus

**[12:16](https://youtube.com/watch?v=ChXN7pDTo5k&t=736s)** data source. And then I'm going to select a metric charge percentage because we know that one

**[12:21](https://youtube.com/watch?v=ChXN7pDTo5k&t=741s)** exists. And then I click on the run queries button up here. And you can see that my charge

**[12:25](https://youtube.com/watch?v=ChXN7pDTo5k&t=745s)** percentage is now in a Prometheus graph. I could obviously take this a step further and type in,

**[12:31](https://youtube.com/watch?v=ChXN7pDTo5k&t=751s)** you know, snowball battery percent, click save. I'm going to call this snowball UPS. And you can

**[12:41](https://youtube.com/watch?v=ChXN7pDTo5k&t=761s)** see I've now got a dashboard. And I can monitor my UPS battery percentage and anything else my

**[12:47](https://youtube.com/watch?v=ChXN7pDTo5k&t=767s)** well, my little brain can think of. I could monitor the disk usage with a Prometheus node

**[12:53](https://youtube.com/watch?v=ChXN7pDTo5k&t=773s)** exporter on the remote system. I can monitor pretty much any sensor that can output a basic

**[13:00](https://youtube.com/watch?v=ChXN7pDTo5k&t=780s)** formatted list of parameters and sensors. Prometheus can scrape. And it really is a very

**[13:08](https://youtube.com/watch?v=ChXN7pDTo5k&t=788s)** versatile tool, particularly when you don't even have to worry about firewalls being in the way

**[13:12](https://youtube.com/watch?v=ChXN7pDTo5k&t=792s)** thanks to tail scale. So I hope you learned something today. It was a quick and fast video. But

**[13:16](https://youtube.com/watch?v=ChXN7pDTo5k&t=796s)** sometimes I think the purpose of these videos is more to give you the idea than it is to show you

**[13:21](https://youtube.com/watch?v=ChXN7pDTo5k&t=801s)** the exact specifics of every single solution possible with Prometheus because there's a lot.

**[13:28](https://youtube.com/watch?v=ChXN7pDTo5k&t=808s)** Now don't forget to get subscribed down below. We have started doing live streams here on YouTube

**[13:32](https://youtube.com/watch?v=ChXN7pDTo5k&t=812s)** every couple of weeks. You can come and ask me questions in real time and we'll work through them

**[13:36](https://youtube.com/watch?v=ChXN7pDTo5k&t=816s)** together. So until next time, thank you so much for watching. I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
