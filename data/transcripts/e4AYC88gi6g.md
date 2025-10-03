---
video_id: "e4AYC88gi6g"
title: "Immich 2.0 is ready to replace Google Photos - Here's how to access it remotely"
description: "Immich 2.0 is here, and it is a huge milestone. This project has quickly become one of the most impressive self-hosted apps around, offering a real alternative to Google Photos that puts you in contro..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-10-03"
duration_seconds: 408
youtube_url: "https://www.youtube.com/watch?v=e4AYC88gi6g"
thumbnail_url: "https://i.ytimg.com/vi_webp/e4AYC88gi6g/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T15:47:24.255824"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1226
transcription_time_seconds: 11.0
---

# Immich 2.0 is ready to replace Google Photos - Here's how to access it remotely

**[00:00](https://youtube.com/watch?v=e4AYC88gi6g&t=0s)** The image project just hit a huge milestone this week with version 2.0. Officially, image is now stable.

**[00:08](https://youtube.com/watch?v=e4AYC88gi6g&t=8s)** My congratulations goes out to Alex and the team over at Futo who have been working towards this goal for 1337 days.

**[00:16](https://youtube.com/watch?v=e4AYC88gi6g&t=16s)** That's a very good nerd joke, by the way. I'll drop a link to their announcement in the description if you want to read the full details.

**[00:24](https://youtube.com/watch?v=e4AYC88gi6g&t=24s)** Now if you haven't come across image before, it's a self-hosted photo and video management tool, and you can kind of think of it a little bit like Google Photos

**[00:32](https://youtube.com/watch?v=e4AYC88gi6g&t=32s)** but if someone lifted that and put it onto hardware in your house, that you own and you can keep complete control of your library and your data too.

**[00:40](https://youtube.com/watch?v=e4AYC88gi6g&t=40s)** It's got features like face detection, automatic mobile device, backup, a beautiful web interface, geolocation, and I'm sure I'm missing a bunch of other cool features too.

**[00:51](https://youtube.com/watch?v=e4AYC88gi6g&t=51s)** Now that the project is officially stable though, it might actually be time to seriously consider dropping that expensive iCloud or Google Storage subscription.

**[01:00](https://youtube.com/watch?v=e4AYC88gi6g&t=60s)** Now this video isn't going to be a full setup guide, I've already got plenty of those covering how he set image up step by step and I'll link one here, which is part two of the self-hosting series I did recently on the channel.

**[01:12](https://youtube.com/watch?v=e4AYC88gi6g&t=72s)** I also did another one which I'll put a link to in the description down below showing how to use a remote GPU over tail scale to speed up initial image processing and search.

**[01:21](https://youtube.com/watch?v=e4AYC88gi6g&t=81s)** So when you're ingesting 100,000 photos from Google takeout, all in one go, you can actually use your gaming GPU to speed that process up and I'll put a link to that down below of course.

**[01:32](https://youtube.com/watch?v=e4AYC88gi6g&t=92s)** In this video I want to focus on how to remotely access image and some of the considerations you might want to consider when you're sharing image with a family or a wider friend group perhaps.

**[01:44](https://youtube.com/watch?v=e4AYC88gi6g&t=104s)** So if you run image on a home server you will quickly hit the classic self-hosting problem, remote access.

**[01:51](https://youtube.com/watch?v=e4AYC88gi6g&t=111s)** At home if you're on the home wi-fi everything works just fine but the moment you leave your home your home land your home wi-fi you can't reach it or you end up in a world of port forwarding or cloud flare tunnels or firewall rules and it all gets very complicated.

**[02:10](https://youtube.com/watch?v=e4AYC88gi6g&t=130s)** And honestly this is the point where a lot of people just give up, it can be really complicated and it doesn't feel safe.

**[02:17](https://youtube.com/watch?v=e4AYC88gi6g&t=137s)** This is where tail scale comes in, we create something called a tailnet that's our name for a grouping of devices in your personal tail scale network.

**[02:26](https://youtube.com/watch?v=e4AYC88gi6g&t=146s)** Every device you add your phone your laptop your server each gets a secure stable address inside that private tailnet network.

**[02:35](https://youtube.com/watch?v=e4AYC88gi6g&t=155s)** So if image is running at home and connected to your tailnet and your phone is with you perhaps you're on vacation or something and is also connected to your tailnet the connection will just work.

**[02:46](https://youtube.com/watch?v=e4AYC88gi6g&t=166s)** You don't have to configure anything, tail scale will automatically establish a direct connection between those devices using the encryption of wire guard under the hood.

**[02:56](https://youtube.com/watch?v=e4AYC88gi6g&t=176s)** It feels like you're on the same local network as image even if you're on the other side of the world.

**[03:02](https://youtube.com/watch?v=e4AYC88gi6g&t=182s)** Now let's think about family photo sharing for a second.

**[03:05](https://youtube.com/watch?v=e4AYC88gi6g&t=185s)** The first option is to bring everybody into your tailnet so you your partner the kids maybe even grandparents and they all become members of your tailnet once they're in they can reach your image server directly just like you do.

**[03:20](https://youtube.com/watch?v=e4AYC88gi6g&t=200s)** The benefit here is simplicity everything lives inside one private network and access is really straightforward.

**[03:27](https://youtube.com/watch?v=e4AYC88gi6g&t=207s)** This approach is easy and effective but as we'll come on to shortly there are some caveats when it comes to the number of users you can have on tail scales free plan.

**[03:38](https://youtube.com/watch?v=e4AYC88gi6g&t=218s)** The other option we've got is something called no sharing this other option is another way to share image and instead of putting everybody into your tailnet you keep your tailnet just for you your devices your servers that's it.

**[03:51](https://youtube.com/watch?v=e4AYC88gi6g&t=231s)** But you can still give access to your image server or any other tailnet node for that matter without inviting people into your private network.

**[04:00](https://youtube.com/watch?v=e4AYC88gi6g&t=240s)** Tailscale lets you share a single device in this case your image box directly with somebody else from their side it just shows up in their tailscale account and then they connect to it securely.

**[04:11](https://youtube.com/watch?v=e4AYC88gi6g&t=251s)** You can even use our grants and ACL policies to fine tune their access if you need to.

**[04:17](https://youtube.com/watch?v=e4AYC88gi6g&t=257s)** The difference is that they don't become part of your tailnet they only see the one thing that you chose to share with them and that can often be a really nice fit for extended family.

**[04:28](https://youtube.com/watch?v=e4AYC88gi6g&t=268s)** I'm talking grandparents for example who can browse and then even use your image server to back up their photos from their phones automatically but not be a part of your tailnet and not count towards your user allotment that you have on the tailscale free plan.

**[04:43](https://youtube.com/watch?v=e4AYC88gi6g&t=283s)** So let's talk about that plan for just a second because before you pick an approach it's worth knowing how tailscales plans affect this decision.

**[04:51](https://youtube.com/watch?v=e4AYC88gi6g&t=291s)** On the free personal plan you can have up to three users and a hundred devices completely for free across the tailnet.

**[04:58](https://youtube.com/watch?v=e4AYC88gi6g&t=298s)** If you upgrade to the personal plus plan for five dollars a month the user limit increases to six so here's how it might play out for example.

**[05:06](https://youtube.com/watch?v=e4AYC88gi6g&t=306s)** If your family's just you a partner maybe and a kid's just three of you a single tailnet will work great until you think right I want to share a picture with the grandparents and then suddenly you've got a fourth user so you either then need to upgrade to the personal plus plan or start sharing a node out that way and of course you can can blend these two approaches together.

**[05:29](https://youtube.com/watch?v=e4AYC88gi6g&t=329s)** So it's really up to you and I think for most families no sharing ends up being the cleaner approach anyway there are fewer accounts to manage for you as the admin and it's easier for less technical relatives because all they see is just the single image node appear in their account.

**[05:43](https://youtube.com/watch?v=e4AYC88gi6g&t=343s)** They click on the URL in there and they're good to go and that's the choice at the heart of sharing your private image instance via tailscale.

**[05:51](https://youtube.com/watch?v=e4AYC88gi6g&t=351s)** Do you bring everyone into your tailnet or do you keep your tailnet just for you and then share things out the other way to other people either way will work really well and image 2.0 is now finally officially stable and can handle.

**[06:06](https://youtube.com/watch?v=e4AYC88gi6g&t=366s)** I think I've been using it in my personal life now for at least a couple of years so I think it's probably ready that you gave it a try for your family's photo library needs.

**[06:14](https://youtube.com/watch?v=e4AYC88gi6g&t=374s)** Tailscale makes remote access and sharing private services easy and straightforward and for most of you completely for free.

**[06:22](https://youtube.com/watch?v=e4AYC88gi6g&t=382s)** Now if you want to see the full walkthroughs or the GPU acceleration demo I mentioned in the intro links are of course in the description and as always thank you so much for watching and until next time I've been Alex from Tailscale.

---

*Automatically generated transcript. May contain errors.*
