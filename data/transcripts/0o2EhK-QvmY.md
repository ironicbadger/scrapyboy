---
video_id: "0o2EhK-QvmY"
title: "Remotely access your Synology from anywhere with Tailscale"
description: "In today's video I'll walk you through setting up Tailscale on your Synology, including automated updates and TLS certificates. If you've been curious about how to remotely access your self-hosted sto..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-10-22"
duration_seconds: 898
youtube_url: "https://www.youtube.com/watch?v=0o2EhK-QvmY"
thumbnail_url: "https://i.ytimg.com/vi/0o2EhK-QvmY/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T18:04:07.822637"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2754
transcription_time_seconds: 24.7
---

# Remotely access your Synology from anywhere with Tailscale

**[00:00](https://youtube.com/watch?v=0o2EhK-QvmY&t=0s)** If you have a Synology NAS and want to securely access it from outside your home network, then how would you do that today? Well, one option is to put your NAS by extension your data onto the public internet, poking holes in your firewall or port-forwarding, perhaps. This is a big no-no from a security perspective, though, not to mention totally unnecessary with Tailscale, which creates a private and secure network of devices that we call a tailnet. Tailscale creates a private mesh network between all of your

**[00:30](https://youtube.com/watch?v=0o2EhK-QvmY&t=30s)** devices, even ones behind firewalls using our natural versatile technology and encrypted WireGuard tunnels behind the scenes. This means that you and only you can connect to your Synology whether you're at home, at the office, on the train, or even on vacation and want to back up your holiday photos. Pretty much any way you have an internet connection, Tailscale can establish a direct secure connection back to your Synology at home, or wherever it happens to be, without exposing anything to the wild of the public internet.

**[01:00](https://youtube.com/watch?v=0o2EhK-QvmY&t=60s)** So in today's video, I'll show you how to get started with Tailscale for free and configure it on your Synology, will also configure auto updates and how to create an HTTPS certificate with the TS.net domain name that every tailnet gets for free.

**[01:14](https://youtube.com/watch?v=0o2EhK-QvmY&t=74s)** If you're brand new to Tailscale, I'm just going to take a second to tell you that we make clients not only for Synology, but also for Mac, Windows, Linux, iOS, Android, Fire TVs, Apple TVs, it can even run on a robot vacuum.

**[01:32](https://youtube.com/watch?v=0o2EhK-QvmY&t=92s)** Pretty much any way you can think of, there is a Tailscale client available. The advantage of installing Tailscale directly on each client is that you can establish direct device to device connections without any complicated networking rules.

**[01:45](https://youtube.com/watch?v=0o2EhK-QvmY&t=105s)** You can also then pick that device up and take it to a different physical network from this house to a parent's house or something, and the two will just find each other and connect over the tailnet.

**[01:57](https://youtube.com/watch?v=0o2EhK-QvmY&t=117s)** But today's video is all about Synology, so I'm going to be using DSM 7, and I think this is the latest update at the time of recording for my particular Synology box, the DS 1621 Plus.

**[02:09](https://youtube.com/watch?v=0o2EhK-QvmY&t=129s)** I'm running DSM 7.2.169057 update 5. No idea if that's important. I'm not exactly a Synology power user, but I do know that this is up to date and when I check for updates, there will no more available.

**[02:25](https://youtube.com/watch?v=0o2EhK-QvmY&t=145s)** So, first thing we want to do is jump into the Synology Package Center. I have mine on the desktop, but you can just as easily open up your package search thing that Synology has in the browser and look under the Package Center for Tailscale.

**[02:42](https://youtube.com/watch?v=0o2EhK-QvmY&t=162s)** Funny story. This is actually how I first interacted with Tailscale as a user before I worked here many years ago now.

**[02:50](https://youtube.com/watch?v=0o2EhK-QvmY&t=170s)** When installing is really easy, you just search for it and click on the install button, wait for it to download and install, which only takes a moment.

**[02:58](https://youtube.com/watch?v=0o2EhK-QvmY&t=178s)** Then we're going to need to authenticate this node to your tailnet, so you're going to need a tailnet in order for this to work.

**[03:05](https://youtube.com/watch?v=0o2EhK-QvmY&t=185s)** So, whilst that's installing in the background, let's jump over to tailscale.com and just see what's required.

**[03:11](https://youtube.com/watch?v=0o2EhK-QvmY&t=191s)** Up here in the top right hand corner, you can see there's a button here that says admin console. That only shows up because I've already got a tailnet created and logged in.

**[03:19](https://youtube.com/watch?v=0o2EhK-QvmY&t=199s)** If I log out and go to tailscale.com, this might be you if you're completely brand new, you'll see a login button.

**[03:26](https://youtube.com/watch?v=0o2EhK-QvmY&t=206s)** That's fine. You can go ahead and sign up here with your Google account, Microsoft, GitHub, whatever you want to use as your authentication provider.

**[03:34](https://youtube.com/watch?v=0o2EhK-QvmY&t=214s)** Tailscale deliberately doesn't want your password. We hand off that authentication piece to what are called OIDC providers.

**[03:42](https://youtube.com/watch?v=0o2EhK-QvmY&t=222s)** Again, that's an implementation detail. It's not terribly important, but just know that your credentials live with these providers and not tailscale directly.

**[03:50](https://youtube.com/watch?v=0o2EhK-QvmY&t=230s)** The private keys on tailscale devices also never leave the device themselves, so everything is completely secure from that perspective too.

**[03:59](https://youtube.com/watch?v=0o2EhK-QvmY&t=239s)** The signing process is quite straightforward, so I'm going to click signing with Google.

**[04:03](https://youtube.com/watch?v=0o2EhK-QvmY&t=243s)** I'm already logged in in this Chrome session with my Google account, as I imagine most people are.

**[04:08](https://youtube.com/watch?v=0o2EhK-QvmY&t=248s)** You'll see this choosing account option, and then you can see I've got five devices currently in my tailnet.

**[04:13](https://youtube.com/watch?v=0o2EhK-QvmY&t=253s)** What we're going to do is add this Synology NAS into my existing tailnet, where I've already got the handful of other devices.

**[04:21](https://youtube.com/watch?v=0o2EhK-QvmY&t=261s)** I go back to this other tab and click on the open button. This is going to open another tab where it's going to ask us to re-authenticate this node.

**[04:29](https://youtube.com/watch?v=0o2EhK-QvmY&t=269s)** In actual fact, we're not reauthenticating. We're just authenticating. It's just a terminology, weirdness there.

**[04:35](https://youtube.com/watch?v=0o2EhK-QvmY&t=275s)** Click on the reauthenticate button, and this is going to take you into your tailscale console connect device page.

**[04:42](https://youtube.com/watch?v=0o2EhK-QvmY&t=282s)** If you're happy with everything, you can just check any of the node keys, the host names, the operating system, etc.

**[04:48](https://youtube.com/watch?v=0o2EhK-QvmY&t=288s)** Just click on the big blue connect button.

**[04:50](https://youtube.com/watch?v=0o2EhK-QvmY&t=290s)** What you'll notice is that your Synology node, in my case, Octonaz, now shows up as a node in your tailnet connected,

**[04:57](https://youtube.com/watch?v=0o2EhK-QvmY&t=297s)** running the client version 1.58.2 on the Linux kernel 4.4.

**[05:03](https://youtube.com/watch?v=0o2EhK-QvmY&t=303s)** Each node gets a dedicated IP address in the 100.ip namespace. It also gets an IPv6 address, if you care about that kind of thing.

**[05:11](https://youtube.com/watch?v=0o2EhK-QvmY&t=311s)** We also give you a fully qualified domain name, which we'll come onto a little bit later, as well as a short DNS name.

**[05:18](https://youtube.com/watch?v=0o2EhK-QvmY&t=318s)** I can now access my Synology over tailscale without doing anything further, because I am logged in as a client device on this laptop in this tailnet.

**[05:31](https://youtube.com/watch?v=0o2EhK-QvmY&t=331s)** So a tail in scales at gmail.com, I already authenticated my Mac by installing tailscale on my Mac, doing the same login dance that we just did on this Synology.

**[05:40](https://youtube.com/watch?v=0o2EhK-QvmY&t=340s)** And now I can connect these two devices together, wherever my laptop is, I can now connect to that Synology, regardless of what files are in the way, what Wi-Fi I'm connected to, etc.

**[05:51](https://youtube.com/watch?v=0o2EhK-QvmY&t=351s)** I just need to make sure I'm connected to this tailnet, and you can see that this device, Baldric, is in this tailnet here.

**[05:57](https://youtube.com/watch?v=0o2EhK-QvmY&t=357s)** MVP Baldric is connected as is Octonaz, and that's how the two talk together.

**[06:03](https://youtube.com/watch?v=0o2EhK-QvmY&t=363s)** Okay, so that's the basics of installing the tailscale client on your Synology box, taking care of.

**[06:08](https://youtube.com/watch?v=0o2EhK-QvmY&t=368s)** What we want to do now is set up an auto-updating task, so that you always have the most up to date version of the tailscale client on your Synology box.

**[06:18](https://youtube.com/watch?v=0o2EhK-QvmY&t=378s)** Sometimes the updates on the Synology App Store can take a few days or weeks behind what we've made available upstream.

**[06:24](https://youtube.com/watch?v=0o2EhK-QvmY&t=384s)** Now in order to work around that, what we can do is create a user-defined script to automatically update the tailscale client in the background for us.

**[06:33](https://youtube.com/watch?v=0o2EhK-QvmY&t=393s)** This will keep it in sync with what we've released upstream and not be beholden to the version that's currently in this Synology App Store.

**[06:39](https://youtube.com/watch?v=0o2EhK-QvmY&t=399s)** So jump into your control panel and then look for task scheduler down here.

**[06:45](https://youtube.com/watch?v=0o2EhK-QvmY&t=405s)** We want to create a brand new scheduled task. Click up here on the top left, create scheduled task, and then a user-defined script.

**[06:53](https://youtube.com/watch?v=0o2EhK-QvmY&t=413s)** In here, I'm going to call this tailscale update.

**[06:57](https://youtube.com/watch?v=0o2EhK-QvmY&t=417s)** The user needs to be root, because tailscale is running as root.

**[07:03](https://youtube.com/watch?v=0o2EhK-QvmY&t=423s)** Next, click on schedule, and we want to set this to just something regular, so weekly should be absolutely fine.

**[07:10](https://youtube.com/watch?v=0o2EhK-QvmY&t=430s)** I'm going to have this just run on the weekend of Sunday. Why not?

**[07:15](https://youtube.com/watch?v=0o2EhK-QvmY&t=435s)** It doesn't really matter what day you pick. Just pick one day a week and just have this task run once a week.

**[07:21](https://youtube.com/watch?v=0o2EhK-QvmY&t=441s)** Next, we want to run under the task settings. We want to put the command in of tailscale update dash dash yes.

**[07:30](https://youtube.com/watch?v=0o2EhK-QvmY&t=450s)** What this will do is it will go out to the tailscale service, check for an update, and install it if one is available.

**[07:36](https://youtube.com/watch?v=0o2EhK-QvmY&t=456s)** The dash dash yes allows for unattended updates if you're not physically present, which you won't be when the script is running behind the scenes.

**[07:43](https://youtube.com/watch?v=0o2EhK-QvmY&t=463s)** And that's it. We just need to click OK, and it's going to give us a big warning saying, modifying system configurations blah, blah, blah.

**[07:50](https://youtube.com/watch?v=0o2EhK-QvmY&t=470s)** Please make sure you are aware of the consequences before execution.

**[07:54](https://youtube.com/watch?v=0o2EhK-QvmY&t=474s)** I've just explained those for you. So I'm just going to put in my root password or my username for my DSM account and click on the submit button.

**[08:03](https://youtube.com/watch?v=0o2EhK-QvmY&t=483s)** Next, I actually want to just run this action right now just to show you what happens. If I click on run and then OK behind the scenes, this is going to be running that tailscale update command for us.

**[08:13](https://youtube.com/watch?v=0o2EhK-QvmY&t=493s)** And right away, the tailscale client jumped from version 1.58 to 1.76.

**[08:21](https://youtube.com/watch?v=0o2EhK-QvmY&t=501s)** So in this section, we're going to cover creating a certificate backed by tailscale and letting crypt to access your Synology NAS securely from anywhere with a trusted TLS HTTPS certificate.

**[08:34](https://youtube.com/watch?v=0o2EhK-QvmY&t=514s)** Now we created in the last chapter, we created the tailscale update command.

**[08:39](https://youtube.com/watch?v=0o2EhK-QvmY&t=519s)** This is important. You have to make sure that you're on at least client version 1.60 to check my notes 1.64 or newer. We're on 1.76, so we're all good to go there.

**[08:49](https://youtube.com/watch?v=0o2EhK-QvmY&t=529s)** But you do need to make sure you've got these regular updates taken care of before we proceed.

**[08:54](https://youtube.com/watch?v=0o2EhK-QvmY&t=534s)** Now, the next thing we want to do is on our tail that we want to make sure we've got a couple of things set up, first of all.

**[09:00](https://youtube.com/watch?v=0o2EhK-QvmY&t=540s)** So jump over to your tailscale admin console, get logged in at tailscale.com. Up here, along the top, there is a DNS option.

**[09:07](https://youtube.com/watch?v=0o2EhK-QvmY&t=547s)** We need to jump all the way down to the bottom of this page and enable, make sure that magic DNS is enabled and also make sure that HTTPS certificates are enabled as well.

**[09:17](https://youtube.com/watch?v=0o2EhK-QvmY&t=557s)** Then at the top of the page, I've already done this, but your name, if it's a brand new tailnet, will be like tail dash FAC123 or something dot TS dot net.

**[09:29](https://youtube.com/watch?v=0o2EhK-QvmY&t=569s)** Click on the rename tailnet button, and then you can see actually this is what my original name was tail six E five BF dot TS dot net.

**[09:38](https://youtube.com/watch?v=0o2EhK-QvmY&t=578s)** I much prefer the loss of rap to high for noodle fish. So you can go ahead and re roll your DNS names as many times as you would like in the initial phase, at least, to find name that better suits what you want it to be.

**[09:51](https://youtube.com/watch?v=0o2EhK-QvmY&t=591s)** Remember, this is a free service that tailscale provides doesn't cost you anything, but it means that you can actually access your synology with a fully qualified domain name, which is a necessity if you want to have a TLS certificate.

**[10:04](https://youtube.com/watch?v=0o2EhK-QvmY&t=604s)** The entire purpose of a TLS certificate is to verify identities, make sure that I'm talking to who I think I'm talking to on the other end and that that certificate gets signed by a certificate issuer in this case, let's encrypt say yes, Alex definitely owns that,

**[10:19](https://youtube.com/watch?v=0o2EhK-QvmY&t=619s)** also wrapped a high for noodle fish dot TS dot net. So we've gone ahead and done that, we can now either connect via SSH, but I'm not going to do that here because I want to do everything automatically for you moving forward.

**[10:30](https://youtube.com/watch?v=0o2EhK-QvmY&t=630s)** We're going to create another user defined script. So jump back to your control panel and then look for the what's it called task scheduler, then under create scheduled task, we're just going to create another user defined script.

**[10:44](https://youtube.com/watch?v=0o2EhK-QvmY&t=644s)** I'm just going to call this one tailscale cert and set the execution user to be root again. Now scheduling wise, let's encrypt certificates only last 90 days.

**[10:54](https://youtube.com/watch?v=0o2EhK-QvmY&t=654s)** So I'm going to run this task every month, which should be more than sufficient for what we need to do here. So I'm going to do run on the following days monthly, and then I'm just going to set again, I'm just going to set the first Monday of the month here.

**[11:10](https://youtube.com/watch?v=0o2EhK-QvmY&t=670s)** So once your scheduling page looks like this, this is going to run, obviously now on the first Monday of every month, under task settings, we need to put in the required field of what the command is we want to actually execute.

**[11:22](https://youtube.com/watch?v=0o2EhK-QvmY&t=682s)** In our case, we're going to do tailscale configure Synology hyphen cert. This is a special command that tailscale created just for this purpose to run on the Synologies.

**[11:34](https://youtube.com/watch?v=0o2EhK-QvmY&t=694s)** Now, I'm going to click OK, and again, it's going to give me that warning about making sure that I'm not going to explode some kittens or something.

**[11:41](https://youtube.com/watch?v=0o2EhK-QvmY&t=701s)** I'm going to click on submit. When that's done, I'm just going to run this action. Now, this might take a couple of minutes to come back from the Lexing crypt API to generate these certificates required.

**[11:53](https://youtube.com/watch?v=0o2EhK-QvmY&t=713s)** Now, we need to jump over to a different area of the control panel under security.

**[11:57](https://youtube.com/watch?v=0o2EhK-QvmY&t=717s)** We want to go and find that certificate that was just generated and install it into our Synology DSM software.

**[12:04](https://youtube.com/watch?v=0o2EhK-QvmY&t=724s)** As you can see, the certificate has been issued successfully and is valid until the 13th of January 2025.

**[12:13](https://youtube.com/watch?v=0o2EhK-QvmY&t=733s)** We're almost at 25. Oh, well.

**[12:16](https://youtube.com/watch?v=0o2EhK-QvmY&t=736s)** Now, we've generated the certificate. We need to tell Synology to use it. Click on action and then edit and then set as default certificate.

**[12:24](https://youtube.com/watch?v=0o2EhK-QvmY&t=744s)** If you want to, you can set this on a per service basis, but for my purposes, I want to create a nice simple tutorial.

**[12:31](https://youtube.com/watch?v=0o2EhK-QvmY&t=751s)** So I think just setting it as the default certificate is probably going to be the most sane thing for most people watching this video.

**[12:37](https://youtube.com/watch?v=0o2EhK-QvmY&t=757s)** Now, in order to get this new certificate actually working, I ended up having to delete the default certificate under this page here.

**[12:44](https://youtube.com/watch?v=0o2EhK-QvmY&t=764s)** And so even though I'd set the velociraptor.ts.net certificate as the default, for some reason it was still going back to my self-signed Synology certificate.

**[12:56](https://youtube.com/watch?v=0o2EhK-QvmY&t=776s)** I actually don't know why, but if you run into that issue, just try deleting the default certificate and hopefully everything will just work like it has for me.

**[13:06](https://youtube.com/watch?v=0o2EhK-QvmY&t=786s)** So in this other tab over here, look, we can see that I've now got a secure connection to octanas, velociraptor, noodle fish with a secure connection and a valid certificate.

**[13:17](https://youtube.com/watch?v=0o2EhK-QvmY&t=797s)** You can see this issue by electing crypt until Monday, January the 13th, 2025.

**[13:22](https://youtube.com/watch?v=0o2EhK-QvmY&t=802s)** Of course, the automation we set up to renew that certificate every month on the first Monday of every month should take care of that renewing before January the 13th.

**[13:31](https://youtube.com/watch?v=0o2EhK-QvmY&t=811s)** Now, those of you that have noticed there's a port number still on the end of this thing here, will know that I don't really like that.

**[13:38](https://youtube.com/watch?v=0o2EhK-QvmY&t=818s)** And typically I would recommend at this point you use something like tail scale serve to expose this with essentially what's a built in reverse proxy into tail scale to the rest of your talent without worrying about port numbers.

**[13:50](https://youtube.com/watch?v=0o2EhK-QvmY&t=830s)** But with a Synology, it redirects anyway. So I don't actually know how much value you gain from doing tail scale serve on a Synology.

**[14:00](https://youtube.com/watch?v=0o2EhK-QvmY&t=840s)** I'll put a link to a card. I'll just get the wrong side. It's up here. It's definitely up here.

**[14:05](https://youtube.com/watch?v=0o2EhK-QvmY&t=845s)** We have a video about tail scale serve and funnel if you're curious about that kind of thing.

**[14:10](https://youtube.com/watch?v=0o2EhK-QvmY&t=850s)** And there's a whole bunch more stuff you can do with tail scale, which we don't have time to get into in today's video.

**[14:15](https://youtube.com/watch?v=0o2EhK-QvmY&t=855s)** Check out all of the other videos and playlists and things we have here. I have a bunch of live streams as well.

**[14:20](https://youtube.com/watch?v=0o2EhK-QvmY&t=860s)** So if you want to come and join me on a live stream every couple of weeks and ask your questions, it can be about Synology.

**[14:25](https://youtube.com/watch?v=0o2EhK-QvmY&t=865s)** It can be about anything to do with tail scale and networking. I'll do my best to answer those for you in the live stream as well.

**[14:31](https://youtube.com/watch?v=0o2EhK-QvmY&t=871s)** So I hope today's video is useful. If you're a Synology user, let us know down in the comments what you want to see from tail scale on a Synology and we'll do our best to make that happen for you.

**[14:40](https://youtube.com/watch?v=0o2EhK-QvmY&t=880s)** And until next time, thank you so much for watching. I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
