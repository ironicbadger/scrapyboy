---
video_id: "-GqO9o51jcM"
title: "Ask a Tailscale Expert"
description: "Join and have your questions answered by Tailscale expert engineers Alex and Lee, in real time...."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-06-05"
duration_seconds: 3495
youtube_url: "https://www.youtube.com/watch?v=-GqO9o51jcM"
thumbnail_url: "https://i.ytimg.com/vi/-GqO9o51jcM/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:06:28.768400"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 11060
transcription_time_seconds: 120.4
---

# Ask a Tailscale Expert

**[00:00](https://youtube.com/watch?v=-GqO9o51jcM&t=0s)** Live. Webinar is being live streamed. All right. Let's wait and see for YouTube to catch up. I think we're there. I think we're live. Hello, YouTube. Hello, world.

**[00:13](https://youtube.com/watch?v=-GqO9o51jcM&t=13s)** Anybody that's joining us today, thank you very much. You are here for the Tailscale, ask an expert series with myself, Alex.

**[00:22](https://youtube.com/watch?v=-GqO9o51jcM&t=22s)** And me Lee. Lee Briggs is feeling a little under the weather today. So we've got to be very nice to Lee and send him some lemon sip to make him feel better. Yeah, I'm feeling a little bit under the weather today. So my all answers today are with a caveat of it may not be completely acting because my brain is functioning like it would not. But we'll see how it goes.

**[00:45](https://youtube.com/watch?v=-GqO9o51jcM&t=45s)** Because normally, if the two of us, you're like the high energy one.

**[00:49](https://youtube.com/watch?v=-GqO9o51jcM&t=49s)** Yeah, I mean, it's going to be interesting. I this is the only one I haven't looked forward to because I woke up this morning feeling terrible. That's the only reason, but I did not want to leave you in the

**[00:58](https://youtube.com/watch?v=-GqO9o51jcM&t=58s)** Lurge Alex as much as I know that you could do a full hour of answering questions on your own. I did not want to leave you, you know, I don't want to have to break out the tap dancing shoes. Anyway,

**[01:09](https://youtube.com/watch?v=-GqO9o51jcM&t=69s)** just keep the people entertained. So what is this next hour or so that we've got coming up? Well, you can ask questions in the live stream. We're on both YouTube and also on the zoom. It'll probably help if I started the zoom side, wouldn't it? Let's do that.

**[01:24](https://youtube.com/watch?v=-GqO9o51jcM&t=84s)** There we go. No, the zoom side is now live too. So what is this next hour? It's a it's a Q&A format. You can ask Lee and I pretty much any question you would like about Tailscale. We will curate the question. So if we can't get to a question in time, sometimes.

**[01:39](https://youtube.com/watch?v=-GqO9o51jcM&t=99s)** There's just not enough time. We can follow up with you very mad if you would like. And here we can talk about Tailscale. We can talk about networking pretty much anything you can think of in that realm. We'll do our best to talk to you about. So throw some questions in the YouTube live chat. We'd love to see those. If you're on the zoom side, we ask you use the dedicated Q&A section so that we don't miss those questions coming through in the chat. We've got the ever fantastic producer Kate on the back end.

**[02:08](https://youtube.com/watch?v=-GqO9o51jcM&t=128s)** Sort of mastering the questions and kind of keeping the thing flowing along. So I think probably for me, the biggest news out of Tailscale this week is that grants are now GA. Does this mean that ACLs are dead?

**[02:24](https://youtube.com/watch?v=-GqO9o51jcM&t=144s)** We have made the commitment that I think most of the software companies would never dare to make that we are going to continue to support them until the end of time or the heat death of the universe.

**[02:35](https://youtube.com/watch?v=-GqO9o51jcM&t=155s)** Which is one of the things that CEO Avery has kind of stood, you know, made a foundation on is that if we're going to build a platform in which you build a network connectivity, it has to be stable and backwards compatible. So ACLs are going nowhere, they will continue to function and they will continue to work as long as you need them.

**[02:58](https://youtube.com/watch?v=-GqO9o51jcM&t=178s)** There are a lot of benefits to moving to grants though. And one of the things that I would really encourage people to start looking at is, you know, what kind of level of segmentation you need in your network.

**[03:11](https://youtube.com/watch?v=-GqO9o51jcM&t=191s)** Do you want to be able to get application level capabilities in some applications.

**[03:15](https://youtube.com/watch?v=-GqO9o51jcM&t=195s)** We actually have a really interesting graphana proxy that you can find in our open source repo that will actually authenticate you down into graphana based on your talent identity and grants as one of the mechanism that's the underlying use case there.

**[03:29](https://youtube.com/watch?v=-GqO9o51jcM&t=209s)** You've done lots of content Alex on TSI BP which also uses grants as well to kind of determine who you are. So there's a lot of benefits to moving towards grants but ACLs are going nowhere.

**[03:43](https://youtube.com/watch?v=-GqO9o51jcM&t=223s)** I put a link to the grants GA the general available announcement post in the YouTube live chat.

**[03:50](https://youtube.com/watch?v=-GqO9o51jcM&t=230s)** But essentially what you can think of a grant is it's kind of a bit like a firewall rule but for your talent.

**[03:57](https://youtube.com/watch?v=-GqO9o51jcM&t=237s)** It basically permits who can go where who can see what what can access what.

**[04:02](https://youtube.com/watch?v=-GqO9o51jcM&t=242s)** And our old syntax was called access control list ACLs but the new syntax which is going to supersede and become like the standard default moving forward is called grants.

**[04:13](https://youtube.com/watch?v=-GqO9o51jcM&t=253s)** So you can do stuff like say the engineering team is only allowed to access development tagged nodes for example.

**[04:23](https://youtube.com/watch?v=-GqO9o51jcM&t=263s)** And then you can use something like tells us just in time access to come through grants to to say well they can access production for the next 30 minutes or something like that.

**[04:32](https://youtube.com/watch?v=-GqO9o51jcM&t=272s)** Around like a maintenance window or deployment window or something like that and grants is what's powering all of that kind of smarts behind behind the scenes.

**[04:39](https://youtube.com/watch?v=-GqO9o51jcM&t=279s)** One of my favorite things to do with grants though is the new via functionality.

**[04:44](https://youtube.com/watch?v=-GqO9o51jcM&t=284s)** So you can route specific traffic via a specific subnet router.

**[04:49](https://youtube.com/watch?v=-GqO9o51jcM&t=289s)** So for example, I want to route all of my BBC traffic out through a subnet router in England.

**[04:55](https://youtube.com/watch?v=-GqO9o51jcM&t=295s)** That way I don't need to have specific rules or app connectors or exit knows or anything like that.

**[05:01](https://youtube.com/watch?v=-GqO9o51jcM&t=301s)** I can just whitelist certain domains and they all traverse things correctly.

**[05:05](https://youtube.com/watch?v=-GqO9o51jcM&t=305s)** So the via stuff's really powerful and it's it answers a question that we've had for many years of how do we make a subnet router more secure of like I don't want to give everybody on my town access to that entire subnet.

**[05:16](https://youtube.com/watch?v=-GqO9o51jcM&t=316s)** And now you can lock it down using grants.

**[05:19](https://youtube.com/watch?v=-GqO9o51jcM&t=319s)** There's a great questions come in related to this in zoom that I think is a good time to answer it.

**[05:24](https://youtube.com/watch?v=-GqO9o51jcM&t=324s)** The question is a grants implicitly deny all and only granted capabilities are allowed.

**[05:30](https://youtube.com/watch?v=-GqO9o51jcM&t=330s)** So by default, if you have no ACLs all grants in your in your tailnet, you can't do anything.

**[05:40](https://youtube.com/watch?v=-GqO9o51jcM&t=340s)** And so it's denied by default.

**[05:42](https://youtube.com/watch?v=-GqO9o51jcM&t=342s)** And we build a white list of sorry, an analysis of capabilities and permissions on like as you add those one thing that is always what pointing out is when you create a new tailnet, we add a very permissive ACL to every tailnet.

**[05:59](https://youtube.com/watch?v=-GqO9o51jcM&t=359s)** So that you don't end up kind of wondering why tail scale isn't working and you know you created tell net and you can connect to anything that's kind of the reason that that exists.

**[06:08](https://youtube.com/watch?v=-GqO9o51jcM&t=368s)** It would be a pretty poor user experience if you install tail scale onto devices and then you had to go and figure out why you can communicate with them.

**[06:15](https://youtube.com/watch?v=-GqO9o51jcM&t=375s)** So step one is always remove that permissive ACL is like a star star ACL from every tailnet that you create.

**[06:23](https://youtube.com/watch?v=-GqO9o51jcM&t=383s)** And then from there you add permissions on who can kind of communicate with wall.

**[06:28](https://youtube.com/watch?v=-GqO9o51jcM&t=388s)** So hopefully that helps down sort of related Vladimir is coming in and ask the question that's kind of similarly related as well.

**[06:35](https://youtube.com/watch?v=-GqO9o51jcM&t=395s)** The question is, is there a way to prevent certain users from using certain exit nodes?

**[06:39](https://youtube.com/watch?v=-GqO9o51jcM&t=399s)** I want users to have access to my service parts like 80 or 4 for 3, but I want to prevent them from using that computer as an exit node on my tailnet.

**[06:49](https://youtube.com/watch?v=-GqO9o51jcM&t=409s)** Alex, you want to know you have any ideas around this or I can jump in and answer as well.

**[06:55](https://youtube.com/watch?v=-GqO9o51jcM&t=415s)** Yeah, go ahead.

**[06:56](https://youtube.com/watch?v=-GqO9o51jcM&t=416s)** Yeah, so you know, advertising the exit node capability.

**[07:01](https://youtube.com/watch?v=-GqO9o51jcM&t=421s)** It means that you can use that thing as an exit node and you can use it to communicate with other, you know, all the things on the tailnet.

**[07:10](https://youtube.com/watch?v=-GqO9o51jcM&t=430s)** You can use that as a default route for all the other clients on the tailnet.

**[07:14](https://youtube.com/watch?v=-GqO9o51jcM&t=434s)** If you add an ACL that allows you to do like port any up for for 3, it will also allow you to be able to communicate via port 80 and 4 for 3.

**[07:23](https://youtube.com/watch?v=-GqO9o51jcM&t=443s)** Now, the thing that I think you're asking here is like if I've added port 80 and 4 for 3, can they then use that thing as an exit node?

**[07:34](https://youtube.com/watch?v=-GqO9o51jcM&t=454s)** I actually don't know if that's something you can do of the top of your head. I wonder if it's something in the IP.

**[07:42](https://youtube.com/watch?v=-GqO9o51jcM&t=462s)** Like so if you look at a grant, there's an IP field, which will allow you to specify certain protocols, but I think this is actually something I'm going to need to.

**[07:50](https://youtube.com/watch?v=-GqO9o51jcM&t=470s)** Maybe it's just the illness I'm fighting off today, but I can't think of a way to allow communication with another node and then preventing from using as an exit node off the top of my head.

**[08:00](https://youtube.com/watch?v=-GqO9o51jcM&t=480s)** So yeah, I don't have a good answer for that right now, unfortunately.

**[08:05](https://youtube.com/watch?v=-GqO9o51jcM&t=485s)** I think there is a way, is there a group for exit node permission? There's certainly a group for internet permission, like an auto group for internet permission.

**[08:14](https://youtube.com/watch?v=-GqO9o51jcM&t=494s)** So you could do that.

**[08:15](https://youtube.com/watch?v=-GqO9o51jcM&t=495s)** Yeah, and that's auto group internet, right? Yeah, but I think you're actually right. If you have a very restrictive set of ACL, so you remove the default ACL and you don't add auto group internet, you should only be able to communicate with that other node via port 80 and 4 for 3.

**[08:31](https://youtube.com/watch?v=-GqO9o51jcM&t=511s)** So I think that's probably right if you haven't added all a group internet. Yeah, I think you've nailed it, Alex.

**[08:38](https://youtube.com/watch?v=-GqO9o51jcM&t=518s)** Yeah, Vladimir, if that's not covering off your question, please let us know, but we're going to jump into some YouTube questions. Now the first one came in from pre-tore zin.

**[08:51](https://youtube.com/watch?v=-GqO9o51jcM&t=531s)** Who comes up with these usernames? You're just making my life difficult people. Okay, is it possible to access reverse proxy to service?

**[08:59](https://youtube.com/watch?v=-GqO9o51jcM&t=539s)** Is it possible to access reverse proxy to services by local DNS when on a tailnet?

**[09:05](https://youtube.com/watch?v=-GqO9o51jcM&t=545s)** I haven't been able to make this work and I need to I need to avoid updating the public DNS as I'm currently using that for pangolin, which is like a self hosted cloud flare tunnels alternative.

**[09:16](https://youtube.com/watch?v=-GqO9o51jcM&t=556s)** So what do you mean by local DNS? I am assuming you're not meaning the TS dot net entry, the magic DNS entry here. I assume you're meaning that you own your own custom domain name and that you want to use that on your land.

**[09:30](https://youtube.com/watch?v=-GqO9o51jcM&t=570s)** And then also have that be rootable from some kind of external place. Would you agree with that?

**[09:36](https://youtube.com/watch?v=-GqO9o51jcM&t=576s)** I think that's a, I think this is a split DNS question, right? So you have a public facing, you have a public facing domain, which is likely going to be pangolin.microdomain.com and that's going to point to the, you know, the public IP address of your router, for example, is my guess here.

**[09:55](https://youtube.com/watch?v=-GqO9o51jcM&t=595s)** And then internally, you want to be able to resolve that over the tail scale IP address when you connected to tail scale.

**[10:03](https://youtube.com/watch?v=-GqO9o51jcM&t=603s)** So this is a split DNS situation, a very common thing in most corporate enterprises, and usually at home, the step one is run a DNS server, right?

**[10:12](https://youtube.com/watch?v=-GqO9o51jcM&t=612s)** Like an internal DNS server in your, in your environment, DNS mask is pretty easy to go get a ball running call DNS is pretty easy to get a ball running.

**[10:22](https://youtube.com/watch?v=-GqO9o51jcM&t=622s)** And then set that resolver to be one of the DNS resolvers in your tail scale settings. If you're going to the admin console and going to DNS, you can specify a DNS server which you've set up.

**[10:35](https://youtube.com/watch?v=-GqO9o51jcM&t=635s)** I recognize that's probably not like the easy mode that you want to be able to do, but that's the only real way of being able to do it because what you want to do is at the split horizon situation, where if you're on one network, it resolves a certain thing, and when you're on another network, it resolves another thing.

**[10:50](https://youtube.com/watch?v=-GqO9o51jcM&t=650s)** I generally have kind of moved away from split DNS because it's super confusing and it can be really like tricky to configure correctly.

**[10:57](https://youtube.com/watch?v=-GqO9o51jcM&t=657s)** So what I do is I just add on my tail scale IP to my public DNS now and just use tail scale to connect to them. That's the easy mode way of doing that.

**[11:05](https://youtube.com/watch?v=-GqO9o51jcM&t=665s)** Yeah, so you can get as fancy as you like with split DNS and I've put a link to a very old video of mine.

**[11:16](https://youtube.com/watch?v=-GqO9o51jcM&t=676s)** She's probably a couple of years old now talking about magic DNS and how you can split DNS between different sites and what have you.

**[11:22](https://youtube.com/watch?v=-GqO9o51jcM&t=682s)** Where it does become useful is if you have a bunch of local entries across a bunch of different sites and you want each of those sites to maintain functionality, even if tail scales not involved.

**[11:33](https://youtube.com/watch?v=-GqO9o51jcM&t=693s)** You run a local DNS server in each network so it could be a pie hole.

**[11:37](https://youtube.com/watch?v=-GqO9o51jcM&t=697s)** Lee mentioned a couple others called DNS. There's a bunch at guard home is another one that blocks ads for you as well.

**[11:43](https://youtube.com/watch?v=-GqO9o51jcM&t=703s)** And you can set that in your tail scale DNS settings to run as your upstream DNS server for the entire tail net.

**[11:51](https://youtube.com/watch?v=-GqO9o51jcM&t=711s)** And because it's tail scale everything's a flat network, it doesn't matter where the devices are, they can all route their DNS queries through that kind of central DNS server.

**[12:00](https://youtube.com/watch?v=-GqO9o51jcM&t=720s)** So that's another option as well, but really there's no one right way to skin this particular cat.

**[12:06](https://youtube.com/watch?v=-GqO9o51jcM&t=726s)** It's that genuinely that DNS is one of those things that it's complicated and when it goes wrong, we all love to have, you know, we will love Jeff Gehlings T shirt.

**[12:16](https://youtube.com/watch?v=-GqO9o51jcM&t=736s)** It's it's always DNS, right? But it's true because it's at the core of everything we do. So the easiest, the easiest thing to do is add a host file entry.

**[12:26](https://youtube.com/watch?v=-GqO9o51jcM&t=746s)** That would be the easiest thing to do. Like if you really want to do easy mode here is out of host file entry and don't have to deal with DNS at all.

**[12:34](https://youtube.com/watch?v=-GqO9o51jcM&t=754s)** But that's the very, I've been around long enough to remember when we used to send host file entries to each other back in the 90s.

**[12:41](https://youtube.com/watch?v=-GqO9o51jcM&t=761s)** So yeah, let's not go back to those days.

**[12:45](https://youtube.com/watch?v=-GqO9o51jcM&t=765s)** Speaking to the guy that when he did his computer science masters sent source code around all Facebook messenger and a zip file to his team.

**[12:54](https://youtube.com/watch?v=-GqO9o51jcM&t=774s)** Because Git was too complicated, you know, yeah, I mean, I remember the pre Git days very vaguely.

**[13:00](https://youtube.com/watch?v=-GqO9o51jcM&t=780s)** So we've all committed crimes against humanity in the name of tech.

**[13:05](https://youtube.com/watch?v=-GqO9o51jcM&t=785s)** Yeah, man, I do not miss SBN at all.

**[13:08](https://youtube.com/watch?v=-GqO9o51jcM&t=788s)** Curial is another one.

**[13:09](https://youtube.com/watch?v=-GqO9o51jcM&t=789s)** And my previous company was a big user of Mercurial for the cell reason, like, well, Facebook uses it.

**[13:15](https://youtube.com/watch?v=-GqO9o51jcM&t=795s)** And I'm like, okay, but that'd be only once.

**[13:17](https://youtube.com/watch?v=-GqO9o51jcM&t=797s)** Yeah, so what else to use butter FS, which has got a massive right hole anyway.

**[13:22](https://youtube.com/watch?v=-GqO9o51jcM&t=802s)** And then there's almost the the per false club with all the gaming companies using per false.

**[13:27](https://youtube.com/watch?v=-GqO9o51jcM&t=807s)** A good question again, while we're on still kind of a sociable grants, do grants include a time window for exploration or an ability to specify on off times, not by default, but there is a posture mechanism with just in time posture that can do this.

**[13:41](https://youtube.com/watch?v=-GqO9o51jcM&t=821s)** And so that will allow you to add a new field to a grant that is source posture and the source posture is a metadata attribute on the client and once you add it, you can have something like remove that over a certain amount of time.

**[13:55](https://youtube.com/watch?v=-GqO9o51jcM&t=835s)** Which is really, really useful and it's good for things like temporary access to production or temporary access to the Kubernetes operator and stuff like that.

**[14:04](https://youtube.com/watch?v=-GqO9o51jcM&t=844s)** It's really useful. So I would recommend looking into that.

**[14:08](https://youtube.com/watch?v=-GqO9o51jcM&t=848s)** Now I just put a link in the chat to our just in time access video that came out three weeks ago now, kind of giving some more details on that particular topic.

**[14:19](https://youtube.com/watch?v=-GqO9o51jcM&t=859s)** So it's so serendipitous. You do a video and then there's a question about it two weeks later. It's great.

**[14:23](https://youtube.com/watch?v=-GqO9o51jcM&t=863s)** Yeah. Well, I haven't done one on grants yet, but that is coming. And these questions, by the way, informed content that I make. So thank you for asking the questions. I didn't know needed answering before and even thought of them.

**[14:36](https://youtube.com/watch?v=-GqO9o51jcM&t=876s)** I love you guys. So another question on grants. Where are they enforced is the question.

**[14:43](https://youtube.com/watch?v=-GqO9o51jcM&t=883s)** I'm going to try and where grants enforced. They're enforced on the actual one. So basically, when you every tail scale client gets a net map, right. And it's like a big map of what's actually happening on the network.

**[14:58](https://youtube.com/watch?v=-GqO9o51jcM&t=898s)** And it's enforced on the local client when that net map is kind of propagated out to all the nodes in the in the tail scale network.

**[15:05](https://youtube.com/watch?v=-GqO9o51jcM&t=905s)** So one thing that we always say is if like in the very unlikely events that we have a control plan outage or there's like a problem with the tail scale control plane, everything will continue to work, but you can't make modifications to things like ACLs because you can't propagate those things out to the client.

**[15:21](https://youtube.com/watch?v=-GqO9o51jcM&t=921s)** So essentially, when you set a grant or when you set an ACL in the editor, what happens is that gets propagated out to all of the different clients. When we do demos for customers on the solutions engineering team.

**[15:34](https://youtube.com/watch?v=-GqO9o51jcM&t=934s)** One of my favorite things to do is like modify their grant and then show how quickly that applies. It's usually less than the amount of time it takes me to change my window.

**[15:44](https://youtube.com/watch?v=-GqO9o51jcM&t=944s)** So usually so millisecond that happens, which is, you know, a very, very impressive feat of engineering, when you, especially when you're in some of the large networks.

**[15:51](https://youtube.com/watch?v=-GqO9o51jcM&t=951s)** But the client of the local itself basically says, ah, you are trying to connect to this thing that I know about, but over a part that I won't let you. So I'm not going to let you do that.

**[15:59](https://youtube.com/watch?v=-GqO9o51jcM&t=959s)** And so that's kind of how they're enforced.

**[16:04](https://youtube.com/watch?v=-GqO9o51jcM&t=964s)** Yeah, all client side. So every single rule set that gets created in tail scale, yes, it's coordinated by the central server, but all of the processing happens client side.

**[16:17](https://youtube.com/watch?v=-GqO9o51jcM&t=977s)** So for example, with DNS, your phone is running a local DNS server as part of the tail scale package on the phone itself.

**[16:26](https://youtube.com/watch?v=-GqO9o51jcM&t=986s)** And the rule set gets pushed down from the central server every time there's a change in the same as true of grants of everything else.

**[16:32](https://youtube.com/watch?v=-GqO9o51jcM&t=992s)** So yeah, it's pretty, it's pretty performant way to do it. And the nice, the nice upshot of that is if tail scale goes down for any reason that central server is not reachable by the particular client, you know, the rest of the internet is for whatever reason, like maybe you just can't reach tail scale.com for that few seconds.

**[16:48](https://youtube.com/watch?v=-GqO9o51jcM&t=1008s)** It doesn't matter because everything happens locally. So that means performance is a lot better. The resolution is better or that kind of stuff too.

**[16:57](https://youtube.com/watch?v=-GqO9o51jcM&t=1017s)** All right, so a couple of questions regarding connections and trust and unsolicited unsolicited stuff. So there's what about funnel here, first of all, are there any ways to secure the funnel connections and reduce scanning, or do you recommend any compatible systems instead.

**[17:13](https://youtube.com/watch?v=-GqO9o51jcM&t=1033s)** I mean, I think the short answer is no, as soon as you funnel something you're putting it out on the public internet and putting it at the best of all of the scary things in the public internet, the the glib answer is yes, don't use funnel and just use tail scale to do the communication. But if you want to expose something over the public internet, funnel is basically giving you, you know, exposing those things to all the big scary internet things.

**[17:38](https://youtube.com/watch?v=-GqO9o51jcM&t=1058s)** And so you are going to be part scan and you are going to have around and people trying to connect to you. That just is kind of the contract that we have of the internet as a large right now.

**[17:48](https://youtube.com/watch?v=-GqO9o51jcM&t=1068s)** If you don't want it public, don't make it public, right. Yeah, I think if you really wanted to, you know, you could look at different ways of exposing to the public internet and do it that way. And then add a firewall in front of it. But like, that's really side outside of the like a web application.

**[18:07](https://youtube.com/watch?v=-GqO9o51jcM&t=1087s)** Firewall, sorry, like that's really outside the scope of funnel, right. For those funnel is just your ability to, you know, provide access inside your tail net through our infrastructure, basically. So I think the short answer there is, you know, unfortunately, all the ways of doing this, yeah, like, you know, attach a public IP to it and put a web application firewall and from it, whether that's with your cloud provider or at home or anything along those lines.

**[18:35](https://youtube.com/watch?v=-GqO9o51jcM&t=1115s)** I put a link to a project called CrowdSec in the YouTube chat right now, which I've seen a lot of chatter about in the self hosted community for people putting on in front of public URLs to do things like blocking specific geo regions and stuff like that.

**[18:53](https://youtube.com/watch?v=-GqO9o51jcM&t=1133s)** Essentially, it's a crowdsourced server detection and protection against malicious IP engine, whatever that means in plain English.

**[19:01](https://youtube.com/watch?v=-GqO9o51jcM&t=1141s)** So I would have a look at that because I think it's it's kind of doing what you want. There's no affiliation with tail scale. Like I've never even used the software, but I've read about it many times. And I believe it will do some of what you're asking.

**[19:14](https://youtube.com/watch?v=-GqO9o51jcM&t=1154s)** But the reality is, if you don't want it on the public internet, don't put it on the public internet because, you know, vulnerabilities are a thing. And even if you have a login page, like somebody somewhere has got an exploit for it. I can almost guarantee that. So

**[19:27](https://youtube.com/watch?v=-GqO9o51jcM&t=1167s)** Indeed.

**[19:28](https://youtube.com/watch?v=-GqO9o51jcM&t=1168s)** Next question. In fact, there's two kind of very similar ones here is how can I block unsolicited outbound connections from hosts. I don't trust.

**[19:37](https://youtube.com/watch?v=-GqO9o51jcM&t=1177s)** And how can I block certain tail scale IPs from making unsolicited calls to my other tail scale hosts, but still allow me to connect to them.

**[19:46](https://youtube.com/watch?v=-GqO9o51jcM&t=1186s)** Again, I think this comes back to what we talked about earlier. It's it's around like building your ACL like every single question that is related to this. I will almost guarantee you probably got the default ACL configured in

**[19:57](https://youtube.com/watch?v=-GqO9o51jcM&t=1197s)** Oh, you've got that default permissive ACL in there. So step one is, let's remove that line. Right. Like let's get rid of the, you know, the star star allow anything line.

**[20:08](https://youtube.com/watch?v=-GqO9o51jcM&t=1208s)** And then nobody won't be able to communicate with anyone in detail. And then you're supposed to build your connectivity on top of that. Right. And so if you don't want people to be able to be like make unsolicited outbound connections, you don't give them all to go into net. And if you don't want

**[20:22](https://youtube.com/watch?v=-GqO9o51jcM&t=1222s)** People to be able to communicate with your application on par for for three or HTTPS. You don't allow that route.

**[20:29](https://youtube.com/watch?v=-GqO9o51jcM&t=1229s)** I think, you know, what there's been a lot of questions around grants and ACLs here. And I'm like almost thinking to ourselves. We might be to

**[20:37](https://youtube.com/watch?v=-GqO9o51jcM&t=1237s)** Write a blog post or a piece of content, which is like it's day one and you've got tail scale. What should you do? Right. Like

**[20:45](https://youtube.com/watch?v=-GqO9o51jcM&t=1245s)** Because one of the things that's really great about tail scale is it just works. But then when you want to do these more advanced things, because it's just worked, you haven't really understood the underlying way of all connects together.

**[20:56](https://youtube.com/watch?v=-GqO9o51jcM&t=1256s)** So I do think that would be really useful. Like, you know, the first 24 hours with tail scale, remove the default ACL, start building on the traffic and going from there.

**[21:05](https://youtube.com/watch?v=-GqO9o51jcM&t=1265s)** I wonder, could we approach Mr. Beast to do some does let's not go down that route.

**[21:11](https://youtube.com/watch?v=-GqO9o51jcM&t=1271s)** That's 24 hours with tail scale.

**[21:13](https://youtube.com/watch?v=-GqO9o51jcM&t=1273s)** I just the eyes on those videos just freaked me out. You know, Mr. Beast eyes, you know, anyway, personal opinions aside.

**[21:22](https://youtube.com/watch?v=-GqO9o51jcM&t=1282s)** There's a really interesting question that I've seen in our little list that I think is I'll be clear. We don't have a straight answer to this, but it's an interesting question.

**[21:32](https://youtube.com/watch?v=-GqO9o51jcM&t=1292s)** Do paid customers, I personal plus start a premium, et cetera, get any kind of priority on dirt servers. If not, are there any plans to introduce this?

**[21:40](https://youtube.com/watch?v=-GqO9o51jcM&t=1300s)** The short answer for that right now is no, we have a specific queuing mechanism, which we apply to all dirt servers, which basically gives a fair usage across all clients.

**[21:52](https://youtube.com/watch?v=-GqO9o51jcM&t=1312s)** Assuming you are not being, you know, you're not a bit torrenting over it or sending, you know, large amounts of traffic.

**[22:00](https://youtube.com/watch?v=-GqO9o51jcM&t=1320s)** I think there is certainly internal interest around this, right? Like, and we've got to be very clear.

**[22:07](https://youtube.com/watch?v=-GqO9o51jcM&t=1327s)** Our product roadmap and demand are very, very intrinsically linked. So if you are interested in paying for dirt servers that are for your tailnet that are kind of like outside of the community, dirt servers, we would like to hear about it.

**[22:23](https://youtube.com/watch?v=-GqO9o51jcM&t=1343s)** We want to hear about these things, whether it's in GitHub issues, whether it's sales contacts, support tickets, like all the ways that you can communicate with us.

**[22:31](https://youtube.com/watch?v=-GqO9o51jcM&t=1351s)** It's something that we have generally stayed away from for the simple reason that we, you know, I personally have a belief that there should be no internet fastening and it should be relatively fair.

**[22:41](https://youtube.com/watch?v=-GqO9o51jcM&t=1361s)** But at the same time, you know, if you're paying those tell scale, you know, $100,000 a year, you probably want your traffic prioritized over

**[22:52](https://youtube.com/watch?v=-GqO9o51jcM&t=1372s)** Lee's bit ton of traffic, right? So I think this is something that we want to hear more about from you folks. If you are interested in, you know, you know, exploring this.

**[23:04](https://youtube.com/watch?v=-GqO9o51jcM&t=1384s)** You can always run your own dirt servers. It's not a straightforward thing to do. We generally don't recommend it. But if you want dedicated traffic running your own dirt servers is an answer to that as well.

**[23:13](https://youtube.com/watch?v=-GqO9o51jcM&t=1393s)** And there are lots of community things that I maintain a community dirt server package that you can run.

**[23:18](https://youtube.com/watch?v=-GqO9o51jcM&t=1398s)** But generally, the answer is no. And so, you know, more feedback in the comments will be super useful.

**[23:26](https://youtube.com/watch?v=-GqO9o51jcM&t=1406s)** Always always useful. Speaking of comments and feedback in the last couple of weeks, we had a security built in published around a shared domains issue.

**[23:36](https://youtube.com/watch?v=-GqO9o51jcM&t=1416s)** And I want to address that very quickly in the live stream today. There was a question here saying one of my co workers was able to see somebody else's.

**[23:43](https://youtube.com/watch?v=-GqO9o51jcM&t=1423s)** Nodes in tail scale, I put a link to the security bulletin in the live chat on YouTube. But the short answer is if you're affected by this in any way, please reach out to our support teams immediately.

**[23:55](https://youtube.com/watch?v=-GqO9o51jcM&t=1435s)** And they will do everything they can to prioritize a ticket and get you taken care of and make sure that the shared domain issues taken taken care of is something that our engineering teams are taking incredibly serious.

**[24:06](https://youtube.com/watch?v=-GqO9o51jcM&t=1446s)** Let me tell you internally, there's been some huge discussions senior leadership all the way up to Avery involved in this one. So take a take a read of the security built in to find out more.

**[24:18](https://youtube.com/watch?v=-GqO9o51jcM&t=1458s)** Yeah. And I think one of the things that I wish one idea is, you know, we all obviously read the comments for better old worse, you know, never read the comments, but we'll read the comments for better or worse.

**[24:27](https://youtube.com/watch?v=-GqO9o51jcM&t=1467s)** And I think one of the things that was very kind of clear is like, how did you let this happen for so long? Right.

**[24:33](https://youtube.com/watch?v=-GqO9o51jcM&t=1473s)** And I think the answer that I would have to that is everybody has worked under a prioritization system at work. And I can, I can bet you imagine, you know, there are things that you have identified in your day to day role or your software engineering job or your, you know, your environment that you're like, man, we shouldn't really take care of that.

**[24:50](https://youtube.com/watch?v=-GqO9o51jcM&t=1490s)** And I think this is one of those things that was a wake up call for us.

**[24:54](https://youtube.com/watch?v=-GqO9o51jcM&t=1494s)** And, you know, there's no kind of excuses really. I don't think I was trying to make excuses. We always were going to reprioritize this and we always were going to make sure that we got this fix. But, you know, priorities change and priorities shift.

**[25:09](https://youtube.com/watch?v=-GqO9o51jcM&t=1509s)** And I think there's a certainly a deep level of like humility around this internally for us at the moment. So, you know, we hear you loud and clear.

**[25:18](https://youtube.com/watch?v=-GqO9o51jcM&t=1518s)** You know, we're not a perfect organization. This was a mistake and we will rectify it and fix it. And we have some really exciting changes around our identity model coming.

**[25:28](https://youtube.com/watch?v=-GqO9o51jcM&t=1528s)** I think in our last asking expert when I did a bunch of demos, everybody saw a little sneak peek about some of the things that are coming around the ability to switch tail nets and all that kind of stuff and have tail nets, you know, embedded in tail nets, which is going to be exciting.

**[25:41](https://youtube.com/watch?v=-GqO9o51jcM&t=1541s)** But all of that is is underwork underway and we are going to address it in that scope of work, basically.

**[25:48](https://youtube.com/watch?v=-GqO9o51jcM&t=1548s)** Yeah, so again, reach out to our support teams. If you're affected anyway by this one. And yeah, we're sorry about that. Okay, question for you, Lee. Can I self host the Derp server?

**[26:01](https://youtube.com/watch?v=-GqO9o51jcM&t=1561s)** Yes. So the code for a Derp server is just in our results. We don't repo us in the tail scale repo under command on a Derp. It's a gold binary. We don't publish packages for it. So you need to build it.

**[26:13](https://youtube.com/watch?v=-GqO9o51jcM&t=1573s)** And then you need to run it on a on a node that has both IPv4 and IPv6 addresses attached directly to it.

**[26:22](https://youtube.com/watch?v=-GqO9o51jcM&t=1582s)** I run a Derp server. I run a couple of Derp servers in linode one in London and one in Seattle because they are in a geographically opposed to the places that I want to connect you.

**[26:32](https://youtube.com/watch?v=-GqO9o51jcM&t=1592s)** And, you know, if you want to run production level Derp servers, you have to connect them together and create a mesh key and do a whole bunch of other stuff. But for a single small organization, a Derp server can be run pretty easily.

**[26:43](https://youtube.com/watch?v=-GqO9o51jcM&t=1603s)** The reason we don't generally publish any documentation on how to do this is because it's a much more complicated task than like installing a setting up tail scale and we require.

**[26:53](https://youtube.com/watch?v=-GqO9o51jcM&t=1613s)** Because, you know, if you run into problems, we just don't have the capacity to be able to help you. So, you know, you can do go install for the Derp server. I maintain an RPM package that I periodically publish.

**[27:06](https://youtube.com/watch?v=-GqO9o51jcM&t=1626s)** I know there's plenty of people out there that package up into a Docker container, which you have to run with host network. But yeah, you can tell the run your own Derp server. You just need to make sure it has IPv4 and IPv6 connectivity.

**[27:17](https://youtube.com/watch?v=-GqO9o51jcM&t=1637s)** And so it has to have a public IP. It can't be behind in that. It can't be a firewall. It must be publicly available.

**[27:23](https://youtube.com/watch?v=-GqO9o51jcM&t=1643s)** And the other thing that you can do finally on this is if you run tail scale alongside your Derp server, you can set a flag on the run of the Derp server that will only allow your tail net to connect to it.

**[27:37](https://youtube.com/watch?v=-GqO9o51jcM&t=1657s)** And so people can randomly add your Derp server to their netmap or to their ACL, which is something that I do as well.

**[27:44](https://youtube.com/watch?v=-GqO9o51jcM&t=1664s)** So, yes, you can tell me when you're on a Derp server. I have, you know, I have offered to help people do this on a kind of production, you know, you know, on a production level.

**[27:55](https://youtube.com/watch?v=-GqO9o51jcM&t=1675s)** But we generally don't recommend it, basically.

**[27:59](https://youtube.com/watch?v=-GqO9o51jcM&t=1679s)** Jeff Goldblum time.

**[28:01](https://youtube.com/watch?v=-GqO9o51jcM&t=1681s)** The scientists were too preoccupied with whether they could. They didn't stop to ask themselves whether they should is running a debt server as a regular user, a good idea.

**[28:11](https://youtube.com/watch?v=-GqO9o51jcM&t=1691s)** I don't think so. I think most of the problems that you run into that you need a Derp server for can be solved by architecting things so you get direct connections, right? Like, so, you know, making sure that you are using easy now on both sides of the equation or making sure that you are putting one side as a no net is usually, you know, pretty straightforward.

**[28:32](https://youtube.com/watch?v=-GqO9o51jcM&t=1712s)** You know, I would generally steer away from it and in most circumstances.

**[28:37](https://youtube.com/watch?v=-GqO9o51jcM&t=1717s)** It's just one more thing to break, right?

**[28:39](https://youtube.com/watch?v=-GqO9o51jcM&t=1719s)** It's just another thing that can go wrong. Yeah, absolutely.

**[28:42](https://youtube.com/watch?v=-GqO9o51jcM&t=1722s)** Okay, so on the client side, the question came in around Docker. Is it better to use the official Docker container beside an app?

**[28:52](https://youtube.com/watch?v=-GqO9o51jcM&t=1732s)** Assuming that means in like Docker compose when you're running applications together or would you prefer or would you embed tail scale into a container with mods, for example, I assume that means like running your application and tail scale inside the same container.

**[29:05](https://youtube.com/watch?v=-GqO9o51jcM&t=1745s)** I know you've done a lot on this like so I would love you to answer it.

**[29:08](https://youtube.com/watch?v=-GqO9o51jcM&t=1748s)** Yeah, so this actually speaks to back in the dark ages of my Docker history, I was one of the founding members of Linux server.

**[29:18](https://youtube.com/watch?v=-GqO9o51jcM&t=1758s)** And we came up with this concept of a Docker mod, which was this idea of been able to install plugins effectively or customize the init sequence of a container to do custom stuff.

**[29:33](https://youtube.com/watch?v=-GqO9o51jcM&t=1773s)** I didn't write that bit, but it was some very clever people that wrote that bit, not me, but essentially you're limited as far as I'm aware, Linux server.io containers are the only ones that support Docker mods as they are called.

**[29:47](https://youtube.com/watch?v=-GqO9o51jcM&t=1787s)** They do work really well. You can install, if you have a Linux server container, anyone who install a Docker mod in there of tail scale, it works. In fact, some of my production infrastructure that I do here at tail scale for some of the developer relations, you know, event demos and stuff like that.

**[30:03](https://youtube.com/watch?v=-GqO9o51jcM&t=1803s)** I utilize that stuff. I just use the Linux server engine X image throw tail scale in the Docker mod section of that image and it just works.

**[30:12](https://youtube.com/watch?v=-GqO9o51jcM&t=1812s)** But for everything else, which is like 99% of the rest of the internet that doesn't have mod support sidecar container is the way to go.

**[30:23](https://youtube.com/watch?v=-GqO9o51jcM&t=1823s)** And it's certainly the officially supported and sanctioned way to go even for Linux server images to.

**[30:29](https://youtube.com/watch?v=-GqO9o51jcM&t=1829s)** So a sidecar docker image only uses about 20, maybe 25 megabytes of memory to run alongside your existing application.

**[30:37](https://youtube.com/watch?v=-GqO9o51jcM&t=1837s)** And literally all it's doing is proxying traffic to and from your talent using some clever Linux kernel namespace merging going on behind the scenes.

**[30:47](https://youtube.com/watch?v=-GqO9o51jcM&t=1847s)** But so far as your concern as a user, your application, whatever it is, it is now on tail scale just through the virtue of having one little sidecar container.

**[30:59](https://youtube.com/watch?v=-GqO9o51jcM&t=1859s)** Very thorough, wonderful answer, Alex, thank you.

**[31:03](https://youtube.com/watch?v=-GqO9o51jcM&t=1863s)** You want to throw a question at me next? Like you got a couple that have highlighted.

**[31:09](https://youtube.com/watch?v=-GqO9o51jcM&t=1869s)** Sure, yeah, I'll ask you any road map for using custom SSO provider is also known as custom skim.

**[31:17](https://youtube.com/watch?v=-GqO9o51jcM&t=1877s)** So I want to make sure to differentiate between these two things, right?

**[31:20](https://youtube.com/watch?v=-GqO9o51jcM&t=1880s)** SSO, we use the OIDC protocol for logging into tail scale.

**[31:25](https://youtube.com/watch?v=-GqO9o51jcM&t=1885s)** It is we consistently get questions in our support queue for like why kind of logging with email and password.

**[31:32](https://youtube.com/watch?v=-GqO9o51jcM&t=1892s)** So, you know, to address that while we're at it.

**[31:36](https://youtube.com/watch?v=-GqO9o51jcM&t=1896s)** We don't want to store your password locally because we want the identity providers to store it because they're way better at it than we could have hoped to be.

**[31:43](https://youtube.com/watch?v=-GqO9o51jcM&t=1903s)** So we every tail scale network must have an OIDC backend.

**[31:48](https://youtube.com/watch?v=-GqO9o51jcM&t=1908s)** However, you can bring your own custom or IDC backend.

**[31:52](https://youtube.com/watch?v=-GqO9o51jcM&t=1912s)** I think you've mentioned a couple of times, Alex, things like key cloak, which are kind of supported and you have to host your own OIDC provider.

**[31:59](https://youtube.com/watch?v=-GqO9o51jcM&t=1919s)** Yeah, pocket ID.

**[32:00](https://youtube.com/watch?v=-GqO9o51jcM&t=1920s)** I believe the question here recently.

**[32:02](https://youtube.com/watch?v=-GqO9o51jcM&t=1922s)** Is it going to be possible to support skim with those custom OIDC providers?

**[32:09](https://youtube.com/watch?v=-GqO9o51jcM&t=1929s)** The answer to that right now is it's not on the roadmap for two reasons, one, while skim is a allegedly well defined protocol.

**[32:20](https://youtube.com/watch?v=-GqO9o51jcM&t=1940s)** Every single provider skim implementation has its own nuances and differences.

**[32:25](https://youtube.com/watch?v=-GqO9o51jcM&t=1945s)** And we found that as we tried to make this generic.

**[32:28](https://youtube.com/watch?v=-GqO9o51jcM&t=1948s)** And so what we end up doing is playing whack a mole with everybody skim implementation.

**[32:33](https://youtube.com/watch?v=-GqO9o51jcM&t=1953s)** So, you know, we implemented skim support for Microsoft entry ID and we were under the belief that that would work out of the box with octa and we found that didn't work.

**[32:42](https://youtube.com/watch?v=-GqO9o51jcM&t=1962s)** So right now there is no potential like roadmap item for this, but again, we're driven by customer demand.

**[32:48](https://youtube.com/watch?v=-GqO9o51jcM&t=1968s)** So if you are wanting to use tail scale and you want to kind of, you know, this is a blocker for you.

**[32:56](https://youtube.com/watch?v=-GqO9o51jcM&t=1976s)** And you feel that it's like significant enough in terms of our revenue dollars that we can, you know, manipulate our roadmap or manipulates in the wrong way, but influence our roadmap.

**[33:05](https://youtube.com/watch?v=-GqO9o51jcM&t=1985s)** We want to hear from you, right?

**[33:06](https://youtube.com/watch?v=-GqO9o51jcM&t=1986s)** And we recognize that, you know, we'd love to be able to support this if there was a, if there was a protocol that was ubiquitous and worked across all identity providers.

**[33:16](https://youtube.com/watch?v=-GqO9o51jcM&t=1996s)** And didn't require us to do custom code for every single thing.

**[33:19](https://youtube.com/watch?v=-GqO9o51jcM&t=1999s)** We would almost certainly do this, right?

**[33:21](https://youtube.com/watch?v=-GqO9o51jcM&t=2001s)** But as it stands, that has not been our experience with the skin protocol.

**[33:26](https://youtube.com/watch?v=-GqO9o51jcM&t=2006s)** Now another question came in asking about our user community that was recently formed.

**[33:33](https://youtube.com/watch?v=-GqO9o51jcM&t=2013s)** We may recently hired a new community manager, her name's Natasha. She's fantastic.

**[33:37](https://youtube.com/watch?v=-GqO9o51jcM&t=2017s)** She sits alongside me on the dev rail team.

**[33:40](https://youtube.com/watch?v=-GqO9o51jcM&t=2020s)** And put a link in the chat here to our new insiders program.

**[33:43](https://youtube.com/watch?v=-GqO9o51jcM&t=2023s)** So if you are a tail scale super fan and you'd like to get more involved with the tail scale community, we have a program just for you.

**[33:50](https://youtube.com/watch?v=-GqO9o51jcM&t=2030s)** Please fill in the form, apply and Natasha will get back to you at some point talking about this program.

**[33:57](https://youtube.com/watch?v=-GqO9o51jcM&t=2037s)** Yes. And Natasha is also from the British, British expert club that is following the tail scale.

**[34:02](https://youtube.com/watch?v=-GqO9o51jcM&t=2042s)** I think we have one of the largest British expert communities in any software engineering organization.

**[34:08](https://youtube.com/watch?v=-GqO9o51jcM&t=2048s)** I love it.

**[34:09](https://youtube.com/watch?v=-GqO9o51jcM&t=2049s)** Why, why is that?

**[34:10](https://youtube.com/watch?v=-GqO9o51jcM&t=2050s)** I don't know. I don't know.

**[34:12](https://youtube.com/watch?v=-GqO9o51jcM&t=2052s)** I think part of it is because we hire in Canada.

**[34:14](https://youtube.com/watch?v=-GqO9o51jcM&t=2054s)** And there's a big migratory population from the UK to Canada.

**[34:19](https://youtube.com/watch?v=-GqO9o51jcM&t=2059s)** But you, me, and there's at least three over British, British people living in the USA tail scale as well, which is.

**[34:27](https://youtube.com/watch?v=-GqO9o51jcM&t=2067s)** I wonder.

**[34:28](https://youtube.com/watch?v=-GqO9o51jcM&t=2068s)** My theory is, is that we all miss eye players so much that we are VPN adjacent.

**[34:34](https://youtube.com/watch?v=-GqO9o51jcM&t=2074s)** Yes.

**[34:36](https://youtube.com/watch?v=-GqO9o51jcM&t=2076s)** Maybe. Yeah.

**[34:37](https://youtube.com/watch?v=-GqO9o51jcM&t=2077s)** I just want to have a community of people who I can tell people jokes to and have them understand it.

**[34:42](https://youtube.com/watch?v=-GqO9o51jcM&t=2082s)** That's really what I'm looking for.

**[34:44](https://youtube.com/watch?v=-GqO9o51jcM&t=2084s)** I will say just on the community side, we are Natasha and I met last week about kind of building a community gathering space outside and read it.

**[34:52](https://youtube.com/watch?v=-GqO9o51jcM&t=2092s)** So watch the space.

**[34:53](https://youtube.com/watch?v=-GqO9o51jcM&t=2093s)** I'm really excited about that.

**[34:54](https://youtube.com/watch?v=-GqO9o51jcM&t=2094s)** One of my favorite things to do is kind of go back through the YouTube comments here and see how like engaged everybody is.

**[35:01](https://youtube.com/watch?v=-GqO9o51jcM&t=2101s)** We've recognized that having a gathering place for people would be extremely useful.

**[35:05](https://youtube.com/watch?v=-GqO9o51jcM&t=2105s)** It would also take a lot of work off me and Alex because we wouldn't have to constantly answer questions and stuff.

**[35:10](https://youtube.com/watch?v=-GqO9o51jcM&t=2110s)** Because I think there's so many knowledgeable people in our community who can help and answer questions.

**[35:16](https://youtube.com/watch?v=-GqO9o51jcM&t=2116s)** So we're hard to work at that and watch the space.

**[35:19](https://youtube.com/watch?v=-GqO9o51jcM&t=2119s)** It's it's in in process.

**[35:21](https://youtube.com/watch?v=-GqO9o51jcM&t=2121s)** Yeah.

**[35:24](https://youtube.com/watch?v=-GqO9o51jcM&t=2124s)** Oh, here's a really interesting question that came through about Derp servers in particular.

**[35:28](https://youtube.com/watch?v=-GqO9o51jcM&t=2128s)** Does Taylor scale have any rough stats on how much traffic runs through a Derp on a daily basis?

**[35:34](https://youtube.com/watch?v=-GqO9o51jcM&t=2134s)** I don't I have actually previously asked if we can publish this and we have made an explicit decision not to but I will say it is.

**[35:44](https://youtube.com/watch?v=-GqO9o51jcM&t=2144s)** I don't know how much.

**[35:45](https://youtube.com/watch?v=-GqO9o51jcM&t=2145s)** No, I'm going to say no.

**[35:46](https://youtube.com/watch?v=-GqO9o51jcM&t=2146s)** I don't want to get in trouble.

**[35:47](https://youtube.com/watch?v=-GqO9o51jcM&t=2147s)** We're on a live stream.

**[35:48](https://youtube.com/watch?v=-GqO9o51jcM&t=2148s)** It's a lot of traffic.

**[35:49](https://youtube.com/watch?v=-GqO9o51jcM&t=2149s)** Right.

**[35:50](https://youtube.com/watch?v=-GqO9o51jcM&t=2150s)** Like let's put it this way.

**[35:51](https://youtube.com/watch?v=-GqO9o51jcM&t=2151s)** It's a lot of traffic.

**[35:52](https://youtube.com/watch?v=-GqO9o51jcM&t=2152s)** Right.

**[35:53](https://youtube.com/watch?v=-GqO9o51jcM&t=2153s)** It's a joke to our Derp server team that were basically a CDN that has a client attached to it right because we're pushing.

**[35:58](https://youtube.com/watch?v=-GqO9o51jcM&t=2158s)** Outrageous amounts of traffic and I will also point out we don't bill you for this right like.

**[36:04](https://youtube.com/watch?v=-GqO9o51jcM&t=2164s)** I think I constantly see these comments after the series C and in Reddit and in how can you be like.

**[36:12](https://youtube.com/watch?v=-GqO9o51jcM&t=2172s)** It's a matter of time if our tail scale sells out and I'm like.

**[36:16](https://youtube.com/watch?v=-GqO9o51jcM&t=2176s)** We have been not charging you for bandwidth for the past five years.

**[36:20](https://youtube.com/watch?v=-GqO9o51jcM&t=2180s)** You're worried we're going to sell out right like.

**[36:22](https://youtube.com/watch?v=-GqO9o51jcM&t=2182s)** We could have charged you for bandwidth a long time ago and we haven't done that.

**[36:26](https://youtube.com/watch?v=-GqO9o51jcM&t=2186s)** So you know, we we are here to make your life better.

**[36:30](https://youtube.com/watch?v=-GqO9o51jcM&t=2190s)** We are here to make your life easier to connect to things.

**[36:34](https://youtube.com/watch?v=-GqO9o51jcM&t=2194s)** And you know, we push a lot of traffic on your behalf through our Derp servers as a result of that.

**[36:39](https://youtube.com/watch?v=-GqO9o51jcM&t=2199s)** You know, we spend hundreds of like.

**[36:42](https://youtube.com/watch?v=-GqO9o51jcM&t=2202s)** I'm just going to give a number that we spend a lot of money on bandwidth.

**[36:46](https://youtube.com/watch?v=-GqO9o51jcM&t=2206s)** I don't want to give too much information away right now, but generally it's a lot of traffic.

**[36:53](https://youtube.com/watch?v=-GqO9o51jcM&t=2213s)** It's a substantial amount.

**[36:56](https://youtube.com/watch?v=-GqO9o51jcM&t=2216s)** We can't blame you for thinking these things either.

**[36:59](https://youtube.com/watch?v=-GqO9o51jcM&t=2219s)** I mean, particularly if you're in the self-hosted ecosystem like I am,

**[37:02](https://youtube.com/watch?v=-GqO9o51jcM&t=2222s)** just look at what plexer up to lately.

**[37:04](https://youtube.com/watch?v=-GqO9o51jcM&t=2224s)** Like just inshitifying their thrive and center.

**[37:07](https://youtube.com/watch?v=-GqO9o51jcM&t=2227s)** I mean, Corey Doctorow coined this term a couple of years ago to describe what happens when a company has to monetize every single feature

**[37:16](https://youtube.com/watch?v=-GqO9o51jcM&t=2236s)** in order to stay solvent.

**[37:18](https://youtube.com/watch?v=-GqO9o51jcM&t=2238s)** Every hour CEO has gone on record sometimes on YouTube even,

**[37:22](https://youtube.com/watch?v=-GqO9o51jcM&t=2242s)** as well as our blog statings, tail scales business model is giving away for free,

**[37:27](https://youtube.com/watch?v=-GqO9o51jcM&t=2247s)** get people excited about the product and then they'll bring it to work.

**[37:31](https://youtube.com/watch?v=-GqO9o51jcM&t=2251s)** And that's where we make our money.

**[37:33](https://youtube.com/watch?v=-GqO9o51jcM&t=2253s)** So charging for a Derp servers probably not on that list, if I'm honest.

**[37:38](https://youtube.com/watch?v=-GqO9o51jcM&t=2258s)** Well, I think charging for public Derp servers is certainly not on that list.

**[37:41](https://youtube.com/watch?v=-GqO9o51jcM&t=2261s)** If we're having enough interest from people who want to run a dedicated fast lane depth server for just them,

**[37:46](https://youtube.com/watch?v=-GqO9o51jcM&t=2266s)** I think we'd definitely be open to exploring that for sure.

**[37:49](https://youtube.com/watch?v=-GqO9o51jcM&t=2269s)** Yeah.

**[37:50](https://youtube.com/watch?v=-GqO9o51jcM&t=2270s)** Okay.

**[37:51](https://youtube.com/watch?v=-GqO9o51jcM&t=2271s)** Do you happen to know much about the Android client?

**[37:53](https://youtube.com/watch?v=-GqO9o51jcM&t=2273s)** Someone's asking about the Android in 15 years.

**[37:56](https://youtube.com/watch?v=-GqO9o51jcM&t=2276s)** Okay.

**[37:57](https://youtube.com/watch?v=-GqO9o51jcM&t=2277s)** I'm going to defer to you on that one, I think.

**[37:59](https://youtube.com/watch?v=-GqO9o51jcM&t=2279s)** Yeah.

**[38:00](https://youtube.com/watch?v=-GqO9o51jcM&t=2280s)** No, I don't know.

**[38:01](https://youtube.com/watch?v=-GqO9o51jcM&t=2281s)** No signing on Android.

**[38:02](https://youtube.com/watch?v=-GqO9o51jcM&t=2282s)** I'm afraid no answer on that one.

**[38:04](https://youtube.com/watch?v=-GqO9o51jcM&t=2284s)** I'm afraid so.

**[38:05](https://youtube.com/watch?v=-GqO9o51jcM&t=2285s)** There's a nice easy question here.

**[38:07](https://youtube.com/watch?v=-GqO9o51jcM&t=2287s)** One app connect is coming out of beta any minute now.

**[38:10](https://youtube.com/watch?v=-GqO9o51jcM&t=2290s)** I.

**[38:11](https://youtube.com/watch?v=-GqO9o51jcM&t=2291s)** Any day.

**[38:12](https://youtube.com/watch?v=-GqO9o51jcM&t=2292s)** I.

**[38:13](https://youtube.com/watch?v=-GqO9o51jcM&t=2293s)** We had the internal document this like last month that was kind of like talking about making app connectors.

**[38:21](https://youtube.com/watch?v=-GqO9o51jcM&t=2301s)** GA it was approved.

**[38:23](https://youtube.com/watch?v=-GqO9o51jcM&t=2303s)** It's happening any minute now.

**[38:24](https://youtube.com/watch?v=-GqO9o51jcM&t=2304s)** Wait for the blog post.

**[38:25](https://youtube.com/watch?v=-GqO9o51jcM&t=2305s)** It will be any.

**[38:27](https://youtube.com/watch?v=-GqO9o51jcM&t=2307s)** I actually wondered if it was going to come out today.

**[38:29](https://youtube.com/watch?v=-GqO9o51jcM&t=2309s)** So yes, very, very soon.

**[38:30](https://youtube.com/watch?v=-GqO9o51jcM&t=2310s)** As the answer to that question.

**[38:33](https://youtube.com/watch?v=-GqO9o51jcM&t=2313s)** Got so many questions about Derp server.

**[38:34](https://youtube.com/watch?v=-GqO9o51jcM&t=2314s)** I think this is one of those situations where we spent a long time talking about Derp servers.

**[38:38](https://youtube.com/watch?v=-GqO9o51jcM&t=2318s)** So people ask questions about Derp servers.

**[38:40](https://youtube.com/watch?v=-GqO9o51jcM&t=2320s)** I'm really going to spend the entire time talking about Derp servers apparently.

**[38:43](https://youtube.com/watch?v=-GqO9o51jcM&t=2323s)** Yeah, that's fine.

**[38:44](https://youtube.com/watch?v=-GqO9o51jcM&t=2324s)** It's a pretty certain difference.

**[38:45](https://youtube.com/watch?v=-GqO9o51jcM&t=2325s)** You know, can we give back to the community by crowd hosting a Derp server?

**[38:50](https://youtube.com/watch?v=-GqO9o51jcM&t=2330s)** Yes, but we will not add it to net maps by default.

**[38:54](https://youtube.com/watch?v=-GqO9o51jcM&t=2334s)** Right.

**[38:55](https://youtube.com/watch?v=-GqO9o51jcM&t=2335s)** So if you want to write a Derp server and you want it to be a public Derp server.

**[38:58](https://youtube.com/watch?v=-GqO9o51jcM&t=2338s)** Totally do that.

**[38:59](https://youtube.com/watch?v=-GqO9o51jcM&t=2339s)** But tail scale networks will not use it by default.

**[39:02](https://youtube.com/watch?v=-GqO9o51jcM&t=2342s)** We have the default Derp map, which we add to when we host.

**[39:06](https://youtube.com/watch?v=-GqO9o51jcM&t=2346s)** We are not going to add random Derp servers that other people host that for security reasons.

**[39:12](https://youtube.com/watch?v=-GqO9o51jcM&t=2352s)** As you can probably imagine, right?

**[39:14](https://youtube.com/watch?v=-GqO9o51jcM&t=2354s)** Like, you know, we, we need to be able to trust the traffic and we need to be able to trust what's going in between that that infrastructure.

**[39:21](https://youtube.com/watch?v=-GqO9o51jcM&t=2361s)** But if you want to host a Derp server and you want to specify its IP addresses.

**[39:25](https://youtube.com/watch?v=-GqO9o51jcM&t=2365s)** And then publicly communicate that so people can optionally add it.

**[39:29](https://youtube.com/watch?v=-GqO9o51jcM&t=2369s)** That is totally fine.

**[39:30](https://youtube.com/watch?v=-GqO9o51jcM&t=2370s)** It's very easy to the people to add those things manually.

**[39:32](https://youtube.com/watch?v=-GqO9o51jcM&t=2372s)** So yes.

**[39:33](https://youtube.com/watch?v=-GqO9o51jcM&t=2373s)** Again, you are outside of the confines of tail scale support.

**[39:38](https://youtube.com/watch?v=-GqO9o51jcM&t=2378s)** At that point, you know, you're, you know, here be dragons, your mileage may vary.

**[39:43](https://youtube.com/watch?v=-GqO9o51jcM&t=2383s)** But if you want to host a Derp server and not make it locked down to your infrastructure, you can totally do that.

**[39:48](https://youtube.com/watch?v=-GqO9o51jcM&t=2388s)** Absolutely.

**[39:50](https://youtube.com/watch?v=-GqO9o51jcM&t=2390s)** Yeah, coloring outside the lines.

**[39:51](https://youtube.com/watch?v=-GqO9o51jcM&t=2391s)** I think it's a good way to put that one.

**[39:54](https://youtube.com/watch?v=-GqO9o51jcM&t=2394s)** It's a very nice idea, though.

**[39:56](https://youtube.com/watch?v=-GqO9o51jcM&t=2396s)** I mean, it's one of those things that if.

**[40:00](https://youtube.com/watch?v=-GqO9o51jcM&t=2400s)** I don't know.

**[40:01](https://youtube.com/watch?v=-GqO9o51jcM&t=2401s)** You want, you want the Derp servers to be absolutely 100% vetted and trusted because.

**[40:08](https://youtube.com/watch?v=-GqO9o51jcM&t=2408s)** Yes.

**[40:09](https://youtube.com/watch?v=-GqO9o51jcM&t=2409s)** Even though all the traffic traversing numbers encrypted end to end over the wide guard tunnels that tail scale operates on.

**[40:15](https://youtube.com/watch?v=-GqO9o51jcM&t=2415s)** You don't really want to have any kind of incidents related to third party Derp servers.

**[40:21](https://youtube.com/watch?v=-GqO9o51jcM&t=2421s)** So our standard dirt map will remain.

**[40:27](https://youtube.com/watch?v=-GqO9o51jcM&t=2427s)** Yeah.

**[40:28](https://youtube.com/watch?v=-GqO9o51jcM&t=2428s)** Yeah.

**[40:29](https://youtube.com/watch?v=-GqO9o51jcM&t=2429s)** Yeah.

**[40:30](https://youtube.com/watch?v=-GqO9o51jcM&t=2430s)** Yeah.

**[40:31](https://youtube.com/watch?v=-GqO9o51jcM&t=2431s)** All right.

**[40:32](https://youtube.com/watch?v=-GqO9o51jcM&t=2432s)** Let's see what else we've got in the questions.

**[40:34](https://youtube.com/watch?v=-GqO9o51jcM&t=2434s)** They are coming thick and fast today.

**[40:36](https://youtube.com/watch?v=-GqO9o51jcM&t=2436s)** We've got about 15 minutes left now.

**[40:38](https://youtube.com/watch?v=-GqO9o51jcM&t=2438s)** So we may not get to all of them.

**[40:40](https://youtube.com/watch?v=-GqO9o51jcM&t=2440s)** But thank you for asking anyway.

**[40:43](https://youtube.com/watch?v=-GqO9o51jcM&t=2443s)** All right.

**[40:44](https://youtube.com/watch?v=-GqO9o51jcM&t=2444s)** Good question here.

**[40:45](https://youtube.com/watch?v=-GqO9o51jcM&t=2445s)** I'd love to go for if you don't mind out.

**[40:47](https://youtube.com/watch?v=-GqO9o51jcM&t=2447s)** With the node limit on the account, if you hit that known limit,

**[40:51](https://youtube.com/watch?v=-GqO9o51jcM&t=2451s)** well, future nodes fail to create.

**[40:53](https://youtube.com/watch?v=-GqO9o51jcM&t=2453s)** So I think this is kind of collating two different questions together.

**[40:56](https://youtube.com/watch?v=-GqO9o51jcM&t=2456s)** So I'm going to think I'm going to read between the lines and x, y, x, y and kind of address them both.

**[41:09](https://youtube.com/watch?v=-GqO9o51jcM&t=2469s)** So the first all is that we have a soft.

**[41:12](https://youtube.com/watch?v=-GqO9o51jcM&t=2472s)** It's actually like a hard limit of 3000 nodes on a tail net, especially for personal plans.

**[41:17](https://youtube.com/watch?v=-GqO9o51jcM&t=2477s)** We can raise that limit.

**[41:19](https://youtube.com/watch?v=-GqO9o51jcM&t=2479s)** But it is something that we have to do.

**[41:21](https://youtube.com/watch?v=-GqO9o51jcM&t=2481s)** We need to contact us if you want more than 3000 notes.

**[41:24](https://youtube.com/watch?v=-GqO9o51jcM&t=2484s)** Part of the reason for that is.

**[41:26](https://youtube.com/watch?v=-GqO9o51jcM&t=2486s)** Excuse me.

**[41:28](https://youtube.com/watch?v=-GqO9o51jcM&t=2488s)** Part of the reason for that is obviously the more node you add to a tail net,

**[41:32](https://youtube.com/watch?v=-GqO9o51jcM&t=2492s)** the more traffic there is in terms of the net map we send out.

**[41:37](https://youtube.com/watch?v=-GqO9o51jcM&t=2497s)** So.

**[41:38](https://youtube.com/watch?v=-GqO9o51jcM&t=2498s)** You know, from a from a size perspective,

**[41:40](https://youtube.com/watch?v=-GqO9o51jcM&t=2500s)** we have tail nets that are many, many thousands of nodes.

**[41:43](https://youtube.com/watch?v=-GqO9o51jcM&t=2503s)** It's just something that we want to be able to communicate with you around that.

**[41:46](https://youtube.com/watch?v=-GqO9o51jcM&t=2506s)** I will also say if you're at 3000 nodes,

**[41:48](https://youtube.com/watch?v=-GqO9o51jcM&t=2508s)** you're almost certainly violating our terms of service.

**[41:50](https://youtube.com/watch?v=-GqO9o51jcM&t=2510s)** And you probably shouldn't be doing that because you need to pay for those devices.

**[41:54](https://youtube.com/watch?v=-GqO9o51jcM&t=2514s)** Everyone gets 100 devices by default.

**[41:56](https://youtube.com/watch?v=-GqO9o51jcM&t=2516s)** And then you're at 20 devices per, you know, per user license that you add.

**[42:02](https://youtube.com/watch?v=-GqO9o51jcM&t=2522s)** But if you're running 3000 nodes and you want to go on user,

**[42:05](https://youtube.com/watch?v=-GqO9o51jcM&t=2525s)** you are almost certainly violating our terms of service and we need to talk to you.

**[42:08](https://youtube.com/watch?v=-GqO9o51jcM&t=2528s)** So like that's step one.

**[42:11](https://youtube.com/watch?v=-GqO9o51jcM&t=2531s)** The second thing that I think this is asking is when you spin up an AWS Fargate,

**[42:15](https://youtube.com/watch?v=-GqO9o51jcM&t=2535s)** like subnet router, for example,

**[42:17](https://youtube.com/watch?v=-GqO9o51jcM&t=2537s)** you're probably making it a federal.

**[42:20](https://youtube.com/watch?v=-GqO9o51jcM&t=2540s)** And you are adding a new one.

**[42:22](https://youtube.com/watch?v=-GqO9o51jcM&t=2542s)** And then the other one is hanging around for a little bit.

**[42:26](https://youtube.com/watch?v=-GqO9o51jcM&t=2546s)** The reason for that is that we run a job to clear up a federal loads on like a,

**[42:31](https://youtube.com/watch?v=-GqO9o51jcM&t=2551s)** on like a schedule.

**[42:33](https://youtube.com/watch?v=-GqO9o51jcM&t=2553s)** And I don't know what that is off the top of my head,

**[42:35](https://youtube.com/watch?v=-GqO9o51jcM&t=2555s)** but they don't vanish immediately.

**[42:37](https://youtube.com/watch?v=-GqO9o51jcM&t=2557s)** If you want it to vanish immediately in your shutdown step within Fargate or within Docker,

**[42:43](https://youtube.com/watch?v=-GqO9o51jcM&t=2563s)** you need to run tail scale logout.

**[42:45](https://youtube.com/watch?v=-GqO9o51jcM&t=2565s)** And that will immediately remove the client from the list.

**[42:49](https://youtube.com/watch?v=-GqO9o51jcM&t=2569s)** And you won't run into any kind of limits.

**[42:52](https://youtube.com/watch?v=-GqO9o51jcM&t=2572s)** I would love to hear a little bit more about this particular use case,

**[42:55](https://youtube.com/watch?v=-GqO9o51jcM&t=2575s)** because I'm very interested in kind of what we're calling the machine to machine communication stuff.

**[43:00](https://youtube.com/watch?v=-GqO9o51jcM&t=2580s)** And so if you're running 3000 nodes or you want to run 3000 nodes in your tail scale network,

**[43:05](https://youtube.com/watch?v=-GqO9o51jcM&t=2585s)** I personally would like to hear from you.

**[43:08](https://youtube.com/watch?v=-GqO9o51jcM&t=2588s)** So I'm not going to give my email.

**[43:10](https://youtube.com/watch?v=-GqO9o51jcM&t=2590s)** It's pretty easy to find me.

**[43:12](https://youtube.com/watch?v=-GqO9o51jcM&t=2592s)** Or if you want to email sales at tailscale.com.

**[43:15](https://youtube.com/watch?v=-GqO9o51jcM&t=2595s)** We would love to talk to you.

**[43:16](https://youtube.com/watch?v=-GqO9o51jcM&t=2596s)** But I think that's what you were getting at when it talks about like,

**[43:19](https://youtube.com/watch?v=-GqO9o51jcM&t=2599s)** the old one is removed slower than the new one is added.

**[43:22](https://youtube.com/watch?v=-GqO9o51jcM&t=2602s)** So yeah.

**[43:25](https://youtube.com/watch?v=-GqO9o51jcM&t=2605s)** The chat's going bonkers asking for open sense tutorials.

**[43:28](https://youtube.com/watch?v=-GqO9o51jcM&t=2608s)** It's okay.

**[43:29](https://youtube.com/watch?v=-GqO9o51jcM&t=2609s)** People calm down.

**[43:30](https://youtube.com/watch?v=-GqO9o51jcM&t=2610s)** There's already plenty of content about open sense.

**[43:33](https://youtube.com/watch?v=-GqO9o51jcM&t=2613s)** There are two videos about open sense already as well as a blog post.

**[43:37](https://youtube.com/watch?v=-GqO9o51jcM&t=2617s)** And a huge lot of support article with those videos embedded in it.

**[43:40](https://youtube.com/watch?v=-GqO9o51jcM&t=2620s)** So if that open sense scene of content doesn't meet your needs for any reason,

**[43:45](https://youtube.com/watch?v=-GqO9o51jcM&t=2625s)** please reach out to me.

**[43:46](https://youtube.com/watch?v=-GqO9o51jcM&t=2626s)** Alex, Kate, tailscale.com.

**[43:48](https://youtube.com/watch?v=-GqO9o51jcM&t=2628s)** And I'll make another one.

**[43:50](https://youtube.com/watch?v=-GqO9o51jcM&t=2630s)** How about that?

**[43:51](https://youtube.com/watch?v=-GqO9o51jcM&t=2631s)** Allow noises.

**[43:52](https://youtube.com/watch?v=-GqO9o51jcM&t=2632s)** Allow noises.

**[43:53](https://youtube.com/watch?v=-GqO9o51jcM&t=2633s)** Exactly.

**[43:54](https://youtube.com/watch?v=-GqO9o51jcM&t=2634s)** Yeah.

**[43:55](https://youtube.com/watch?v=-GqO9o51jcM&t=2635s)** Okay.

**[43:57](https://youtube.com/watch?v=-GqO9o51jcM&t=2637s)** Is there any chance of tailscale being launched with Samsung or Sony smart TVs or make a good exit?

**[44:01](https://youtube.com/watch?v=-GqO9o51jcM&t=2641s)** And those are most of us who have our network.

**[44:04](https://youtube.com/watch?v=-GqO9o51jcM&t=2644s)** Alex, you want to try and call out?

**[44:07](https://youtube.com/watch?v=-GqO9o51jcM&t=2647s)** I don't know specifically about smart TV integrations,

**[44:11](https://youtube.com/watch?v=-GqO9o51jcM&t=2651s)** because I know that the ties in the OS that Samsung uses is pretty locked down.

**[44:15](https://youtube.com/watch?v=-GqO9o51jcM&t=2655s)** Yeah.

**[44:16](https://youtube.com/watch?v=-GqO9o51jcM&t=2656s)** What I will say is the Apple TV is right there.

**[44:19](https://youtube.com/watch?v=-GqO9o51jcM&t=2659s)** It's pretty cheap.

**[44:20](https://youtube.com/watch?v=-GqO9o51jcM&t=2660s)** And it's revised 30 bucks, right?

**[44:22](https://youtube.com/watch?v=-GqO9o51jcM&t=2662s)** You're not beholden to a specific manufacturer's rule or anything.

**[44:26](https://youtube.com/watch?v=-GqO9o51jcM&t=2666s)** I'll space you up beholden to Apple.

**[44:28](https://youtube.com/watch?v=-GqO9o51jcM&t=2668s)** But the Apple TV will sit there and sip half of what when it's not in use.

**[44:32](https://youtube.com/watch?v=-GqO9o51jcM&t=2672s)** And still function in deep sleep mode as a full subnet router.

**[44:36](https://youtube.com/watch?v=-GqO9o51jcM&t=2676s)** So it's crazy.

**[44:37](https://youtube.com/watch?v=-GqO9o51jcM&t=2677s)** For me, it's impossible to beat that really as a, as a,

**[44:40](https://youtube.com/watch?v=-GqO9o51jcM&t=2680s)** just a set and forget it remote exit node subnet router situation.

**[44:44](https://youtube.com/watch?v=-GqO9o51jcM&t=2684s)** Okay.

**[44:45](https://youtube.com/watch?v=-GqO9o51jcM&t=2685s)** And just to kind of like round out that.

**[44:47](https://youtube.com/watch?v=-GqO9o51jcM&t=2687s)** That's the thing.

**[44:48](https://youtube.com/watch?v=-GqO9o51jcM&t=2688s)** Tense goes written and go.

**[44:50](https://youtube.com/watch?v=-GqO9o51jcM&t=2690s)** It will compile to any CPU architecture that goes support generally.

**[44:54](https://youtube.com/watch?v=-GqO9o51jcM&t=2694s)** I think April falls.

**[44:56](https://youtube.com/watch?v=-GqO9o51jcM&t=2696s)** Brad,

**[44:57](https://youtube.com/watch?v=-GqO9o51jcM&t=2697s)** eponymous, Brad,

**[44:59](https://youtube.com/watch?v=-GqO9o51jcM&t=2699s)** I managed to compile it for some archaic CPU architecture.

**[45:03](https://youtube.com/watch?v=-GqO9o51jcM&t=2703s)** The, the, I had not heard of in years.

**[45:07](https://youtube.com/watch?v=-GqO9o51jcM&t=2707s)** And so we can feasibly support Samsung TV and,

**[45:11](https://youtube.com/watch?v=-GqO9o51jcM&t=2711s)** and Sony TVs.

**[45:12](https://youtube.com/watch?v=-GqO9o51jcM&t=2712s)** But the app store for those,

**[45:14](https://youtube.com/watch?v=-GqO9o51jcM&t=2714s)** for those ecosystems is extremely prohibitive.

**[45:18](https://youtube.com/watch?v=-GqO9o51jcM&t=2718s)** We do require the ability to specify a network interface in order to be an exit node.

**[45:24](https://youtube.com/watch?v=-GqO9o51jcM&t=2724s)** So you can't run it in user space mode.

**[45:26](https://youtube.com/watch?v=-GqO9o51jcM&t=2726s)** And as a result, we just wouldn't get through the app store.

**[45:29](https://youtube.com/watch?v=-GqO9o51jcM&t=2729s)** We will process even if we wanted to.

**[45:31](https://youtube.com/watch?v=-GqO9o51jcM&t=2731s)** So it's not really, you know,

**[45:33](https://youtube.com/watch?v=-GqO9o51jcM&t=2733s)** lobby Samsung and lobby Sony to let us run on play stations.

**[45:37](https://youtube.com/watch?v=-GqO9o51jcM&t=2737s)** And we're all about it.

**[45:39](https://youtube.com/watch?v=-GqO9o51jcM&t=2739s)** But ultimately, they have a closed ecosystem.

**[45:42](https://youtube.com/watch?v=-GqO9o51jcM&t=2742s)** And there's not really much we can do about that.

**[45:44](https://youtube.com/watch?v=-GqO9o51jcM&t=2744s)** Looks like from one of the comments in the chat here that Benjamin tried to do

**[45:48](https://youtube.com/watch?v=-GqO9o51jcM&t=2748s)** tail scale side load it on his Sony TV.

**[45:50](https://youtube.com/watch?v=-GqO9o51jcM&t=2750s)** I'm assuming it's an Android TV.

**[45:52](https://youtube.com/watch?v=-GqO9o51jcM&t=2752s)** But Sony somehow blocks the traffic even though DNS worked.

**[45:56](https://youtube.com/watch?v=-GqO9o51jcM&t=2756s)** So I just refer to my previous comment that the app TV is probably the easiest way to go.

**[46:00](https://youtube.com/watch?v=-GqO9o51jcM&t=2760s)** Or the Nvidia shield is also a pretty sweet option as well.

**[46:04](https://youtube.com/watch?v=-GqO9o51jcM&t=2764s)** All right.

**[46:08](https://youtube.com/watch?v=-GqO9o51jcM&t=2768s)** So the follow up to the open sense discussion saying that the open sense videos out of date

**[46:13](https://youtube.com/watch?v=-GqO9o51jcM&t=2773s)** because tail scales now in the open sense GUI.

**[46:16](https://youtube.com/watch?v=-GqO9o51jcM&t=2776s)** Technically, you are correct, which is the best kind of correct.

**[46:19](https://youtube.com/watch?v=-GqO9o51jcM&t=2779s)** Let's be fair.

**[46:20](https://youtube.com/watch?v=-GqO9o51jcM&t=2780s)** But also it's a community implementation.

**[46:23](https://youtube.com/watch?v=-GqO9o51jcM&t=2783s)** I forget the name of the chap that did it.

**[46:25](https://youtube.com/watch?v=-GqO9o51jcM&t=2785s)** I think I think it's from your neck of the woods in England Lee.

**[46:28](https://youtube.com/watch?v=-GqO9o51jcM&t=2788s)** But his name escapes me.

**[46:30](https://youtube.com/watch?v=-GqO9o51jcM&t=2790s)** It's a community implementation of tail scale in the UI of open sense.

**[46:35](https://youtube.com/watch?v=-GqO9o51jcM&t=2795s)** So the official methods still remain unchanged.

**[46:38](https://youtube.com/watch?v=-GqO9o51jcM&t=2798s)** So the videos also technically up to date.

**[46:42](https://youtube.com/watch?v=-GqO9o51jcM&t=2802s)** If that makes sense, technically correct.

**[46:44](https://youtube.com/watch?v=-GqO9o51jcM&t=2804s)** We're both technically correct.

**[46:46](https://youtube.com/watch?v=-GqO9o51jcM&t=2806s)** How about that?

**[46:47](https://youtube.com/watch?v=-GqO9o51jcM&t=2807s)** Indeed.

**[46:48](https://youtube.com/watch?v=-GqO9o51jcM&t=2808s)** Yeah, always technically.

**[46:49](https://youtube.com/watch?v=-GqO9o51jcM&t=2809s)** So we have our weekly conversation around direct connections.

**[46:51](https://youtube.com/watch?v=-GqO9o51jcM&t=2811s)** I feel like we haven't done it yet.

**[46:53](https://youtube.com/watch?v=-GqO9o51jcM&t=2813s)** And there's a question.

**[46:54](https://youtube.com/watch?v=-GqO9o51jcM&t=2814s)** Yeah, because you have a really great tool to help people diagnose stuff.

**[46:57](https://youtube.com/watch?v=-GqO9o51jcM&t=2817s)** Yes.

**[46:58](https://youtube.com/watch?v=-GqO9o51jcM&t=2818s)** Which I was using just this morning, because I love it.

**[47:01](https://youtube.com/watch?v=-GqO9o51jcM&t=2821s)** I'm glad to hear it.

**[47:02](https://youtube.com/watch?v=-GqO9o51jcM&t=2822s)** Yeah.

**[47:03](https://youtube.com/watch?v=-GqO9o51jcM&t=2823s)** I mean, we're going to get that in the client, man.

**[47:04](https://youtube.com/watch?v=-GqO9o51jcM&t=2824s)** Like I'm going to get it in the client, I think.

**[47:06](https://youtube.com/watch?v=-GqO9o51jcM&t=2826s)** And to be clear, it will.

**[47:08](https://youtube.com/watch?v=-GqO9o51jcM&t=2828s)** It will go into the client.

**[47:10](https://youtube.com/watch?v=-GqO9o51jcM&t=2830s)** But my software development skills are not meeting our bar of excellence right now.

**[47:14](https://youtube.com/watch?v=-GqO9o51jcM&t=2834s)** And so it's easier for me to write a random tool that I can put up my own yet.

**[47:18](https://youtube.com/watch?v=-GqO9o51jcM&t=2838s)** Or rather than have to be ripped to shreds by talented software engineers.

**[47:22](https://youtube.com/watch?v=-GqO9o51jcM&t=2842s)** But the question is,

**[47:25](https://youtube.com/watch?v=-GqO9o51jcM&t=2845s)** why is tail scale so aggressive with using DEP servers?

**[47:28](https://youtube.com/watch?v=-GqO9o51jcM&t=2848s)** Sometimes when I'm on a Melbourne network, it uses DEP servers,

**[47:30](https://youtube.com/watch?v=-GqO9o51jcM&t=2850s)** but using a simple wire guard tunnel just works without any relay servers.

**[47:34](https://youtube.com/watch?v=-GqO9o51jcM&t=2854s)** Well, the reason for that is.

**[47:36](https://youtube.com/watch?v=-GqO9o51jcM&t=2856s)** As always, it depends on the type of connectivity that you tell scale client has.

**[47:40](https://youtube.com/watch?v=-GqO9o51jcM&t=2860s)** If you have a standard wire guard tunnel,

**[47:43](https://youtube.com/watch?v=-GqO9o51jcM&t=2863s)** that has a public address, then show you can connect to that.

**[47:46](https://youtube.com/watch?v=-GqO9o51jcM&t=2866s)** But tail scale will also work behind net.

**[47:49](https://youtube.com/watch?v=-GqO9o51jcM&t=2869s)** And that's kind of one of its unique properties.

**[47:52](https://youtube.com/watch?v=-GqO9o51jcM&t=2872s)** So if you get the tail scale node that is behind.

**[47:57](https://youtube.com/watch?v=-GqO9o51jcM&t=2877s)** There's on the same place as your wire guard server on to a public.

**[48:02](https://youtube.com/watch?v=-GqO9o51jcM&t=2882s)** On to a public address.

**[48:03](https://youtube.com/watch?v=-GqO9o51jcM&t=2883s)** So I have no nap behind it.

**[48:04](https://youtube.com/watch?v=-GqO9o51jcM&t=2884s)** You'll also get direct connections.

**[48:06](https://youtube.com/watch?v=-GqO9o51jcM&t=2886s)** It's all a configuration problem, rather than like a tail scale problem.

**[48:10](https://youtube.com/watch?v=-GqO9o51jcM&t=2890s)** As Alex already mentioned, I wrote a tool which will diagnose the current connection that you have that can run on laptops.

**[48:15](https://youtube.com/watch?v=-GqO9o51jcM&t=2895s)** It won't run on phones yet.

**[48:17](https://youtube.com/watch?v=-GqO9o51jcM&t=2897s)** Maybe I'll try and do that.

**[48:19](https://youtube.com/watch?v=-GqO9o51jcM&t=2899s)** And if you run it on your tail scale client, it's called stunner.

**[48:25](https://youtube.com/watch?v=-GqO9o51jcM&t=2905s)** Alex also you have a link to it even share and chat.

**[48:29](https://youtube.com/watch?v=-GqO9o51jcM&t=2909s)** And Kate, maybe can trust you Kate in the back end can help us.

**[48:33](https://youtube.com/watch?v=-GqO9o51jcM&t=2913s)** But if you run that, I will tell you what we'll get direct connections to this particular client.

**[48:37](https://youtube.com/watch?v=-GqO9o51jcM&t=2917s)** And you want to get that client into no now as much as you possibly can.

**[48:41](https://youtube.com/watch?v=-GqO9o51jcM&t=2921s)** That means opening ports.

**[48:43](https://youtube.com/watch?v=-GqO9o51jcM&t=2923s)** It means giving it a public IP address.

**[48:45](https://youtube.com/watch?v=-GqO9o51jcM&t=2925s)** It means making sure that you don't have to traverse and simplify well in order to do that.

**[48:50](https://youtube.com/watch?v=-GqO9o51jcM&t=2930s)** And you will get direct connections.

**[48:52](https://youtube.com/watch?v=-GqO9o51jcM&t=2932s)** I do still feel like despite all the content that we have put out on this that it just isn't landing.

**[49:00](https://youtube.com/watch?v=-GqO9o51jcM&t=2940s)** And I wonder Alex, we've been talking about doing some content together.

**[49:05](https://youtube.com/watch?v=-GqO9o51jcM&t=2945s)** I wonder if we should do a specific YouTube video on this because I did a an hour long webinar about it last year.

**[49:12](https://youtube.com/watch?v=-GqO9o51jcM&t=2952s)** But an hour is a long time and you do a much better job of condensing information into short concise snippets.

**[49:18](https://youtube.com/watch?v=-GqO9o51jcM&t=2958s)** So maybe we should do something for this.

**[49:21](https://youtube.com/watch?v=-GqO9o51jcM&t=2961s)** You know, I earlier on recorded a 53 minute long video about how to install image a self hosted image.

**[49:32](https://youtube.com/watch?v=-GqO9o51jcM&t=2972s)** 13 minutes of that was actually the final runtime.

**[49:35](https://youtube.com/watch?v=-GqO9o51jcM&t=2975s)** So I only do a good job because of editing.

**[49:39](https://youtube.com/watch?v=-GqO9o51jcM&t=2979s)** It's a very different base to do it live.

**[49:42](https://youtube.com/watch?v=-GqO9o51jcM&t=2982s)** It's a very, very, very, it's a skill that I have absolutely zero ability at.

**[49:46](https://youtube.com/watch?v=-GqO9o51jcM&t=2986s)** So I will happily work with you on your excellent editing skills for sure.

**[49:51](https://youtube.com/watch?v=-GqO9o51jcM&t=2991s)** Yeah.

**[49:52](https://youtube.com/watch?v=-GqO9o51jcM&t=2992s)** Malik asks, what was your reaction when you saw PewDiePie using tail scale in his latest video?

**[49:59](https://youtube.com/watch?v=-GqO9o51jcM&t=2999s)** I didn't see this.

**[50:00](https://youtube.com/watch?v=-GqO9o51jcM&t=3000s)** I want to see this.

**[50:02](https://youtube.com/watch?v=-GqO9o51jcM&t=3002s)** I watched the one where he switched to Linux, which was pretty cool where he sort of raised his desktop for a bit.

**[50:08](https://youtube.com/watch?v=-GqO9o51jcM&t=3008s)** That was that was kind of fun.

**[50:09](https://youtube.com/watch?v=-GqO9o51jcM&t=3009s)** Seeing such a prominent person using was it arch or it was using hyper land on top of mental.

**[50:16](https://youtube.com/watch?v=-GqO9o51jcM&t=3016s)** I can't remember.

**[50:17](https://youtube.com/watch?v=-GqO9o51jcM&t=3017s)** Does that mean it's the year of the Linux desktop Alex?

**[50:20](https://youtube.com/watch?v=-GqO9o51jcM&t=3020s)** That's my real question.

**[50:21](https://youtube.com/watch?v=-GqO9o51jcM&t=3021s)** Is it following only here if these prominent YouTubers are switching to Linux?

**[50:25](https://youtube.com/watch?v=-GqO9o51jcM&t=3025s)** Are we at the year of the Linux desktop?

**[50:28](https://youtube.com/watch?v=-GqO9o51jcM&t=3028s)** The year of the Linux desktop.

**[50:30](https://youtube.com/watch?v=-GqO9o51jcM&t=3030s)** Actually, okay, this has been a tangent for the tail scale expert hour, but why not?

**[50:35](https://youtube.com/watch?v=-GqO9o51jcM&t=3035s)** For me, the Steam Deck did more than anything to advance the Linux desktop in the last 10 years.

**[50:42](https://youtube.com/watch?v=-GqO9o51jcM&t=3042s)** If Proton could support all of the silly anti-cheat stuff that the big guys like EA like to put, you know,

**[50:49](https://youtube.com/watch?v=-GqO9o51jcM&t=3049s)** I bought F124 last year to try and play that on my Steam Deck and it turned out I can't run F124 on my Steam Deck

**[50:58](https://youtube.com/watch?v=-GqO9o51jcM&t=3058s)** because of some stupid and anti-cheat thing that only runs on Windows.

**[51:02](https://youtube.com/watch?v=-GqO9o51jcM&t=3062s)** I'm not even playing online.

**[51:04](https://youtube.com/watch?v=-GqO9o51jcM&t=3064s)** Who can I use?

**[51:05](https://youtube.com/watch?v=-GqO9o51jcM&t=3065s)** My like, my guilty pleasure game is Red Dead Redemption 2.

**[51:10](https://youtube.com/watch?v=-GqO9o51jcM&t=3070s)** I just went to the quarantine.

**[51:11](https://youtube.com/watch?v=-GqO9o51jcM&t=3071s)** So good on the Steam Deck.

**[51:12](https://youtube.com/watch?v=-GqO9o51jcM&t=3072s)** I'm running around on a horse.

**[51:13](https://youtube.com/watch?v=-GqO9o51jcM&t=3073s)** Not only will it only work on a Windows machine.

**[51:16](https://youtube.com/watch?v=-GqO9o51jcM&t=3076s)** It will not work if you disconnected from the Internet.

**[51:20](https://youtube.com/watch?v=-GqO9o51jcM&t=3080s)** So if I get on a plane with my Azus rogue ally, I have to connect to the game.

**[51:25](https://youtube.com/watch?v=-GqO9o51jcM&t=3085s)** Then get on the plane.

**[51:27](https://youtube.com/watch?v=-GqO9o51jcM&t=3087s)** And I just don't understand it, but any minute now we're going to have a year of the Linux desktop.

**[51:33](https://youtube.com/watch?v=-GqO9o51jcM&t=3093s)** But yes, I totally agree with you that it's very frustrating.

**[51:38](https://youtube.com/watch?v=-GqO9o51jcM&t=3098s)** Let's try and squeeze in one more question.

**[51:41](https://youtube.com/watch?v=-GqO9o51jcM&t=3101s)** Let's do that.

**[51:44](https://youtube.com/watch?v=-GqO9o51jcM&t=3104s)** Nice easy one is a published roadmap for upcoming features.

**[51:47](https://youtube.com/watch?v=-GqO9o51jcM&t=3107s)** The answer is no, we have an internal roadmap.

**[51:49](https://youtube.com/watch?v=-GqO9o51jcM&t=3109s)** If those priorities change on a regular basis.

**[51:51](https://youtube.com/watch?v=-GqO9o51jcM&t=3111s)** And so we generally don't publish them publicly.

**[51:53](https://youtube.com/watch?v=-GqO9o51jcM&t=3113s)** If you want to be called a telescope customer, we're happy to share that roadmap with you.

**[51:57](https://youtube.com/watch?v=-GqO9o51jcM&t=3117s)** So you're going to influence it.

**[51:58](https://youtube.com/watch?v=-GqO9o51jcM&t=3118s)** But no, we're not going to publish a portal roadmap.

**[52:00](https://youtube.com/watch?v=-GqO9o51jcM&t=3120s)** Sorry.

**[52:01](https://youtube.com/watch?v=-GqO9o51jcM&t=3121s)** Another document for your likes.

**[52:03](https://youtube.com/watch?v=-GqO9o51jcM&t=3123s)** When using the Docker side car coming forward, arbitrary TCP and new DP packets.

**[52:08](https://youtube.com/watch?v=-GqO9o51jcM&t=3128s)** This is a personal use case where my daughter's micro server is in Docker.

**[52:11](https://youtube.com/watch?v=-GqO9o51jcM&t=3131s)** And I'm using a side car now for HTTPS.

**[52:15](https://youtube.com/watch?v=-GqO9o51jcM&t=3135s)** All right.

**[52:16](https://youtube.com/watch?v=-GqO9o51jcM&t=3136s)** This is a bit of a yak shaving exercise here.

**[52:20](https://youtube.com/watch?v=-GqO9o51jcM&t=3140s)** Because I believe that Minecraft uses quick UDP underneath,

**[52:25](https://youtube.com/watch?v=-GqO9o51jcM&t=3145s)** which I'm going to link a get I found this GitHub issue, which might.

**[52:30](https://youtube.com/watch?v=-GqO9o51jcM&t=3150s)** It might help you.

**[52:31](https://youtube.com/watch?v=-GqO9o51jcM&t=3151s)** It might just confuse you further like it did me.

**[52:34](https://youtube.com/watch?v=-GqO9o51jcM&t=3154s)** Anyway, the short version is Minecraft won't work in this fashion.

**[52:38](https://youtube.com/watch?v=-GqO9o51jcM&t=3158s)** Overtails scale serve or tail scale funnel.

**[52:41](https://youtube.com/watch?v=-GqO9o51jcM&t=3161s)** You should be able to root packets if the people are on your talent.

**[52:44](https://youtube.com/watch?v=-GqO9o51jcM&t=3164s)** If they're members of your talent, that should just work like anything else.

**[52:48](https://youtube.com/watch?v=-GqO9o51jcM&t=3168s)** But if you're trying to serve it through the reverse proxy of funnel,

**[52:53](https://youtube.com/watch?v=-GqO9o51jcM&t=3173s)** it doesn't work at this time.

**[52:54](https://youtube.com/watch?v=-GqO9o51jcM&t=3174s)** Link in the GitHub issue full details in there too,

**[52:56](https://youtube.com/watch?v=-GqO9o51jcM&t=3176s)** along with a response from Brad, who's one of our senior engineers.

**[53:00](https://youtube.com/watch?v=-GqO9o51jcM&t=3180s)** And if you don't want to use funnel,

**[53:02](https://youtube.com/watch?v=-GqO9o51jcM&t=3182s)** I think you just have to expose the part, right?

**[53:04](https://youtube.com/watch?v=-GqO9o51jcM&t=3184s)** I think that's one problem.

**[53:05](https://youtube.com/watch?v=-GqO9o51jcM&t=3185s)** One of the missing pieces when you do the Docker run for the Minecraft server,

**[53:07](https://youtube.com/watch?v=-GqO9o51jcM&t=3187s)** you have to expose the parts and like Minecraft's server has like a six or seven of them.

**[53:13](https://youtube.com/watch?v=-GqO9o51jcM&t=3193s)** If I remember, like it's not just one.

**[53:15](https://youtube.com/watch?v=-GqO9o51jcM&t=3195s)** There's like a whole bunch of them that it uses.

**[53:17](https://youtube.com/watch?v=-GqO9o51jcM&t=3197s)** And so you need to expose those parts.

**[53:19](https://youtube.com/watch?v=-GqO9o51jcM&t=3199s)** And it should work on a local trust, you know,

**[53:21](https://youtube.com/watch?v=-GqO9o51jcM&t=3201s)** because it's all lay in three basically.

**[53:23](https://youtube.com/watch?v=-GqO9o51jcM&t=3203s)** You would expose those on the sidecar container,

**[53:26](https://youtube.com/watch?v=-GqO9o51jcM&t=3206s)** not the application container itself, just to further confuse the matter.

**[53:31](https://youtube.com/watch?v=-GqO9o51jcM&t=3211s)** Yes.

**[53:32](https://youtube.com/watch?v=-GqO9o51jcM&t=3212s)** Are there any plans for direct support on my critic?

**[53:37](https://youtube.com/watch?v=-GqO9o51jcM&t=3217s)** No, no, no, no, Docker method.

**[53:40](https://youtube.com/watch?v=-GqO9o51jcM&t=3220s)** I think we've kind of covered architecture questions pretty comprehensively,

**[53:44](https://youtube.com/watch?v=-GqO9o51jcM&t=3224s)** but tail scale will run on a CPU architecture.

**[53:48](https://youtube.com/watch?v=-GqO9o51jcM&t=3228s)** The reason that we don't support my critic is because my critic has not enabled the ability to install tail scale.

**[53:54](https://youtube.com/watch?v=-GqO9o51jcM&t=3234s)** It's an operating system limitation rather than anything that tail scale is doing wrong.

**[53:58](https://youtube.com/watch?v=-GqO9o51jcM&t=3238s)** So they allow you to run Docker containers,

**[54:00](https://youtube.com/watch?v=-GqO9o51jcM&t=3240s)** which is why you can run a tail scale on Docker containers.

**[54:03](https://youtube.com/watch?v=-GqO9o51jcM&t=3243s)** But they probably don't want you butchering their operating system with random packages,

**[54:07](https://youtube.com/watch?v=-GqO9o51jcM&t=3247s)** because it would create a support burden for them.

**[54:09](https://youtube.com/watch?v=-GqO9o51jcM&t=3249s)** That's my guess.

**[54:10](https://youtube.com/watch?v=-GqO9o51jcM&t=3250s)** I don't know for sure.

**[54:11](https://youtube.com/watch?v=-GqO9o51jcM&t=3251s)** But that's the reason why we don't don't currently support that at the moment.

**[54:15](https://youtube.com/watch?v=-GqO9o51jcM&t=3255s)** So today I learned you can run containers on my critic devices.

**[54:20](https://youtube.com/watch?v=-GqO9o51jcM&t=3260s)** That's cool.

**[54:21](https://youtube.com/watch?v=-GqO9o51jcM&t=3261s)** Isn't it?

**[54:22](https://youtube.com/watch?v=-GqO9o51jcM&t=3262s)** I had loads of my chronic stuff back in like the late 2009, 2010,

**[54:28](https://youtube.com/watch?v=-GqO9o51jcM&t=3268s)** and then unified came out and just changed the game.

**[54:31](https://youtube.com/watch?v=-GqO9o51jcM&t=3271s)** Yeah.

**[54:32](https://youtube.com/watch?v=-GqO9o51jcM&t=3272s)** And I just love their equipment.

**[54:33](https://youtube.com/watch?v=-GqO9o51jcM&t=3273s)** So like I haven't used that stuff for a long time,

**[54:36](https://youtube.com/watch?v=-GqO9o51jcM&t=3276s)** but yeah, I don't see it.

**[54:38](https://youtube.com/watch?v=-GqO9o51jcM&t=3278s)** I can see why they let you run Docker containers,

**[54:40](https://youtube.com/watch?v=-GqO9o51jcM&t=3280s)** because it's all kind of like reinforced for some extent from the actual operating system.

**[54:45](https://youtube.com/watch?v=-GqO9o51jcM&t=3285s)** Right.

**[54:46](https://youtube.com/watch?v=-GqO9o51jcM&t=3286s)** But yeah.

**[54:48](https://youtube.com/watch?v=-GqO9o51jcM&t=3288s)** Interesting.

**[54:49](https://youtube.com/watch?v=-GqO9o51jcM&t=3289s)** Interesting.

**[54:50](https://youtube.com/watch?v=-GqO9o51jcM&t=3290s)** I can see there's a container here to run home assistant directly on my firewall.

**[54:54](https://youtube.com/watch?v=-GqO9o51jcM&t=3294s)** What could go wrong with that?

**[54:57](https://youtube.com/watch?v=-GqO9o51jcM&t=3297s)** What could go wrong?

**[54:59](https://youtube.com/watch?v=-GqO9o51jcM&t=3299s)** Yeah.

**[55:00](https://youtube.com/watch?v=-GqO9o51jcM&t=3300s)** Last question, I think.

**[55:02](https://youtube.com/watch?v=-GqO9o51jcM&t=3302s)** Any tail scale flavors have integrated BGP to allow active active and HA next hops sort of.

**[55:09](https://youtube.com/watch?v=-GqO9o51jcM&t=3309s)** We do support communicating with bird.

**[55:13](https://youtube.com/watch?v=-GqO9o51jcM&t=3313s)** I'm just going to try and find the doc for this.

**[55:19](https://youtube.com/watch?v=-GqO9o51jcM&t=3319s)** I usually have this.

**[55:22](https://youtube.com/watch?v=-GqO9o51jcM&t=3322s)** But we do support.

**[55:23](https://youtube.com/watch?v=-GqO9o51jcM&t=3323s)** There is a method where you can run with bird,

**[55:25](https://youtube.com/watch?v=-GqO9o51jcM&t=3325s)** which will actually advertise the subnet router that's currently team in an active passive mode,

**[55:30](https://youtube.com/watch?v=-GqO9o51jcM&t=3330s)** and it will actually fail over for you as well.

**[55:32](https://youtube.com/watch?v=-GqO9o51jcM&t=3332s)** This is a very much like your your on your own solid thing,

**[55:35](https://youtube.com/watch?v=-GqO9o51jcM&t=3335s)** but we do support a lot of bird.

**[55:37](https://youtube.com/watch?v=-GqO9o51jcM&t=3337s)** I can't find the doc for it right now,

**[55:39](https://youtube.com/watch?v=-GqO9o51jcM&t=3339s)** but if I do, I'll post it in the YouTube comments after.

**[55:42](https://youtube.com/watch?v=-GqO9o51jcM&t=3342s)** But yes, we support the bird.

**[55:46](https://youtube.com/watch?v=-GqO9o51jcM&t=3346s)** Routing Damon, or whatever it's called nowadays.

**[55:50](https://youtube.com/watch?v=-GqO9o51jcM&t=3350s)** So a little bit more about tail scale.

**[55:52](https://youtube.com/watch?v=-GqO9o51jcM&t=3352s)** How folks can get in touch with you and your team leaders to tell scale.

**[55:58](https://youtube.com/watch?v=-GqO9o51jcM&t=3358s)** Yes, so we I run the solutions engineering team,

**[56:00](https://youtube.com/watch?v=-GqO9o51jcM&t=3360s)** which is consistent growing.

**[56:01](https://youtube.com/watch?v=-GqO9o51jcM&t=3361s)** Another person adding next week, which is very exciting.

**[56:03](https://youtube.com/watch?v=-GqO9o51jcM&t=3363s)** And you know, so if you comments on reddit this week,

**[56:05](https://youtube.com/watch?v=-GqO9o51jcM&t=3365s)** and I like the sustainability of our business model.

**[56:08](https://youtube.com/watch?v=-GqO9o51jcM&t=3368s)** Well, our sales engineer and team has doubled in size this last year.

**[56:12](https://youtube.com/watch?v=-GqO9o51jcM&t=3372s)** So either I'm really part of my job or our sales requirements are growing.

**[56:16](https://youtube.com/watch?v=-GqO9o51jcM&t=3376s)** So if you want to get in touch with us,

**[56:18](https://youtube.com/watch?v=-GqO9o51jcM&t=3378s)** the support team is always available as well.

**[56:20](https://youtube.com/watch?v=-GqO9o51jcM&t=3380s)** We work very closely with this part team.

**[56:22](https://youtube.com/watch?v=-GqO9o51jcM&t=3382s)** They are wonderful and they're excellent.

**[56:24](https://youtube.com/watch?v=-GqO9o51jcM&t=3384s)** So if you want to get in touch with us,

**[56:26](https://youtube.com/watch?v=-GqO9o51jcM&t=3386s)** the support team is always available as well.

**[56:28](https://youtube.com/watch?v=-GqO9o51jcM&t=3388s)** We work very closely with this part team.

**[56:30](https://youtube.com/watch?v=-GqO9o51jcM&t=3390s)** They are wonderful and they're excellent at their jobs.

**[56:32](https://youtube.com/watch?v=-GqO9o51jcM&t=3392s)** If you want to contact sales directly,

**[56:34](https://youtube.com/watch?v=-GqO9o51jcM&t=3394s)** we have a sales contact form,

**[56:37](https://youtube.com/watch?v=-GqO9o51jcM&t=3397s)** which will get you in touch with sales.

**[56:39](https://youtube.com/watch?v=-GqO9o51jcM&t=3399s)** If you have talked to a sales person before,

**[56:41](https://youtube.com/watch?v=-GqO9o51jcM&t=3401s)** you probably like, well, I don't want to talk to sales,

**[56:43](https://youtube.com/watch?v=-GqO9o51jcM&t=3403s)** but we have a team of sales engineers who are designed to help you be successful.

**[56:47](https://youtube.com/watch?v=-GqO9o51jcM&t=3407s)** And my experience with our sales team has been that they just want to help you get to solutions as quickly as possible.

**[56:53](https://youtube.com/watch?v=-GqO9o51jcM&t=3413s)** And they're not going to, you know, bother you in general terms and hit you up with emails and all that kind of stuff.

**[56:59](https://youtube.com/watch?v=-GqO9o51jcM&t=3419s)** So if you want to talk to us,

**[57:00](https://youtube.com/watch?v=-GqO9o51jcM&t=3420s)** the sales contact form,

**[57:01](https://youtube.com/watch?v=-GqO9o51jcM&t=3421s)** hopefully our trusty backend and Kate can share that in all of the relative places.

**[57:06](https://youtube.com/watch?v=-GqO9o51jcM&t=3426s)** And then if you want to talk to our solutions engineering team,

**[57:08](https://youtube.com/watch?v=-GqO9o51jcM&t=3428s)** I'm not going to share the solutions engineering team email because it got absolutely hammered.

**[57:14](https://youtube.com/watch?v=-GqO9o51jcM&t=3434s)** The last time I did this with random questions,

**[57:16](https://youtube.com/watch?v=-GqO9o51jcM&t=3436s)** and we have to direct them all to support.

**[57:18](https://youtube.com/watch?v=-GqO9o51jcM&t=3438s)** But if you want to get in touch with us,

**[57:19](https://youtube.com/watch?v=-GqO9o51jcM&t=3439s)** we're going to have a new community space,

**[57:21](https://youtube.com/watch?v=-GqO9o51jcM&t=3441s)** very, very soon where I will be hanging out there and you'll be able to talk to us directly.

**[57:25](https://youtube.com/watch?v=-GqO9o51jcM&t=3445s)** So I'm looking forward to that as an option.

**[57:27](https://youtube.com/watch?v=-GqO9o51jcM&t=3447s)** Yeah, I'll be there too.

**[57:30](https://youtube.com/watch?v=-GqO9o51jcM&t=3450s)** When it does or does not possibly or possibly does not launch at some indeterminate time in the future,

**[57:36](https://youtube.com/watch?v=-GqO9o51jcM&t=3456s)** possibly maybe definitely not soon.

**[57:39](https://youtube.com/watch?v=-GqO9o51jcM&t=3459s)** Yes, how about that?

**[57:41](https://youtube.com/watch?v=-GqO9o51jcM&t=3461s)** As always, this has been absolutely wonderful Alex.

**[57:44](https://youtube.com/watch?v=-GqO9o51jcM&t=3464s)** I felt like garbage at the start of it and I feel slightly better now.

**[57:47](https://youtube.com/watch?v=-GqO9o51jcM&t=3467s)** I'm going to go with the adrenaline.

**[57:48](https://youtube.com/watch?v=-GqO9o51jcM&t=3468s)** Good.

**[57:50](https://youtube.com/watch?v=-GqO9o51jcM&t=3470s)** All of the British people who heard me say they were garbage there.

**[57:53](https://youtube.com/watch?v=-GqO9o51jcM&t=3473s)** I'm really sorry.

**[57:54](https://youtube.com/watch?v=-GqO9o51jcM&t=3474s)** I mean, rubbish.

**[57:55](https://youtube.com/watch?v=-GqO9o51jcM&t=3475s)** I'm in rubbish.

**[57:57](https://youtube.com/watch?v=-GqO9o51jcM&t=3477s)** But it's been a pleasure.

**[57:59](https://youtube.com/watch?v=-GqO9o51jcM&t=3479s)** As always, thank you so much for letting me join you on these amazing webinars.

**[58:04](https://youtube.com/watch?v=-GqO9o51jcM&t=3484s)** And we will see you all next month.

**[58:07](https://youtube.com/watch?v=-GqO9o51jcM&t=3487s)** Yeah, thanks guys.

**[58:08](https://youtube.com/watch?v=-GqO9o51jcM&t=3488s)** And see you next time.

**[58:10](https://youtube.com/watch?v=-GqO9o51jcM&t=3490s)** Bye.

**[58:11](https://youtube.com/watch?v=-GqO9o51jcM&t=3491s)** Bye.

---

*Automatically generated transcript. May contain errors.*
