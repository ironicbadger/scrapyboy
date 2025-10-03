---
video_id: "z1vBMMQzCEk"
title: "App Connectors - Split DNS for any website on your tailnet | Tailscale Explained"
description: "In this video, I demonstrate one of Tailscale’s lesser known, but most powerful features: App Connectors. Think of it as split DNS for specific websites on your Tailnet, allowing you to route traffic ..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-03-13"
duration_seconds: 696
youtube_url: "https://www.youtube.com/watch?v=z1vBMMQzCEk"
thumbnail_url: "https://i.ytimg.com/vi/z1vBMMQzCEk/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:54:35.281936"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2143
transcription_time_seconds: 18.5
---

# App Connectors - Split DNS for any website on your tailnet | Tailscale Explained

**[00:00](https://youtube.com/watch?v=z1vBMMQzCEk&t=0s)** One of the less well-known features of Tailscale is something called App Connectors. You can think of this

**[00:05](https://youtube.com/watch?v=z1vBMMQzCEk&t=5s)** a little bit like Split DNS for specific websites on your tailnet. So, for example, let's say I wanted

**[00:12](https://youtube.com/watch?v=z1vBMMQzCEk&t=12s)** to route all the traffic for IP chicken out through a specific endpoint. So let's say I've got a VPS

**[00:20](https://youtube.com/watch?v=z1vBMMQzCEk&t=20s)** somewhere and I wanted all of the traffic that goes to IP chicken from any client on my tailnet

**[00:25](https://youtube.com/watch?v=z1vBMMQzCEk&t=25s)** to route through that droplet running on digital ocean to get the IPv4 address

**[00:30](https://youtube.com/watch?v=z1vBMMQzCEk&t=30s)** not from where I'm currently sat but from the droplet wherever that happens to be in my case,

**[00:36](https://youtube.com/watch?v=z1vBMMQzCEk&t=36s)** it happens to be in London. So in today's video, we're going to go through the basics of App Connectors,

**[00:40](https://youtube.com/watch?v=z1vBMMQzCEk&t=40s)** hopefully start your gears turning about some of the fun things you can do when you can basically

**[00:45](https://youtube.com/watch?v=z1vBMMQzCEk&t=45s)** split the traffic across any number of websites using Tailscale App Connectors. So I'll put a link

**[00:52](https://youtube.com/watch?v=z1vBMMQzCEk&t=52s)** in the description down below to the documentation for App Connectors and I highly recommend you read it

**[00:57](https://youtube.com/watch?v=z1vBMMQzCEk&t=57s)** even if you've watched this video. There are a number of little steps you've got to follow

**[01:01](https://youtube.com/watch?v=z1vBMMQzCEk&t=61s)** requirements to make sure that you can enable the App Connectors. First of all, you need a piece of

**[01:07](https://youtube.com/watch?v=z1vBMMQzCEk&t=67s)** remote infrastructure through which you're going to route all of your traffic. Now, what are some

**[01:12](https://youtube.com/watch?v=z1vBMMQzCEk&t=72s)** of the use cases that might be useful for this kind of thing? Well, the obvious one that jumps out

**[01:17](https://youtube.com/watch?v=z1vBMMQzCEk&t=77s)** to me at least is let's say you've got an enterprise GitHub and you want to whitelist the only

**[01:22](https://youtube.com/watch?v=z1vBMMQzCEk&t=82s)** certain pieces of infrastructure can connect into your enterprise GitHub deployment. With App Connectors,

**[01:28](https://youtube.com/watch?v=z1vBMMQzCEk&t=88s)** you can effectively tell any client that's running Tailscale, well, to connect to the enterprise

**[01:34](https://youtube.com/watch?v=z1vBMMQzCEk&t=94s)** GitHub, you must go through this front door effectively. You can think of it almost a bit like a

**[01:39](https://youtube.com/watch?v=z1vBMMQzCEk&t=99s)** bastion host, a jump host, or some kind of way to specify the applications and how you connect to

**[01:46](https://youtube.com/watch?v=z1vBMMQzCEk&t=106s)** them specifically over your Tailnet. So this is a very contrived example. I want to connect IP

**[01:53](https://youtube.com/watch?v=z1vBMMQzCEk&t=113s)** chicken here. I'll take my public WAN IP address and have it route out through a digital ocean

**[02:00](https://youtube.com/watch?v=z1vBMMQzCEk&t=120s)** droplet in London. So I'm here in America and the droplet's in London and we're going to make it so

**[02:06](https://youtube.com/watch?v=z1vBMMQzCEk&t=126s)** that when I refresh this page, IPchicken.com and I'm connected to my Tailnet, it routes all of that

**[02:12](https://youtube.com/watch?v=z1vBMMQzCEk&t=132s)** traffic out through the droplet in London. App connectors are available for all plans and if you'd like

**[02:18](https://youtube.com/watch?v=z1vBMMQzCEk&t=138s)** to learn more about bringing Tailscale to work, you can go to tailscale.com slash BTW to find out

**[02:23](https://youtube.com/watch?v=z1vBMMQzCEk&t=143s)** how many of our customers have made the switch to Tailscale. But the first thing that you need to get

**[02:28](https://youtube.com/watch?v=z1vBMMQzCEk&t=148s)** ready to configure are the requirements for your Tailnet policy file, which sometimes refers to

**[02:33](https://youtube.com/watch?v=z1vBMMQzCEk&t=153s)** as your ACL file, but essentially you need to create first of all a tag for the app connector. So

**[02:40](https://youtube.com/watch?v=z1vBMMQzCEk&t=160s)** if we jump over to tailscale.com and go to the admin console and then under access controls,

**[02:48](https://youtube.com/watch?v=z1vBMMQzCEk&t=168s)** we just want to simply create these few lines here. So tag owners and then a tag. So I'm just going

**[02:54](https://youtube.com/watch?v=z1vBMMQzCEk&t=174s)** to call this UK connector. Next up, I'm going to save that policy file and go back to the documentation.

**[03:02](https://youtube.com/watch?v=z1vBMMQzCEk&t=182s)** We next need to add an auto approval policy so that we can approve routes for these app connectors

**[03:09](https://youtube.com/watch?v=z1vBMMQzCEk&t=189s)** automatically. And if we scroll down on the documentation page, we can find an example of the

**[03:14](https://youtube.com/watch?v=z1vBMMQzCEk&t=194s)** auto approver's stanza that's actually required. So I'm just going to copy this straight

**[03:18](https://youtube.com/watch?v=z1vBMMQzCEk&t=198s)** forwardly and put it straight into my access policy file. I'm going to find a space near the bottom.

**[03:23](https://youtube.com/watch?v=z1vBMMQzCEk&t=203s)** In fact, I already have an auto approver's stanza. So a little bit of modification is required here

**[03:28](https://youtube.com/watch?v=z1vBMMQzCEk&t=208s)** just to make sure the syntax is correct. You can see I've already got an auto approver here to

**[03:33](https://youtube.com/watch?v=z1vBMMQzCEk&t=213s)** automatically approve exit node requests. But in my case, I want to enable the routes to be auto

**[03:39](https://youtube.com/watch?v=z1vBMMQzCEk&t=219s)** approved for the app connectors specifically for IP chicken or at least the app connector tag

**[03:46](https://youtube.com/watch?v=z1vBMMQzCEk&t=226s)** that we just created at the top of the file. So if I scroll back up and look for what did I call it,

**[03:52](https://youtube.com/watch?v=z1vBMMQzCEk&t=232s)** UK connector. And I want to put this in now into the auto approver's stanza that's up down here.

**[04:00](https://youtube.com/watch?v=z1vBMMQzCEk&t=240s)** You can see I've got separate lines for IPv4 addresses and IPv6 as well. So it doesn't matter

**[04:06](https://youtube.com/watch?v=z1vBMMQzCEk&t=246s)** if the target remote host that you want to proxy through and split the DNS through the app connector,

**[04:12](https://youtube.com/watch?v=z1vBMMQzCEk&t=252s)** whether it's an IPv4 or an IPv6 situation, both should work just fine. And now if I click save,

**[04:20](https://youtube.com/watch?v=z1vBMMQzCEk&t=260s)** oh, I've made a mistake here. Yes, one too many brackets. Thank you very much, copy and paste.

**[04:25](https://youtube.com/watch?v=z1vBMMQzCEk&t=265s)** All right, with that fixed, I'll just show you once again what the auto approver's stanza now looks

**[04:30](https://youtube.com/watch?v=z1vBMMQzCEk&t=270s)** like. Nice and straightforward, I think. And if we jump back to the documentation one more time,

**[04:35](https://youtube.com/watch?v=z1vBMMQzCEk&t=275s)** we've got to create an access control policy that's going to allow us to route the specific

**[04:39](https://youtube.com/watch?v=z1vBMMQzCEk&t=279s)** application traffic through the app connector tag. This is because you must allow

**[04:44](https://youtube.com/watch?v=z1vBMMQzCEk&t=284s)** tailnet devices to access the routes that the app connector has created. So we're just going to

**[04:49](https://youtube.com/watch?v=z1vBMMQzCEk&t=289s)** copy and paste in here this auto group ACL option here. Essentially what this is going to do is make

**[04:55](https://youtube.com/watch?v=z1vBMMQzCEk&t=295s)** any device, any source device that is a member of your tailnet have access to the destination

**[05:01](https://youtube.com/watch?v=z1vBMMQzCEk&t=301s)** of the internet with a wild card. So I'm going to look for the ACL stanza in my ACLs over here.

**[05:08](https://youtube.com/watch?v=z1vBMMQzCEk&t=308s)** Here we are. In fact, I probably, in my case, don't actually need to do this because I still have

**[05:14](https://youtube.com/watch?v=z1vBMMQzCEk&t=314s)** the default option of ACLs turned on, which is allow any source to any destination. So I'm actually

**[05:21](https://youtube.com/watch?v=z1vBMMQzCEk&t=321s)** just going to leave this one alone. If you've gotten fancy with your ACLs already,

**[05:25](https://youtube.com/watch?v=z1vBMMQzCEk&t=325s)** you will need to follow this step. But in my case, I don't. The next one is step five. And this

**[05:31](https://youtube.com/watch?v=z1vBMMQzCEk&t=331s)** one's a little more involved. And actually, I'm going to show you how to do this bit through the UI

**[05:36](https://youtube.com/watch?v=z1vBMMQzCEk&t=336s)** instead of doing it by copying and pasting into your ACLs file. So you may have noticed over the

**[05:42](https://youtube.com/watch?v=z1vBMMQzCEk&t=342s)** years that this little apps button up here, but maybe you've never quite known what to do with it.

**[05:47](https://youtube.com/watch?v=z1vBMMQzCEk&t=347s)** So what we're going to do is add an app. This is how you configure an app connector. And I'm just

**[05:52](https://youtube.com/watch?v=z1vBMMQzCEk&t=352s)** going to call this one IP chicken. I'm going to select a custom. You can see all the the pre-determined

**[05:58](https://youtube.com/watch?v=z1vBMMQzCEk&t=358s)** things here like octa sales force, GitHub, Google workspaces, Gira and so on. Lots of really useful

**[06:06](https://youtube.com/watch?v=z1vBMMQzCEk&t=366s)** business-y type stuff here. But that's not what we're doing today. We're doing some custom

**[06:10](https://youtube.com/watch?v=z1vBMMQzCEk&t=370s)** hacking today. And I literally just want to type in IP chicken.com. And then I'm going to select

**[06:17](https://youtube.com/watch?v=z1vBMMQzCEk&t=377s)** the UK connector tag just here. Once I've done that, you'll see that it says needs action. Well,

**[06:24](https://youtube.com/watch?v=z1vBMMQzCEk&t=384s)** not least of which because there are no nodes on my tailnet that currently have that tag. So let's

**[06:28](https://youtube.com/watch?v=z1vBMMQzCEk&t=388s)** take care of that. Over on digital ocean, I created a brand new droplet. It's completely empty,

**[06:34](https://youtube.com/watch?v=z1vBMMQzCEk&t=394s)** has nothing installed on it whatsoever. So I'm going to go ahead and install tail scale on that real

**[06:39](https://youtube.com/watch?v=z1vBMMQzCEk&t=399s)** quick. The fastest way to install tail scale on Linux is to use this one line bash command right

**[06:44](https://youtube.com/watch?v=z1vBMMQzCEk&t=404s)** here. Obviously the risks of piping a script to bash to install things. You should always

**[06:52](https://youtube.com/watch?v=z1vBMMQzCEk&t=412s)** inspect the script and make sure that you've tested this stuff before you just do that.

**[06:57](https://youtube.com/watch?v=z1vBMMQzCEk&t=417s)** But for the purposes of my demo, I'm not too worried. All right, with tail scale now installed,

**[07:03](https://youtube.com/watch?v=z1vBMMQzCEk&t=423s)** I should be able to do tail scale up dash dash SSH. This is going to ask me to authenticate this

**[07:10](https://youtube.com/watch?v=z1vBMMQzCEk&t=430s)** node to my tailnet, which we've done many times on this channel before. So I won't go into too much

**[07:15](https://youtube.com/watch?v=z1vBMMQzCEk&t=435s)** detail here. But essentially, I'm going to end up with a host named the digital ocean,

**[07:22](https://youtube.com/watch?v=z1vBMMQzCEk&t=442s)** lovely, simple to pronounce Ubuntu, blah, blah, blah, London 01. And that's going to become a node

**[07:28](https://youtube.com/watch?v=z1vBMMQzCEk&t=448s)** on my tailnet. Once that's there, I want to make sure that I've got the correct tags enabled

**[07:33](https://youtube.com/watch?v=z1vBMMQzCEk&t=453s)** because right now this node is currently owned by a tail and scales at gmail.com. It's currently

**[07:39](https://youtube.com/watch?v=z1vBMMQzCEk&t=459s)** owned by me. But for an app connector to work, you've got to tag the thing. So the 3.menu over here

**[07:45](https://youtube.com/watch?v=z1vBMMQzCEk&t=465s)** on the right, we're going to edit ACL tags. I'm going to select UK connector and click save.

**[07:52](https://youtube.com/watch?v=z1vBMMQzCEk&t=472s)** Next thing I'm going to do is go back to my digital ocean droplet and do tail scale set dash dash

**[07:58](https://youtube.com/watch?v=z1vBMMQzCEk&t=478s)** advertise connector. This is going to turn on the app connector functionality as part of the

**[08:05](https://youtube.com/watch?v=z1vBMMQzCEk&t=485s)** tail scale deployment. Now, you'll notice there are a couple of things we've got to take care of

**[08:09](https://youtube.com/watch?v=z1vBMMQzCEk&t=489s)** first. Of course, because we're doing a similar thing to what we would do with a subnet router,

**[08:13](https://youtube.com/watch?v=z1vBMMQzCEk&t=493s)** we're taking packets in on one interface and forwarding them out over that same interface,

**[08:18](https://youtube.com/watch?v=z1vBMMQzCEk&t=498s)** we've got to make sure that IP forwarding is turned on. And we can do that just by going to the

**[08:22](https://youtube.com/watch?v=z1vBMMQzCEk&t=502s)** tail scale documentation, copying and pasting these few lines right here into your exesysctl.directory.

**[08:29](https://youtube.com/watch?v=z1vBMMQzCEk&t=509s)** So I'm just going to do that straight away. Just paste those in. Now that should be good to go.

**[08:34](https://youtube.com/watch?v=z1vBMMQzCEk&t=514s)** The other thing we're going to do is look at the Linux optimizations we can undertake for UDP

**[08:39](https://youtube.com/watch?v=z1vBMMQzCEk&t=519s)** performance. I don't think performance in our particular scenario is super duper important,

**[08:44](https://youtube.com/watch?v=z1vBMMQzCEk&t=524s)** but in for a penny, in for a pound. Why not? So the first thing I'm going to do is just copy

**[08:49](https://youtube.com/watch?v=z1vBMMQzCEk&t=529s)** this eith tool command right here and paste this into my droplet. It's going to run a bunch of stuff

**[08:55](https://youtube.com/watch?v=z1vBMMQzCEk&t=535s)** in the background. No error messages. So I think we're good. By default, though, changes made

**[09:00](https://youtube.com/watch?v=z1vBMMQzCEk&t=540s)** using eith tool in this method do not survive a reboot. So we're going to have to modify this file

**[09:06](https://youtube.com/watch?v=z1vBMMQzCEk&t=546s)** here in etsy network d dispatcher rootable.d and create a file called 50 dash tail scale. Again,

**[09:14](https://youtube.com/watch?v=z1vBMMQzCEk&t=554s)** just copying and pasting this stuff from the documentation is all it's required. And then

**[09:20](https://youtube.com/watch?v=z1vBMMQzCEk&t=560s)** the final thing is just a check that we've successfully configured this stuff on the droplet.

**[09:25](https://youtube.com/watch?v=z1vBMMQzCEk&t=565s)** No errors occurred. So we should now be pretty much good to go. So I'm going to go back through my

**[09:31](https://youtube.com/watch?v=z1vBMMQzCEk&t=571s)** bash history with a control R and look for advertised connector. And this time there was no error

**[09:37](https://youtube.com/watch?v=z1vBMMQzCEk&t=577s)** in the output. So we should now be in a position where we can try out our brand new app connector.

**[09:43](https://youtube.com/watch?v=z1vBMMQzCEk&t=583s)** And indeed, if we now go back to the apps tab in our tail scale admin console, we can see that

**[09:48](https://youtube.com/watch?v=z1vBMMQzCEk&t=588s)** IP chicken as a domain is now rooting itself through the Ubuntu London one connection last

**[09:54](https://youtube.com/watch?v=z1vBMMQzCEk&t=594s)** seen at 406. It's now 407. So that looks good to me. Status is currently active. So here is my

**[10:01](https://youtube.com/watch?v=z1vBMMQzCEk&t=601s)** current IP address. I'm just going to blur out everything except for the last bit of 192. And

**[10:07](https://youtube.com/watch?v=z1vBMMQzCEk&t=607s)** hopefully, when I refresh this page, it's now going to detect a network change. So it's just picked

**[10:12](https://youtube.com/watch?v=z1vBMMQzCEk&t=612s)** up the new roots. And it's now going to come out through the digital ocean droplet. So let's verify

**[10:16](https://youtube.com/watch?v=z1vBMMQzCEk&t=616s)** this IP address. End in 24.243. Does this match our droplet 24.243? It works. So we can do this now with a

**[10:26](https://youtube.com/watch?v=z1vBMMQzCEk&t=626s)** whole host of different websites. News websites are a particular one for me that I find pretty useful

**[10:32](https://youtube.com/watch?v=z1vBMMQzCEk&t=632s)** to root through. So I live in America these days. This is a very personal use case. But I still like

**[10:37](https://youtube.com/watch?v=z1vBMMQzCEk&t=637s)** to read the BBC now. And again, without adverts and all this kind of other stuff that happens to

**[10:41](https://youtube.com/watch?v=z1vBMMQzCEk&t=641s)** BBC.com. So I send BBC.co.uk through to my parents house. And it roots out through the server that

**[10:48](https://youtube.com/watch?v=z1vBMMQzCEk&t=648s)** I have running in England. And as we like to say in England, jobs are good. And so that's a very

**[10:54](https://youtube.com/watch?v=z1vBMMQzCEk&t=654s)** quick overview of tailscales, innovative app connectors feature. Think of it like split DNS

**[11:00](https://youtube.com/watch?v=z1vBMMQzCEk&t=660s)** for your tailnet to root any application or any website out through any other piece of

**[11:05](https://youtube.com/watch?v=z1vBMMQzCEk&t=665s)** infrastructure that you would like. Take a look at the tailscale explained playlist that I'll

**[11:09](https://youtube.com/watch?v=z1vBMMQzCEk&t=669s)** link in the description down below as well for some of the other tailscale features that we've

**[11:13](https://youtube.com/watch?v=z1vBMMQzCEk&t=673s)** covered on this channel. And until next time, thank you so much for watching. I've been Alex from

**[11:17](https://youtube.com/watch?v=z1vBMMQzCEk&t=677s)** tailscale.

---

*Automatically generated transcript. May contain errors.*
