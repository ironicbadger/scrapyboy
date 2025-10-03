---
video_id: "sPUkAm7yDlU"
title: "Use a custom OIDC and passkeys to log in to Tailscale with Pocket ID"
description: "No more passwords, ever again! That's the promise of passkeys. Using Pocket ID in today's video I will show you how to configure this self-hosted, open source authentication provider to work with your..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-05-01"
duration_seconds: 1453
youtube_url: "https://www.youtube.com/watch?v=sPUkAm7yDlU"
thumbnail_url: "https://i.ytimg.com/vi/sPUkAm7yDlU/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:32:08.815405"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 4692
transcription_time_seconds: 41.5
---

# Use a custom OIDC and passkeys to log in to Tailscale with Pocket ID

**[00:00](https://youtube.com/watch?v=sPUkAm7yDlU&t=0s)** Wouldn't it be cool if you could sign into your tailnet without a password ever again? Well, that's the promise of past keys. And I'm going to show you in today's video, how to set up Pocket ID, which is a custom OIDC provider, to enable just that. So watch this. I'm going to sign into my tailnet here, using the name Bill at inateclabs.dev and inateclabs.dev is a domain name I own, by the way. I'm going to click sign in. Now, no hands, no using names, no passwords, no auto fill or anything like that. And you can see on the screen,

**[00:30](https://youtube.com/watch?v=sPUkAm7yDlU&t=30s)** I've been taken to ID.inateclabs.dev as a Pocket ID sign-in page. So when I click sign in, it's going to prompt me for a pass key. I'm going to click on Bill. I'm then going to present my digit with my fingerprint right here. And I'm going to be logged into Tailscale. It's as simple as that. So if you want to find out how to do that, that's what today's video is all about. Pocket ID, custom OIDC providers and tailscale.

**[00:59](https://youtube.com/watch?v=sPUkAm7yDlU&t=59s)** There are chapter markers down below because there are quite a lot of small little things that we need to get in place for today. And just to save you a bit of time, you know, if you've already got a domain name, for example, and you've already got DNS set up, you can just skip that section of the video that's not relevant to you. But in case you're coming at this completely fresh, I'm going to go through this in a fairly linear order. And again, you can use the chapter markers to kind of find a bit of the video that makes the most sense to you.

**[01:24](https://youtube.com/watch?v=sPUkAm7yDlU&t=84s)** So if you're brand new to tailscale or you're just creating a brand new talent for this purpose, head on over to tailscale.com and click on the get started. It's free button.

**[01:34](https://youtube.com/watch?v=sPUkAm7yDlU&t=94s)** This is going to give you an option to sign up with a whole bunch of different identity providers. And the one that we are interested in today is this one at the bottom, sign up with an OIDC.

**[01:44](https://youtube.com/watch?v=sPUkAm7yDlU&t=104s)** We need a domain name at this point. Now, I hope you have one. If you don't, you can head over to somewhere like, I don't know, pork bun or name cheap or even cloud flares sell domains. But personally, I like to separate the registration of a domain from where its name service are pointed to from where the DNS lives.

**[02:00](https://youtube.com/watch?v=sPUkAm7yDlU&t=120s)** You can find domain names, typically even dot com domain names, if you're willing to go long enough for $10, $12 a year, something like that. If you're willing to go with a slightly more esoteric TLD, and a TLD means the top level domain bit at the end.

**[02:16](https://youtube.com/watch?v=sPUkAm7yDlU&t=136s)** If you're willing to go with a slightly more esoteric TLD, you can get them for a couple of dollars a year. So owning your own domain name, hopefully shouldn't be an impediment to proceeding beyond this point.

**[02:25](https://youtube.com/watch?v=sPUkAm7yDlU&t=145s)** Once you've purchased your domain, you can see I've got a few registered here under my pork bun account. You're going to want to configure the name service for that domain to point to somewhere that you can control in my case, I use cloud flare.

**[02:38](https://youtube.com/watch?v=sPUkAm7yDlU&t=158s)** So we're going to use today, we're going to use the domain name of in a tech labs dot dev when adding a new domain to cloud flare, you click the add button up here, connect a domain, and it will walk you through the process and give you a couple of name servers that are specific to your cloud flare account.

**[02:53](https://youtube.com/watch?v=sPUkAm7yDlU&t=173s)** That information typically lives down the bottom here, cloud flare name server. So in my case, I've got me, Lani and Steven, I then plug that information back into pork bun. So if I go to in a tech labs dot dev and go to details, you can see that I've got these options here for my name servers and I can edit them by clicking this button right here by default, pork bun will give you some default name servers that won't point to cloud flare.

**[03:19](https://youtube.com/watch?v=sPUkAm7yDlU&t=199s)** And so once you've done that, you are pretty much done in terms of setting up the raw mechanics of what's needed for your personal domain side of things.

**[03:28](https://youtube.com/watch?v=sPUkAm7yDlU&t=208s)** The next thing we need to do is actually get pocket ID spun up now, I'm going to run pocket ID today in a digital ocean droplet and the reason for this is because the service needs to be exposed to the public internet.

**[03:39](https://youtube.com/watch?v=sPUkAm7yDlU&t=219s)** You can secure it however you like, I'm going to put mine behind a reverse proxy, more cover all that in the video, don't worry, but I'm going to spin this up like I say on digital ocean, you can use Hetzner or linode or Vulture or AWS or GCP if you want to doesn't really matter.

**[03:54](https://youtube.com/watch?v=sPUkAm7yDlU&t=234s)** So long as you get pocket ID running as a publicly facing service, I don't really care how you get there. But if you're going to follow along this tutorial verbatim, let's just create a brand new droplet.

**[04:04](https://youtube.com/watch?v=sPUkAm7yDlU&t=244s)** The reason I pick DO after all this time really is I have no affiliation to them and neither does tail scale, but they're just cheap, it's like $4, $5, $6 a month, something like that for the basic one.

**[04:15](https://youtube.com/watch?v=sPUkAm7yDlU&t=255s)** You can click on general purpose here, no basic regular, that's it.

**[04:19](https://youtube.com/watch?v=sPUkAm7yDlU&t=259s)** $6 a month is the cheapest option, like I say, Hetzner have some cheap ones linode to lots of options in this space, but I'm going to call this one TS pocket ID.

**[04:30](https://youtube.com/watch?v=sPUkAm7yDlU&t=270s)** Okay, and once that's done, we're going to create the droplets. Now this takes 30 seconds or so, really not that long.

**[04:36](https://youtube.com/watch?v=sPUkAm7yDlU&t=276s)** Once the droplets created, we'll go and SSH into it and set things up some of the basics. So SSH root at and then the IP address of the remote system.

**[04:45](https://youtube.com/watch?v=sPUkAm7yDlU&t=285s)** So the first command we're going to run is apt update this update the local mirrors, a local copy of the mirrors.

**[04:52](https://youtube.com/watch?v=sPUkAm7yDlU&t=292s)** So basically Ubuntu can build a delta between what's available upstream from Ubuntu and what's on my local system and tell me that I've got 160 packages to upgrade to bring this image up to date.

**[05:04](https://youtube.com/watch?v=sPUkAm7yDlU&t=304s)** Next I'm going to type apt upgrade, this is going to upgrade the fresh Ubuntu image from digital ocean and look at that.

**[05:11](https://youtube.com/watch?v=sPUkAm7yDlU&t=311s)** That must be apt 3.0, I haven't seen that before. Wow, that looks nice.

**[05:15](https://youtube.com/watch?v=sPUkAm7yDlU&t=315s)** But anyway, you can see there's 160 odd packages getting upgraded, you can see the excuse to do all that kind of stuff.

**[05:20](https://youtube.com/watch?v=sPUkAm7yDlU&t=320s)** We'll take a couple of minutes, so I'll be right back.

**[05:23](https://youtube.com/watch?v=sPUkAm7yDlU&t=323s)** And with our packages now up to date, I'm going to go ahead and have a little helper script that I just have hosted over at SH dot ktz dot me slash LXC dot SH.

**[05:32](https://youtube.com/watch?v=sPUkAm7yDlU&t=332s)** And you can see in here, there's just two commands.

**[05:34](https://youtube.com/watch?v=sPUkAm7yDlU&t=334s)** One is to install Docker, the other one is to install tail scale. These are both the official commands from both of those projects.

**[05:41](https://youtube.com/watch?v=sPUkAm7yDlU&t=341s)** The helper script is just that, just to help up. So if you want to pipe that to bash and make your life easy, you can don't run random code off the internet unless you're the one hosting it, which in my case is me.

**[05:52](https://youtube.com/watch?v=sPUkAm7yDlU&t=352s)** So it's all good. So this will get tail scale installed onto this machine as well as Docker.

**[05:58](https://youtube.com/watch?v=sPUkAm7yDlU&t=358s)** We're going to use Docker to run pocket ID today and obviously tail scale. I've got to install tail scale.

**[06:03](https://youtube.com/watch?v=sPUkAm7yDlU&t=363s)** All right, let's just part of the part of the deal here, but it will make our SSH access to this server much easier going forward.

**[06:10](https://youtube.com/watch?v=sPUkAm7yDlU&t=370s)** And we can we can enforce things like grants and ACLs and basically fence this off from the rest of our talent and make it a really secure enclave.

**[06:18](https://youtube.com/watch?v=sPUkAm7yDlU&t=378s)** We don't want just anybody to have access to where our identity stuff is living, right.

**[06:23](https://youtube.com/watch?v=sPUkAm7yDlU&t=383s)** So once that's done, we're going to go ahead and reboot the droplet and then connect it to tail scale and spin up the pocket ID Docker.

**[06:29](https://youtube.com/watch?v=sPUkAm7yDlU&t=389s)** So now that's done. It's time to connect this droplet to my tail net. So I'm going to do my standard tail scale up dash dash SSH so I can use tail scale SSH.

**[06:37](https://youtube.com/watch?v=sPUkAm7yDlU&t=397s)** Instead of having to worry about using names on passwords and SSH keys onto this system anymore.

**[06:43](https://youtube.com/watch?v=sPUkAm7yDlU&t=403s)** Which town should I put this on to catch 22 time. Let's actually leave this till later in the video and I'm going to add this to the new tail net that we're going to create.

**[06:54](https://youtube.com/watch?v=sPUkAm7yDlU&t=414s)** So that this node becomes part of rather than my typical demo, tell net of tail and scales or Gmail.com.

**[07:01](https://youtube.com/watch?v=sPUkAm7yDlU&t=421s)** This is going to become part of our new in a tech labs dot dev tail net. All right, very good.

**[07:07](https://youtube.com/watch?v=sPUkAm7yDlU&t=427s)** So let's reboot this node now and pick up the latest kernel. If there was any changes and just make sure the node is completely fresh late for us to build upon.

**[07:16](https://youtube.com/watch?v=sPUkAm7yDlU&t=436s)** So our reboot was successful. Our node is back now in the description down below. There'll be a link to a GitHub snippet where I have all of this code available.

**[07:25](https://youtube.com/watch?v=sPUkAm7yDlU&t=445s)** This is what we're going to need to spin up pocket ID behind a reverse proxy that configures our TLS certificates for us.

**[07:33](https://youtube.com/watch?v=sPUkAm7yDlU&t=453s)** So we're going to run pocket ID on ID dot in a tech labs dot dev. But in order for this traffic container to be able to make the DNS challenges for us in cloud flare.

**[07:43](https://youtube.com/watch?v=sPUkAm7yDlU&t=463s)** We are going to have to set up a token in cloud flare. So head over back to your cloud flare dashboard. Click on profile.

**[07:50](https://youtube.com/watch?v=sPUkAm7yDlU&t=470s)** You can see I've actually already got an in a tech labs DNS challenge one right here.

**[07:54](https://youtube.com/watch?v=sPUkAm7yDlU&t=474s)** So let's just see what the summary of this is. I've got zone read and DNS edit. So let's just create a new one just so that this tutorial is fully complete.

**[08:05](https://youtube.com/watch?v=sPUkAm7yDlU&t=485s)** So I'm going to click on get started and then I'm going to give it in a tech labs pocket ID. I guess.

**[08:14](https://youtube.com/watch?v=sPUkAm7yDlU&t=494s)** And then what did we have zone read zone and then I want to be able to read the settings for this zone.

**[08:25](https://youtube.com/watch?v=sPUkAm7yDlU&t=505s)** And then also under DNS I need to be able to edit the DNS settings for I assume this zone as well.

**[08:32](https://youtube.com/watch?v=sPUkAm7yDlU&t=512s)** Yeah, there we go. The zone DNS edit and I don't want to include all of the zones from this specific cloud flare account.

**[08:42](https://youtube.com/watch?v=sPUkAm7yDlU&t=522s)** I want to limit it to just this one. So in the tech labs dot dev and there we go.

**[08:49](https://youtube.com/watch?v=sPUkAm7yDlU&t=529s)** I'm going to get myself a nice shiny new token, which I'll copy to my clipboard and I'll put into my VS code file right here.

**[08:56](https://youtube.com/watch?v=sPUkAm7yDlU&t=536s)** And now traffic will be able to get us a TLS certificate from let's encrypt for this domain.

**[09:02](https://youtube.com/watch?v=sPUkAm7yDlU&t=542s)** So what do we do with this file? Well, typically I would use the tail scale SSH extension built into VS code to copy the file around.

**[09:09](https://youtube.com/watch?v=sPUkAm7yDlU&t=549s)** But as I mentioned, we're in a bit of a chicken and egg situation here getting out of the ground with a completely fresh talent with our own hosted authentication provider.

**[09:18](https://youtube.com/watch?v=sPUkAm7yDlU&t=558s)** And this is one of the caveats you need to be aware of of this entire solution is batteries are not included.

**[09:23](https://youtube.com/watch?v=sPUkAm7yDlU&t=563s)** It's if it goes wrong, it's kind of up to you. Whereas if Google's auth goes down, a lot of the internet goes down and they'll probably fix it pretty quickly.

**[09:31](https://youtube.com/watch?v=sPUkAm7yDlU&t=571s)** But if your self hosted IDP provider goes down, it's one of you to fix it. So you own the data, but you also own the outages as well.

**[09:39](https://youtube.com/watch?v=sPUkAm7yDlU&t=579s)** Just, you know, here be dragons. All right. So we have Docker running on this. This is the VPS again.

**[09:45](https://youtube.com/watch?v=sPUkAm7yDlU&t=585s)** Remember, this is the the droplet. I'm going to create a file here called compose.yaml. I'm going to insert this entire contents of this file into into that file.

**[09:55](https://youtube.com/watch?v=sPUkAm7yDlU&t=595s)** You can use nano vim whatever you want and then do a Docker compose pull.

**[10:00](https://youtube.com/watch?v=sPUkAm7yDlU&t=600s)** And this should pull down the latest pocket ID and traffic images from Docker hub.

**[10:05](https://youtube.com/watch?v=sPUkAm7yDlU&t=605s)** Shouldn't take two terribly long. Then once that's done, we'll do a Docker compose up.

**[10:10](https://youtube.com/watch?v=sPUkAm7yDlU&t=610s)** Well, we'll do a minus D and then we'll follow that with a logs minus F so that we can see what's going on in the background.

**[10:18](https://youtube.com/watch?v=sPUkAm7yDlU&t=618s)** And in theory, we should now be able to go to wait, I forgot something really important.

**[10:25](https://youtube.com/watch?v=sPUkAm7yDlU&t=625s)** We need to actually configure the ID domain, the DNS part of it, right?

**[10:30](https://youtube.com/watch?v=sPUkAm7yDlU&t=630s)** So let's go into the zone that the InterTech Labs.dev DNS zone, we create an A record pointing at this specific container.

**[10:39](https://youtube.com/watch?v=sPUkAm7yDlU&t=639s)** So our public IP address is this copy that from our droplet. And we're going to put this into we'll put this into Cloud Flare for ID and then we'll put the IP address in here.

**[10:49](https://youtube.com/watch?v=sPUkAm7yDlU&t=649s)** So id.inittechlabs.dev now points to 45 dot whatever, click save.

**[10:55](https://youtube.com/watch?v=sPUkAm7yDlU&t=655s)** And now we should be able to go to id.inittechlabs.dev in theory.

**[11:03](https://youtube.com/watch?v=sPUkAm7yDlU&t=663s)** And there you go. We've got pocket ID spun up. Easiest that. So this login URL won't help us.

**[11:09](https://youtube.com/watch?v=sPUkAm7yDlU&t=669s)** We actually on our first run need to go to slash setup and configure pocket ID for the very first time.

**[11:15](https://youtube.com/watch?v=sPUkAm7yDlU&t=675s)** So let's do continue and we are immediately logged in which is completely fresh instance.

**[11:21](https://youtube.com/watch?v=sPUkAm7yDlU&t=681s)** So all of the all of the defaults are still completely box fresh and click on add pass key.

**[11:28](https://youtube.com/watch?v=sPUkAm7yDlU&t=688s)** Now it's going to give me a few options of where to store this.

**[11:31](https://youtube.com/watch?v=sPUkAm7yDlU&t=691s)** You can store this if you have a password manager installed into your browser session like bit warden or one password or whatever.

**[11:38](https://youtube.com/watch?v=sPUkAm7yDlU&t=698s)** You can install the pass key there. You could install it into your Google password manager built into chrome.

**[11:44](https://youtube.com/watch?v=sPUkAm7yDlU&t=704s)** Your iCloud keychain or a physical hardware device if you have like a you be key or something like that.

**[11:50](https://youtube.com/watch?v=sPUkAm7yDlU&t=710s)** Just for the ease of use right now I'm going to use iCloud keychain because I can use touch ID on my laptop right here.

**[11:56](https://youtube.com/watch?v=sPUkAm7yDlU&t=716s)** As the authentication method for this so iCloud keychain pass key.

**[12:01](https://youtube.com/watch?v=sPUkAm7yDlU&t=721s)** That's how I now authenticate myself with pocket ID and tail scale shortly.

**[12:07](https://youtube.com/watch?v=sPUkAm7yDlU&t=727s)** All right, so we have no users configured in here though. I suppose technically we have the admin user configured out of the box.

**[12:13](https://youtube.com/watch?v=sPUkAm7yDlU&t=733s)** What if we wanted something a little more real.

**[12:16](https://youtube.com/watch?v=sPUkAm7yDlU&t=736s)** Let's go to add user. I'm going to create this one as a bill number.

**[12:23](https://youtube.com/watch?v=sPUkAm7yDlU&t=743s)** Is it bug? Let's do that.

**[12:25](https://youtube.com/watch?v=sPUkAm7yDlU&t=745s)** We'll do bill at intetlabs.dev. Wait, user name bill bill at intetlabs.dev.

**[12:34](https://youtube.com/watch?v=sPUkAm7yDlU&t=754s)** Just for my simplicity, I'll give it admin privileges though. I don't recommend necessarily giving this particular user admin privileges unless you need to.

**[12:43](https://youtube.com/watch?v=sPUkAm7yDlU&t=763s)** Then I'm going to click on save.

**[12:45](https://youtube.com/watch?v=sPUkAm7yDlU&t=765s)** We've successfully created the new user of bill but there's no pass key assigned to bill so we can't log in and authenticate as bill.

**[12:53](https://youtube.com/watch?v=sPUkAm7yDlU&t=773s)** Again, a bit of a catch 22 and this whole self hosted authentication world is full of them.

**[12:59](https://youtube.com/watch?v=sPUkAm7yDlU&t=779s)** You've got to be really careful you don't lock yourself out of things because it's a very easy thing to do but such is life.

**[13:06](https://youtube.com/watch?v=sPUkAm7yDlU&t=786s)** What we need to do is click on this three dot menu here under the user section in pocket ID and get a login code.

**[13:12](https://youtube.com/watch?v=sPUkAm7yDlU&t=792s)** This is a one time thing and it expires after one hour so don't take too long to use this code.

**[13:19](https://youtube.com/watch?v=sPUkAm7yDlU&t=799s)** We're now logged out as admin and now I'm going to go to that URL that was on my clipboard and sign in as bill lumber.

**[13:27](https://youtube.com/watch?v=sPUkAm7yDlU&t=807s)** Next, I want to add another pass key so we've got one pass key per account.

**[13:32](https://youtube.com/watch?v=sPUkAm7yDlU&t=812s)** I'm going to create a new one. You can save this. I want to save this another way.

**[13:37](https://youtube.com/watch?v=sPUkAm7yDlU&t=817s)** I don't want to use the Google password manager. I want to again use the iCloud keychain and use my touch ID. There we go.

**[13:45](https://youtube.com/watch?v=sPUkAm7yDlU&t=825s)** An iCloud keychain password.

**[13:48](https://youtube.com/watch?v=sPUkAm7yDlU&t=828s)** Now I have a pass key assigned to the admin user for my pocket ID instance and also a pass key assigned to the bill lumber user in my pocket ID instance.

**[14:01](https://youtube.com/watch?v=sPUkAm7yDlU&t=841s)** Confused yet? Good.

**[14:04](https://youtube.com/watch?v=sPUkAm7yDlU&t=844s)** It's a bit of a minefield but once you do it a couple of times and get your head around it you should be fine.

**[14:10](https://youtube.com/watch?v=sPUkAm7yDlU&t=850s)** Just to check that that took and everything works properly let's log out as the bill user and authenticate once more.

**[14:15](https://youtube.com/watch?v=sPUkAm7yDlU&t=855s)** You see I'm giving the option now to log in as either admin or bill and authenticate using touch ID again with my finger and I'm now logged in as bill.

**[14:26](https://youtube.com/watch?v=sPUkAm7yDlU&t=866s)** Pretty easy, right?

**[14:28](https://youtube.com/watch?v=sPUkAm7yDlU&t=868s)** Okay, so what do we want to do? We want to go right the way back to the beginning now and find this nice little option that says sign up with OIDC.

**[14:37](https://youtube.com/watch?v=sPUkAm7yDlU&t=877s)** Remember this all the way from the beginning?

**[14:40](https://youtube.com/watch?v=sPUkAm7yDlU&t=880s)** There's a phrase in consulting that I came across a few years ago called yak shaving and this video is the definition of yak shaving.

**[14:50](https://youtube.com/watch?v=sPUkAm7yDlU&t=890s)** In order to set up a custom OIDC provider we need a domain name which means we need DNS which means we need a place to run our pocket ID instance on the public internet which means you get the idea.

**[15:02](https://youtube.com/watch?v=sPUkAm7yDlU&t=902s)** Now there's one more thing that we've got to do which I'm going to deliberately make this fail in order to show you what's going to happen.

**[15:07](https://youtube.com/watch?v=sPUkAm7yDlU&t=907s)** So I'm going to put in bill at any tech labs dot dev and is going to look for a piece of content to verify my ownership of the domain under dot well known slash web finger.

**[15:19](https://youtube.com/watch?v=sPUkAm7yDlU&t=919s)** There isn't a way to do this automatically but if I click on get OIDC issuer you can see that it fails because there is no web finger end point on that domain.

**[15:29](https://youtube.com/watch?v=sPUkAm7yDlU&t=929s)** Like it doesn't exist we haven't created a web server that's going to host that thing.

**[15:32](https://youtube.com/watch?v=sPUkAm7yDlU&t=932s)** So let's fix that and we can do that pretty easily with a little nginx container.

**[15:37](https://youtube.com/watch?v=sPUkAm7yDlU&t=937s)** So we're going to add this to our docker compose file.

**[15:40](https://youtube.com/watch?v=sPUkAm7yDlU&t=940s)** In fact there's a bunch of cropped in here that we don't need.

**[15:43](https://youtube.com/watch?v=sPUkAm7yDlU&t=943s)** So let's just delete those lines obviously what you find in the git repo will have all of this removed already.

**[15:48](https://youtube.com/watch?v=sPUkAm7yDlU&t=948s)** But this is actually the code that I used to host those scripts I talked about earlier in the video on another digital ocean VPS.

**[15:55](https://youtube.com/watch?v=sPUkAm7yDlU&t=955s)** Funnily enough I'm just going to call this one web finger because that's literally all it's going to do.

**[16:00](https://youtube.com/watch?v=sPUkAm7yDlU&t=960s)** And then at data path well I suppose it matters but I'll just call it opt app data.

**[16:05](https://youtube.com/watch?v=sPUkAm7yDlU&t=965s)** And then web finger because we're going to need to create a file shortly to handle the contents of the web finger request to prove that I own the domain.

**[16:15](https://youtube.com/watch?v=sPUkAm7yDlU&t=975s)** So I'm going to say it's back into the droplet here and I'm going to make a directory with make minus p opt app data web finger.

**[16:25](https://youtube.com/watch?v=sPUkAm7yDlU&t=985s)** And then dot well known and that should be all it's looking for right.

**[16:31](https://youtube.com/watch?v=sPUkAm7yDlU&t=991s)** I think yes well known slash web finger the file name is web finger.

**[16:36](https://youtube.com/watch?v=sPUkAm7yDlU&t=996s)** So with that done I'm now going to see the into that directory of course and then dot well known.

**[16:43](https://youtube.com/watch?v=sPUkAm7yDlU&t=1003s)** And then create the file web finger and I'm going to put into it the following contents.

**[16:48](https://youtube.com/watch?v=sPUkAm7yDlU&t=1008s)** And I'm going to update the subject with the email to be bill at in it tech labs dot dev.

**[16:55](https://youtube.com/watch?v=sPUkAm7yDlU&t=1015s)** And the value of this issue URL needs to match what is configured in your VS code window earlier.

**[17:02](https://youtube.com/watch?v=sPUkAm7yDlU&t=1022s)** So this ID dot in it tech labs dot dev and we can include the HTTPS in there as well.

**[17:08](https://youtube.com/watch?v=sPUkAm7yDlU&t=1028s)** So let's just take that value and paste that onto our clipboard and we'll change to so CT and then quote mark in VIM.

**[17:16](https://youtube.com/watch?v=sPUkAm7yDlU&t=1036s)** And I'll replace that entire string with what we need right here.

**[17:20](https://youtube.com/watch?v=sPUkAm7yDlU&t=1040s)** So now I just need to modify my Docker compose file real quick.

**[17:26](https://youtube.com/watch?v=sPUkAm7yDlU&t=1046s)** So edit compose dot yellow and just add in that extra line for the engine X service.

**[17:33](https://youtube.com/watch?v=sPUkAm7yDlU&t=1053s)** So I'm going to delete everything and then just paste in the entire file do a Docker compose up.

**[17:38](https://youtube.com/watch?v=sPUkAm7yDlU&t=1058s)** Minus D and it's going to pull down the latest engine X image and run web finger at what we didn't configure that yet.

**[17:46](https://youtube.com/watch?v=sPUkAm7yDlU&t=1066s)** Again we need to jump back to cloud flare and add at the root of our domain.

**[17:51](https://youtube.com/watch?v=sPUkAm7yDlU&t=1071s)** So we can use the at symbol here and we're going to put in we're going to put in 45.55.91.245 which is the address of our pocket ID instance.

**[18:02](https://youtube.com/watch?v=sPUkAm7yDlU&t=1082s)** And so now in theory at least if we go back to our sign up page for the OIDC side of things we should be able to query the web finger using tail scale.

**[18:13](https://youtube.com/watch?v=sPUkAm7yDlU&t=1093s)** And it worked OK so the well known stuff and the web finger stuff is now good to go but what we've got to do next is create the client ID and client secret.

**[18:23](https://youtube.com/watch?v=sPUkAm7yDlU&t=1103s)** But it basically create tail scale as an app inside of pocket ID.

**[18:28](https://youtube.com/watch?v=sPUkAm7yDlU&t=1108s)** So let's head back over to our pocket ID instance get authenticated as bill lumber.

**[18:35](https://youtube.com/watch?v=sPUkAm7yDlU&t=1115s)** Here we go.

**[18:37](https://youtube.com/watch?v=sPUkAm7yDlU&t=1117s)** And next we want to configure an OIDC client so on the left menu down here click on OIDC clients.

**[18:45](https://youtube.com/watch?v=sPUkAm7yDlU&t=1125s)** And this is why at the beginning at least it's important that bill is an admin user because you can configure these things in pocket ID.

**[18:52](https://youtube.com/watch?v=sPUkAm7yDlU&t=1132s)** But later on you probably want to have a separate browser session or profile and manage these things separately from the user who you are authenticating as just to separate concerns that kind of thing.

**[19:03](https://youtube.com/watch?v=sPUkAm7yDlU&t=1143s)** But let's add an OIDC client.

**[19:05](https://youtube.com/watch?v=sPUkAm7yDlU&t=1145s)** We want to do tail scale right here and let's look in the tail scale OIDC documentation for the callback URL.

**[19:13](https://youtube.com/watch?v=sPUkAm7yDlU&t=1153s)** I should say by the way there's an entire page dedicated in our documentation to doing this.

**[19:18](https://youtube.com/watch?v=sPUkAm7yDlU&t=1158s)** But I know some people prefer a video so that's why I'm making this.

**[19:22](https://youtube.com/watch?v=sPUkAm7yDlU&t=1162s)** Here is the callback URL that we need.

**[19:24](https://youtube.com/watch?v=sPUkAm7yDlU&t=1164s)** So let's paste this now into our OIDC clients page.

**[19:28](https://youtube.com/watch?v=sPUkAm7yDlU&t=1168s)** And let's also just give this an extra little bit of spice.

**[19:32](https://youtube.com/watch?v=sPUkAm7yDlU&t=1172s)** Let's go to dashboard icons.com and search for tail scale.

**[19:38](https://youtube.com/watch?v=sPUkAm7yDlU&t=1178s)** By the way this is a fantastic resource if you need icons for any of your self host applications for like a dashboard or whatever.

**[19:44](https://youtube.com/watch?v=sPUkAm7yDlU&t=1184s)** This one's my favorite that exists on the internet.

**[19:47](https://youtube.com/watch?v=sPUkAm7yDlU&t=1187s)** And now we're going to go and download the light theme PNG.

**[19:52](https://youtube.com/watch?v=sPUkAm7yDlU&t=1192s)** Sure. Why not?

**[19:53](https://youtube.com/watch?v=sPUkAm7yDlU&t=1193s)** No, let's do let's do dark theme PNG.

**[19:56](https://youtube.com/watch?v=sPUkAm7yDlU&t=1196s)** I used to be indecisive, but I'm not so sure anymore.

**[19:59](https://youtube.com/watch?v=sPUkAm7yDlU&t=1199s)** All right, let's upload the logo and voila.

**[20:02](https://youtube.com/watch?v=sPUkAm7yDlU&t=1202s)** We have the tail scale logo. We have our callback URL.

**[20:05](https://youtube.com/watch?v=sPUkAm7yDlU&t=1205s)** I'm going to click on save and it's going to give me now a client ID.

**[20:09](https://youtube.com/watch?v=sPUkAm7yDlU&t=1209s)** I'm going to go back to my first tab.

**[20:11](https://youtube.com/watch?v=sPUkAm7yDlU&t=1211s)** I hope you're still with me and paste in the client ID.

**[20:15](https://youtube.com/watch?v=sPUkAm7yDlU&t=1215s)** And then get my client secret.

**[20:17](https://youtube.com/watch?v=sPUkAm7yDlU&t=1217s)** And again, paste that in right here.

**[20:19](https://youtube.com/watch?v=sPUkAm7yDlU&t=1219s)** And then don't worry about any of these prompts.

**[20:21](https://youtube.com/watch?v=sPUkAm7yDlU&t=1221s)** Leave the default, leave non, leave login, leave select just just leave consent checked.

**[20:26](https://youtube.com/watch?v=sPUkAm7yDlU&t=1226s)** And then click sign up with OIDC and all being well and good.

**[20:31](https://youtube.com/watch?v=sPUkAm7yDlU&t=1231s)** You just signed up for tail scale with a custom OIDC provider.

**[20:38](https://youtube.com/watch?v=sPUkAm7yDlU&t=1238s)** So you now own the authentication for this tail net completely.

**[20:42](https://youtube.com/watch?v=sPUkAm7yDlU&t=1242s)** There's no third party big tech involved in there at all.

**[20:46](https://youtube.com/watch?v=sPUkAm7yDlU&t=1246s)** So personal use, let's just skip all of this stuff because I have used tail scale before.

**[20:51](https://youtube.com/watch?v=sPUkAm7yDlU&t=1251s)** And I'm going to add my first device up here.

**[20:54](https://youtube.com/watch?v=sPUkAm7yDlU&t=1254s)** So just in the same way that you would add any other device,

**[20:58](https://youtube.com/watch?v=sPUkAm7yDlU&t=1258s)** I'm going to go and account settings, click on add account.

**[21:01](https://youtube.com/watch?v=sPUkAm7yDlU&t=1261s)** It's going to take me into a browser to authenticate.

**[21:04](https://youtube.com/watch?v=sPUkAm7yDlU&t=1264s)** I'm going to add the device ball trick to the the inner tech labs tail net.

**[21:09](https://youtube.com/watch?v=sPUkAm7yDlU&t=1269s)** And voila.

**[21:11](https://youtube.com/watch?v=sPUkAm7yDlU&t=1271s)** You can see this device is now authenticated and owned by Bill at inner tech labs.dev.

**[21:16](https://youtube.com/watch?v=sPUkAm7yDlU&t=1276s)** There's a bunch of stuff you can configure on a brand new tail net.

**[21:19](https://youtube.com/watch?v=sPUkAm7yDlU&t=1279s)** But that really is beyond the scope of today's video.

**[21:21](https://youtube.com/watch?v=sPUkAm7yDlU&t=1281s)** One thing you might want to do is just select a plan.

**[21:24](https://youtube.com/watch?v=sPUkAm7yDlU&t=1284s)** If this is a brand new tail net, we do have pricing options available.

**[21:27](https://youtube.com/watch?v=sPUkAm7yDlU&t=1287s)** Like if you want to bring tail scale to work, you can go to tailscale.com slash BTW

**[21:31](https://youtube.com/watch?v=sPUkAm7yDlU&t=1291s)** to find out more about what all of these different pricing options will unlock for you.

**[21:36](https://youtube.com/watch?v=sPUkAm7yDlU&t=1296s)** But our personal plan is very generous.

**[21:38](https://youtube.com/watch?v=sPUkAm7yDlU&t=1298s)** Three users and 100 devices for free.

**[21:40](https://youtube.com/watch?v=sPUkAm7yDlU&t=1300s)** I'm going to click on I understand these terms and end my free enterprise trial.

**[21:44](https://youtube.com/watch?v=sPUkAm7yDlU&t=1304s)** And click on choose personal plan.

**[21:47](https://youtube.com/watch?v=sPUkAm7yDlU&t=1307s)** So under my machines page, I could now just treat this like any other tail net,

**[21:50](https://youtube.com/watch?v=sPUkAm7yDlU&t=1310s)** except for the fact that I authenticate using pocket ID.

**[21:53](https://youtube.com/watch?v=sPUkAm7yDlU&t=1313s)** So let's just do that one more time because it's kind of exciting for me to do this still.

**[21:57](https://youtube.com/watch?v=sPUkAm7yDlU&t=1317s)** And so I'm going to log out as Bill.

**[21:59](https://youtube.com/watch?v=sPUkAm7yDlU&t=1319s)** But I also need to log out from pocket ID as well.

**[22:02](https://youtube.com/watch?v=sPUkAm7yDlU&t=1322s)** Because remember, it shares the token between effectively multiple different tabs.

**[22:07](https://youtube.com/watch?v=sPUkAm7yDlU&t=1327s)** So if I now go to tailscale.com, and I click signing with a passkey,

**[22:11](https://youtube.com/watch?v=sPUkAm7yDlU&t=1331s)** you might be a little confused and think, this is how I sign in now.

**[22:14](https://youtube.com/watch?v=sPUkAm7yDlU&t=1334s)** But actually, no, you want to sign in with Bill at InitectLabs.dev.

**[22:18](https://youtube.com/watch?v=sPUkAm7yDlU&t=1338s)** Click sign in.

**[22:19](https://youtube.com/watch?v=sPUkAm7yDlU&t=1339s)** And now tail scale knows that that's a custom OIDC provider tail net.

**[22:24](https://youtube.com/watch?v=sPUkAm7yDlU&t=1344s)** So it's going to ask me to sign in with the callback URL and all that kind of stuff.

**[22:27](https://youtube.com/watch?v=sPUkAm7yDlU&t=1347s)** Click on Bill, put my finger print in.

**[22:35](https://youtube.com/watch?v=sPUkAm7yDlU&t=1355s)** And it's as easy as that.

**[22:37](https://youtube.com/watch?v=sPUkAm7yDlU&t=1357s)** So again, lots of chapters down below.

**[22:39](https://youtube.com/watch?v=sPUkAm7yDlU&t=1359s)** I know that was a super long, complicated exercise in in yak shaving.

**[22:44](https://youtube.com/watch?v=sPUkAm7yDlU&t=1364s)** But that's just the reality of setting up your own custom OIDC provider.

**[22:48](https://youtube.com/watch?v=sPUkAm7yDlU&t=1368s)** That's why we provide several out of the box.

**[22:51](https://youtube.com/watch?v=sPUkAm7yDlU&t=1371s)** OAuth providers from Google, Microsoft, Apple, GitHub.

**[22:54](https://youtube.com/watch?v=sPUkAm7yDlU&t=1374s)** Because this stuff is complicated.

**[22:56](https://youtube.com/watch?v=sPUkAm7yDlU&t=1376s)** It can be difficult to set up your own infrastructure in a highly available way.

**[23:00](https://youtube.com/watch?v=sPUkAm7yDlU&t=1380s)** And in fact, even pocket ID itself isn't a highly available service.

**[23:04](https://youtube.com/watch?v=sPUkAm7yDlU&t=1384s)** If that droplet goes down, I can't sign into my tail net anymore.

**[23:08](https://youtube.com/watch?v=sPUkAm7yDlU&t=1388s)** So just make sure before you take this path, before you walk this path,

**[23:12](https://youtube.com/watch?v=sPUkAm7yDlU&t=1392s)** you fully understood all of the ramifications of hosting your own identity.

**[23:17](https://youtube.com/watch?v=sPUkAm7yDlU&t=1397s)** I would hate for you to be locked out from your tail net simply because a droplet went down for some reason.

**[23:22](https://youtube.com/watch?v=sPUkAm7yDlU&t=1402s)** So yeah, there's just a lot to it.

**[23:24](https://youtube.com/watch?v=sPUkAm7yDlU&t=1404s)** There's a lot to consider.

**[23:26](https://youtube.com/watch?v=sPUkAm7yDlU&t=1406s)** And I wanted to make this video really just to show you what's possible with these passkeys.

**[23:29](https://youtube.com/watch?v=sPUkAm7yDlU&t=1409s)** Because you can configure pocket ID to work with a lot of self-hosted apps.

**[23:33](https://youtube.com/watch?v=sPUkAm7yDlU&t=1413s)** As well, in fact, I was just playing around with Kara Keep the other day.

**[23:36](https://youtube.com/watch?v=sPUkAm7yDlU&t=1416s)** And it was really playing around with that and hooking that up with OAuth,

**[23:40](https://youtube.com/watch?v=sPUkAm7yDlU&t=1420s)** that was the genesis and the seed of the idea of this video.

**[23:43](https://youtube.com/watch?v=sPUkAm7yDlU&t=1423s)** If you want to self-host your own OAuth, go for it.

**[23:46](https://youtube.com/watch?v=sPUkAm7yDlU&t=1426s)** Be my guest. I would absolutely love to hear from you in the comments down below

**[23:49](https://youtube.com/watch?v=sPUkAm7yDlU&t=1429s)** if you've done that successfully too.

**[23:52](https://youtube.com/watch?v=sPUkAm7yDlU&t=1432s)** But just be aware of the pitfalls.

**[23:54](https://youtube.com/watch?v=sPUkAm7yDlU&t=1434s)** So you have been warned.

**[23:56](https://youtube.com/watch?v=sPUkAm7yDlU&t=1436s)** And as always, thank you so much for watching.

**[23:58](https://youtube.com/watch?v=sPUkAm7yDlU&t=1438s)** I've been Alex from TaleScale.

---

*Automatically generated transcript. May contain errors.*
