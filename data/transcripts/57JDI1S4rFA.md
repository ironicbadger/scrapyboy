---
video_id: "57JDI1S4rFA"
title: "Ask a Tailscale Expert"
description: "Join and have your questions answered by Tailscale experts Alex and Jay in real time...."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-09-25"
duration_seconds: 3613
youtube_url: "https://www.youtube.com/watch?v=57JDI1S4rFA"
thumbnail_url: "https://i.ytimg.com/vi/57JDI1S4rFA/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:09:31.846670"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 9312
transcription_time_seconds: 88.5
---

# Ask a Tailscale Expert

**[00:00](https://youtube.com/watch?v=57JDI1S4rFA&t=0s)** We are live on YouTube. Hello to everybody that's watching. We are live on YouTube and also live on Zoom as well. Welcome into the Ask an Expert hour here on, I almost said, Tailscale TV. That's some forward projection right there. I'm joined by Jay Stapleton today, who is one of our solutions engineers. Hey, Jay, how are you? Just peachy. Just peachy. Well, we're going to affectionately shoot the, well, I can't say that other one.

**[00:30](https://youtube.com/watch?v=57JDI1S4rFA&t=30s)** We're just going to shoot the breeze, I suppose, is what I can say. For the next few minutes, whilst we wait for people to roll in and figure out that we're actually live and all that stuff. I know that you are in the midst of switching out phones at the minute, though, because I've just done my iPhone data transfer. You're a graphene OS chap, though. I just discovered. Yeah. I'm running graphene OS on my Pixel 7.

**[01:00](https://youtube.com/watch?v=57JDI1S4rFA&t=60s)** Pixel 7 Pro with the fancy lenticular tailscale sticker on the back. Yeah. Nice. And I'm going. Can you comments asking how we, how people get those? Thanks Jay. Come visit us at a conference and hopefully we still have some left. I'm going in today to pre-order the Pixel 10 Pro Fold. One of our colleagues, James has the Pixel 9 Pro Fold.

**[01:30](https://youtube.com/watch?v=57JDI1S4rFA&t=90s)** And I was playing with it at an offsite. And I could get into this a little more screen real estate for my, my old eyes, you know, are going from my three large monitors to this tiny little screen.

**[01:46](https://youtube.com/watch?v=57JDI1S4rFA&t=106s)** Yeah, particularly if you ever need to bring up a, like a terminal client or anything, to do any there, I say real work. You know what I mean, right? Where you want to type weird characters and symbols and I got a keyboard that muscle memory, you know, fast, but on a phone screen.

**[02:04](https://youtube.com/watch?v=57JDI1S4rFA&t=124s)** I've got a little Bluetooth keyboard that I keep in my go bag. So if I'm traveling and I only have my phone, I've definitely been known to SSH over tailscale, of course, into my infrastructure. So I can do things like reset a frozen Postgres or, you know, restart and Apache to somewhere.

**[02:29](https://youtube.com/watch?v=57JDI1S4rFA&t=149s)** Boy, that's the way to do it. I remember so that this is like an ancient history tailscale story. I don't know if I've told on the channel, but my very first conference with tailscale as a developer relations person was there upstairs Chicago back in, I guess, 2023 or so.

**[02:48](https://youtube.com/watch?v=57JDI1S4rFA&t=168s)** And, you know, me being cock sure, knowing full well what SSH was, I was like, oh, yeah, I don't really understand what tailscale SSH by ads. So don't really get what it brings to the picture.

**[03:00](https://youtube.com/watch?v=57JDI1S4rFA&t=180s)** And Jeremy, I don't know if you remember Jeremy back then, um, said to me, yeah, but you don't need to manage SSH keys anymore. And I'm like, yeah, but then I have to use tailscale SSH host name and my muscle memory just uses SSH host name.

**[03:15](https://youtube.com/watch?v=57JDI1S4rFA&t=195s)** And he was like, just try it. Just try it. My mind that day, I was like, oh, so the tailscale SSH listener on the remote node is like intercepting traffic as long as the packets traverse the tailnet to get to the destination.

**[03:31](https://youtube.com/watch?v=57JDI1S4rFA&t=211s)** You mean, I don't have to worry about SSH keys anymore like my mind that day was was blown. And of course, you can just do it straight from a phone as well. So if you're on a specific tailnet on your phone.

**[03:42](https://youtube.com/watch?v=57JDI1S4rFA&t=222s)** That's a great use case. Not worth to worry about authentication, you know, being a long time Linux nerd and having been a Linux admin for decades, a tailscale SSH is probably my favorite part of the product.

**[03:57](https://youtube.com/watch?v=57JDI1S4rFA&t=237s)** Like we do so many things, but so much like it has been my job to go around to every production machine and make sure that the pre shared keys for people who have left the company are cleaned up.

**[04:12](https://youtube.com/watch?v=57JDI1S4rFA&t=252s)** And I got to say the first time I did that at one role, there were things that had been in there for five plus years of people that no longer existed in the organization. And that's just a scary place to be.

**[04:27](https://youtube.com/watch?v=57JDI1S4rFA&t=267s)** And then that sort of led me to think about, well, shoot, now I can access anything over my talent. And then we proceeded to discuss ACLs on how they can sort of lock things down for you if you need them to. But anyway, I think we are probably what five minutes in now. So hello, if you're watching some grand rules and little explanation of what we're doing here today.

**[04:51](https://youtube.com/watch?v=57JDI1S4rFA&t=291s)** Jane, are you going to sit here and take a questions about tailscale and try try our very best to answer them in real time, if we can.

**[05:00](https://youtube.com/watch?v=57JDI1S4rFA&t=300s)** If you want to ask us a question, please use the YouTube live chat. We've also got on our brand new discord server discord.gge slash tailscale.

**[05:10](https://youtube.com/watch?v=57JDI1S4rFA&t=310s)** There is an in the comments room, which I have opened on my screen and I'll be keeping a lookout as well.

**[05:15](https://youtube.com/watch?v=57JDI1S4rFA&t=315s)** There's also a third place you can put questions and comments in the zoom chat. So if you're joining us through zoom, hello, please use the Q&A feature on zoom so that I'll produce a rob can put the questions into a doc that Jay and I can both see very much appreciate that.

**[05:30](https://youtube.com/watch?v=57JDI1S4rFA&t=330s)** Now before we get started too much further into the main format of the of today's show.

**[05:37](https://youtube.com/watch?v=57JDI1S4rFA&t=337s)** And you have been busy tailscaling up the retro gaming console to end all retro gaming consoles. Am I right?

**[05:46](https://youtube.com/watch?v=57JDI1S4rFA&t=346s)** I really like retro gaming NES games, you know, old DOS games, I'm a sucker for Commander Keen. I found an old 286 laptop that was fried. And so I replaced the screen with this LCD from an old iPad.

**[06:02](https://youtube.com/watch?v=57JDI1S4rFA&t=362s)** It's now got a Raspberry Pi 5 in there with an NVMe hat.

**[06:06](https://youtube.com/watch?v=57JDI1S4rFA&t=366s)** And I've done other projects in the past around retro gaming like this one here, which is just a Raspberry Pi.

**[06:15](https://youtube.com/watch?v=57JDI1S4rFA&t=375s)** The Nenol W and this is missing its controller right now, but I'm now setting these all back up and using tailscale to sync my saved game data.

**[06:26](https://youtube.com/watch?v=57JDI1S4rFA&t=386s)** So I could be playing Final Fantasy on the laptop and then when it's time to move to a smaller screen, continue my game on these mobile devices.

**[06:36](https://youtube.com/watch?v=57JDI1S4rFA&t=396s)** So Alex has threatened to do a full video about this in the future. So maybe we'll go into more depth on it.

**[06:43](https://youtube.com/watch?v=57JDI1S4rFA&t=403s)** I think the audience needs to see it to be honest, you were describing to me in our sort of pre show everything all about these devices and I was like, hold up.

**[06:53](https://youtube.com/watch?v=57JDI1S4rFA&t=413s)** You're using an old iPad screen, but you're using a Raspberry Pi 5 to drive an old iPad screen.

**[06:59](https://youtube.com/watch?v=57JDI1S4rFA&t=419s)** Yeah, first of all, that's amazing because there's just this little hardware board that is like a display driver for the iPad.

**[07:06](https://youtube.com/watch?v=57JDI1S4rFA&t=426s)** Yeah, where did you, did you pull the screen yourself out of the old iPad? Was it?

**[07:10](https://youtube.com/watch?v=57JDI1S4rFA&t=430s)** Yeah, in a previous life, I did a lot of iPod repairs when I worked in a small mom and pop computer shop.

**[07:18](https://youtube.com/watch?v=57JDI1S4rFA&t=438s)** So I'm in a lot of laptop repairs. So I'm pretty comfortable taking things apart and doing like component level soldering where needed.

**[07:27](https://youtube.com/watch?v=57JDI1S4rFA&t=447s)** No, soldering needed on this though. I just bought a board from eBay that plugged right into it and has a HDMI port on it.

**[07:35](https://youtube.com/watch?v=57JDI1S4rFA&t=455s)** So and there's nothing more to it. It's yeah, row hit or D row hits in the chat says home lab is about recycling junk and making it work.

**[07:46](https://youtube.com/watch?v=57JDI1S4rFA&t=466s)** Exactly.

**[07:47](https://youtube.com/watch?v=57JDI1S4rFA&t=467s)** Couldn't have said it better myself. Absolutely.

**[07:50](https://youtube.com/watch?v=57JDI1S4rFA&t=470s)** Well, we will do, I think a dedicated video on that in the future.

**[07:54](https://youtube.com/watch?v=57JDI1S4rFA&t=474s)** If you'd like to see that, please leave a thumbs up emoji in the YouTube chat or something like that.

**[07:58](https://youtube.com/watch?v=57JDI1S4rFA&t=478s)** Give us an idea of how much you'd like to see.

**[08:00](https://youtube.com/watch?v=57JDI1S4rFA&t=480s)** J's retro gaming console empire broken down on the tail scale YouTube channel.

**[08:05](https://youtube.com/watch?v=57JDI1S4rFA&t=485s)** I mean, we do have to bring it back to tail scale at some point.

**[08:08](https://youtube.com/watch?v=57JDI1S4rFA&t=488s)** No, where's the tail scale piece in all of this?

**[08:11](https://youtube.com/watch?v=57JDI1S4rFA&t=491s)** I'm using tail scale to sink my saved games between all the devices.

**[08:17](https://youtube.com/watch?v=57JDI1S4rFA&t=497s)** I'm on a final fantasy kick right now, which is not the fastest games to solve.

**[08:24](https://youtube.com/watch?v=57JDI1S4rFA&t=504s)** I've been going through final fantasy one for a few weeks now.

**[08:27](https://youtube.com/watch?v=57JDI1S4rFA&t=507s)** And I can play on the laptop for a while and then switch to this when I want to move to the couch and just pick up the game where I left off.

**[08:39](https://youtube.com/watch?v=57JDI1S4rFA&t=519s)** That's really cool. So how are you sinking?

**[08:42](https://youtube.com/watch?v=57JDI1S4rFA&t=522s)** It was there was the software underneath the sink sink sink to say our sink.

**[08:47](https://youtube.com/watch?v=57JDI1S4rFA&t=527s)** Yeah, like I said, I'm a Linux admin from years back.

**[08:53](https://youtube.com/watch?v=57JDI1S4rFA&t=533s)** If I can use our sink for anything, I'll do that.

**[08:56](https://youtube.com/watch?v=57JDI1S4rFA&t=536s)** So, but I can take this traveling, whereas packing the giant 286 looking laptop might raise some eyebrows in certain airports.

**[09:09](https://youtube.com/watch?v=57JDI1S4rFA&t=549s)** This is a little more convenient.

**[09:12](https://youtube.com/watch?v=57JDI1S4rFA&t=552s)** My first ever computer was a 286.

**[09:14](https://youtube.com/watch?v=57JDI1S4rFA&t=554s)** My dad rescued out of a skip at work.

**[09:19](https://youtube.com/watch?v=57JDI1S4rFA&t=559s)** I think my second one had a four gigabyte hard drive because I remember playing monster truck madness on that thing.

**[09:25](https://youtube.com/watch?v=57JDI1S4rFA&t=565s)** Back in the day.

**[09:27](https://youtube.com/watch?v=57JDI1S4rFA&t=567s)** And I don't remember what the first one has, but I do remember the CPU is a 286 and it ran Windows 3.1, 3.11 or whatever it was.

**[09:35](https://youtube.com/watch?v=57JDI1S4rFA&t=575s)** I used to play Lemmings until the sun went down.

**[09:39](https://youtube.com/watch?v=57JDI1S4rFA&t=579s)** It was a great game. I've got Lemmings on that box back there.

**[09:45](https://youtube.com/watch?v=57JDI1S4rFA&t=585s)** So I see we've got some questions trickling in now that we've gone completely off the rails here.

**[09:53](https://youtube.com/watch?v=57JDI1S4rFA&t=593s)** Yeah, a little bit.

**[09:54](https://youtube.com/watch?v=57JDI1S4rFA&t=594s)** I actually didn't know the question, the answer to this first question before we started,

**[10:00](https://youtube.com/watch?v=57JDI1S4rFA&t=600s)** but because the person submitted it just before we went live,

**[10:04](https://youtube.com/watch?v=57JDI1S4rFA&t=604s)** had time to get an answer from one of our engineers.

**[10:07](https://youtube.com/watch?v=57JDI1S4rFA&t=607s)** And somebody asked, I've noticed that magic DNS seems to always prefer IPv4.

**[10:12](https://youtube.com/watch?v=57JDI1S4rFA&t=612s)** Is there a way to prefer IPv6 instead?

**[10:16](https://youtube.com/watch?v=57JDI1S4rFA&t=616s)** And there is.

**[10:18](https://youtube.com/watch?v=57JDI1S4rFA&t=618s)** It's a node attribute that you can add to your policy file with a target of star and an

**[10:27](https://youtube.com/watch?v=57JDI1S4rFA&t=627s)** adder of magic DNS dash AAAAA.

**[10:32](https://youtube.com/watch?v=57JDI1S4rFA&t=632s)** I don't believe this is documented anywhere, but now you've heard it.

**[10:37](https://youtube.com/watch?v=57JDI1S4rFA&t=637s)** We'll post that somewhere where you don't have to rely on my narration to type it back out.

**[10:45](https://youtube.com/watch?v=57JDI1S4rFA&t=645s)** So if this, I believe this came in on a YouTube comment and maybe our intrepid producer

**[10:53](https://youtube.com/watch?v=57JDI1S4rFA&t=653s)** could copy and paste it into a reply there.

**[10:58](https://youtube.com/watch?v=57JDI1S4rFA&t=658s)** But if not, I'll do that after the call.

**[11:03](https://youtube.com/watch?v=57JDI1S4rFA&t=663s)** You know, it's, I've never really considered that as being a,

**[11:08](https://youtube.com/watch?v=57JDI1S4rFA&t=668s)** as being a, it's not, it's not even a problem.

**[11:11](https://youtube.com/watch?v=57JDI1S4rFA&t=671s)** But like, I personally, my mental model of networks is, I just don't really,

**[11:17](https://youtube.com/watch?v=57JDI1S4rFA&t=677s)** I have never really cropped IPv6 every time I've tried to.

**[11:21](https://youtube.com/watch?v=57JDI1S4rFA&t=681s)** I end up in this horrible loop of watching a thousand YouTube videos and still understanding

**[11:27](https://youtube.com/watch?v=57JDI1S4rFA&t=687s)** nothing but the time I get to the end of it. So it's a great question.

**[11:31](https://youtube.com/watch?v=57JDI1S4rFA&t=691s)** I didn't even know that you could do that with a node attribute.

**[11:34](https://youtube.com/watch?v=57JDI1S4rFA&t=694s)** So thanks for sharing that.

**[11:35](https://youtube.com/watch?v=57JDI1S4rFA&t=695s)** Yeah, me neither.

**[11:36](https://youtube.com/watch?v=57JDI1S4rFA&t=696s)** And actually, the engineer who answered close from our engine team said that he noticed that

**[11:45](https://youtube.com/watch?v=57JDI1S4rFA&t=705s)** we had it in one of our corporate environments and tried it out and found out what it did.

**[11:49](https://youtube.com/watch?v=57JDI1S4rFA&t=709s)** So it's so undocumented that not even our whole engineering team knew about it.

**[11:56](https://youtube.com/watch?v=57JDI1S4rFA&t=716s)** As a question here, come in asking, are there any plans to add by assumed DUP servers

**[12:02](https://youtube.com/watch?v=57JDI1S4rFA&t=722s)** or any kind of sales-scale servers in Latin America?

**[12:06](https://youtube.com/watch?v=57JDI1S4rFA&t=726s)** Columbia apparently is getting a pretty beefy bandwidth upgrade soon.

**[12:10](https://youtube.com/watch?v=57JDI1S4rFA&t=730s)** Yeah, so I can't speak for the DUP team, but we are constantly keeping an eye on traffic

**[12:18](https://youtube.com/watch?v=57JDI1S4rFA&t=738s)** and where we gather metrics about the latency that people are experiencing.

**[12:24](https://youtube.com/watch?v=57JDI1S4rFA&t=744s)** But whenever it comes down to talking about DUP servers and prioritizing DUP servers,

**[12:32](https://youtube.com/watch?v=57JDI1S4rFA&t=752s)** there's a couple of things that I will always go back to and that is we try not to use the DUP servers.

**[12:39](https://youtube.com/watch?v=57JDI1S4rFA&t=759s)** So most of the time, we can orchestrate something to get you a direct connection.

**[12:44](https://youtube.com/watch?v=57JDI1S4rFA&t=764s)** And for those cases where DUP servers currently are going to be required,

**[12:53](https://youtube.com/watch?v=57JDI1S4rFA&t=773s)** maybe you're behind a double-net or you're behind something that blocks all UDP,

**[13:01](https://youtube.com/watch?v=57JDI1S4rFA&t=781s)** we have a new feature that is lending, it either just came out or it's just about to

**[13:10](https://youtube.com/watch?v=57JDI1S4rFA&t=790s)** call Peer Relay. And I think Alex and I are going to be doing a bigger talk about this

**[13:16](https://youtube.com/watch?v=57JDI1S4rFA&t=796s)** in the not-too-distant future, where a machine where you can get direct connections

**[13:22](https://youtube.com/watch?v=57JDI1S4rFA&t=802s)** that is proximal to the machine where you can't is going to be able to lily-pad those for you.

**[13:31](https://youtube.com/watch?v=57JDI1S4rFA&t=811s)** So I think that is what does lily-padding mean for those who aren't?

**[13:36](https://youtube.com/watch?v=57JDI1S4rFA&t=816s)** picturing a frog jumping across a pond sort of thing. It gives you an extra hop in your path,

**[13:44](https://youtube.com/watch?v=57JDI1S4rFA&t=824s)** but without having to deal with the QLS or in this case the distance to the nearest DUP server.

**[13:53](https://youtube.com/watch?v=57JDI1S4rFA&t=833s)** Because the speed of light is only so fast after all.

**[13:56](https://youtube.com/watch?v=57JDI1S4rFA&t=836s)** Yeah, it's convenient, but who do you talk to about that?

**[13:59](https://youtube.com/watch?v=57JDI1S4rFA&t=839s)** Yeah, that was funnier than it should have been.

**[14:08](https://youtube.com/watch?v=57JDI1S4rFA&t=848s)** Yeah, because I realized the other day that pinging Seattle from here, I mean, I'm in Raleigh

**[14:12](https://youtube.com/watch?v=57JDI1S4rFA&t=852s)** on the East Coast, pinging Seattle for me takes just about as long as it takes to ping London,

**[14:17](https://youtube.com/watch?v=57JDI1S4rFA&t=857s)** which makes sense given the fact that they're both six, seven hour flights away from here.

**[14:25](https://youtube.com/watch?v=57JDI1S4rFA&t=865s)** Look at the car American, I've become measuring distance in hours instead of actual units.

**[14:30](https://youtube.com/watch?v=57JDI1S4rFA&t=870s)** Canadians do that as well. You know, I'm from Thunder Bay, which is seven hours from anywhere.

**[14:38](https://youtube.com/watch?v=57JDI1S4rFA&t=878s)** Thunder Bay. Oh, you bet you, right?

**[14:44](https://youtube.com/watch?v=57JDI1S4rFA&t=884s)** Should we bring it back to topic for a second? Sure, I got somebody saying, I'm interested

**[14:49](https://youtube.com/watch?v=57JDI1S4rFA&t=889s)** in switching from wire guard to tail scale. Do I still need to part forward like wire guard?

**[14:56](https://youtube.com/watch?v=57JDI1S4rFA&t=896s)** Probably not. One of the little bits magic baked into the tail scale client is

**[15:02](https://youtube.com/watch?v=57JDI1S4rFA&t=902s)** natural reversal. And as I was hinting at earlier, there are some cases where that natural

**[15:09](https://youtube.com/watch?v=57JDI1S4rFA&t=909s)** reversal won't work, like if you're on a network that blocks UDP or if you're behind a double

**[15:14](https://youtube.com/watch?v=57JDI1S4rFA&t=914s)** net situation. But in those cases, rather than failing, we fall back to a relayed connection where

**[15:21](https://youtube.com/watch?v=57JDI1S4rFA&t=921s)** your machines are still talking to each other, they're just bouncing off of one of our DURP servers.

**[15:27](https://youtube.com/watch?v=57JDI1S4rFA&t=927s)** And the DURP servers don't terminate the wire guard tunnels, so they never see your traffic.

**[15:32](https://youtube.com/watch?v=57JDI1S4rFA&t=932s)** They act basically like another internet router, just shuttling those wire guard frames.

**[15:40](https://youtube.com/watch?v=57JDI1S4rFA&t=940s)** I've had a question. We'll come back to the port forwarding wire guard thing in a minute,

**[15:45](https://youtube.com/watch?v=57JDI1S4rFA&t=945s)** but there's an important question just come through in our internal slack from Natasha, our community

**[15:49](https://youtube.com/watch?v=57JDI1S4rFA&t=949s)** manager, who says, I want to know what that screen behind Jay is doing. Now, Natasha, we can tell

**[15:55](https://youtube.com/watch?v=57JDI1S4rFA&t=955s)** you are late because we cover this at the beginning, but anyway, Jay. So I leave my retro gaming laptop,

**[16:03](https://youtube.com/watch?v=57JDI1S4rFA&t=963s)** basically just running either Tetris or Dr. Mario on demo loops, because those are the most

**[16:10](https://youtube.com/watch?v=57JDI1S4rFA&t=970s)** visually interesting without being too distracting. I'm a solutions engineer, so I talk to customers

**[16:16](https://youtube.com/watch?v=57JDI1S4rFA&t=976s)** pretty much all day. And the nature of our customers tends to break towards the nerdy.

**[16:27](https://youtube.com/watch?v=57JDI1S4rFA&t=987s)** And so a lot of people get a kick out of this. I have a conversation about it at least once a day

**[16:33](https://youtube.com/watch?v=57JDI1S4rFA&t=993s)** of somebody being like, I used to have that laptop. The old zoom backdrop game is strong with this one.

**[16:42](https://youtube.com/watch?v=57JDI1S4rFA&t=1002s)** So to come back to the port forwarding discussion about tail scale and wire guard, do I need

**[16:46](https://youtube.com/watch?v=57JDI1S4rFA&t=1006s)** to do port forwarding with tail scale? I'm going to underscore everything Jay said and be like, yes,

**[16:51](https://youtube.com/watch?v=57JDI1S4rFA&t=1011s)** and the entire magic of tail scale for me is that it no longer really matters where your infrastructure

**[17:00](https://youtube.com/watch?v=57JDI1S4rFA&t=1020s)** is. So what do I mean by that? So let's say I have a Raspberry Pi sat on this table in front of me,

**[17:06](https://youtube.com/watch?v=57JDI1S4rFA&t=1026s)** and I want to connect to it with my laptop, right? My laptop, by design, is of course a portable

**[17:17](https://youtube.com/watch?v=57JDI1S4rFA&t=1037s)** little device. So I take my laptop to the coffee shop, and I think, oh shoot, I want to SSA,

**[17:22](https://youtube.com/watch?v=57JDI1S4rFA&t=1042s)** I want to be able to control or do something, check tell the lights off from my Raspberry Pi, whatever

**[17:26](https://youtube.com/watch?v=57JDI1S4rFA&t=1046s)** it is I'm doing with my Pi. With tail scale, it does what's called natural reversal, and it kind of

**[17:31](https://youtube.com/watch?v=57JDI1S4rFA&t=1051s)** figures out a way to abuse, I don't mean to use the word abuse, but it kind of does abuse the way

**[17:37](https://youtube.com/watch?v=57JDI1S4rFA&t=1057s)** that stateful firewalls work. So without getting too much into the weeds of how that whole handshake

**[17:44](https://youtube.com/watch?v=57JDI1S4rFA&t=1064s)** occurs, an outbound packet goes outbound through a firewall, and that state is recorded somewhere

**[17:51](https://youtube.com/watch?v=57JDI1S4rFA&t=1071s)** in a table on the outbound firewall. It then hits the inbound firewall, and the inbound firewalls like,

**[17:57](https://youtube.com/watch?v=57JDI1S4rFA&t=1077s)** no, I'm not going to let you in, but the Raspberry Pi on the other end then sends a discovery packet

**[18:03](https://youtube.com/watch?v=57JDI1S4rFA&t=1083s)** out because it's talking to the tail scale coordination server, which has then been part of that

**[18:08](https://youtube.com/watch?v=57JDI1S4rFA&t=1088s)** triangle of discovery. We can then use those stateful inbound and outbound exchanges to establish

**[18:14](https://youtube.com/watch?v=57JDI1S4rFA&t=1094s)** a direct connection between those two devices, and it's a very complicated thing to try and

**[18:19](https://youtube.com/watch?v=57JDI1S4rFA&t=1099s)** explain with words. So if you're curious to learn more, we'll put a link in the all the various

**[18:25](https://youtube.com/watch?v=57JDI1S4rFA&t=1105s)** chats we have to a fantastic blog post explaining how tail scales natural reversal actually works,

**[18:31](https://youtube.com/watch?v=57JDI1S4rFA&t=1111s)** not Alex's butchered explanation of it, on our blog, a chap called Dave Anderson, one of our

**[18:37](https://youtube.com/watch?v=57JDI1S4rFA&t=1117s)** engineers wrote a post three, four years ago now on how natural reversal works, and it was one of

**[18:44](https://youtube.com/watch?v=57JDI1S4rFA&t=1124s)** I read it on my first week at tail scale, and my mind was just like, it can't possibly be so

**[18:50](https://youtube.com/watch?v=57JDI1S4rFA&t=1130s)** simple. One of those things that when someone explains it, you're like, oh, I've heard the phrase

**[18:56](https://youtube.com/watch?v=57JDI1S4rFA&t=1136s)** stateful firewalls my entire career. I didn't really understand what they meant.

**[19:02](https://youtube.com/watch?v=57JDI1S4rFA&t=1142s)** Yeah, and I just love the way that Dave Anderson lays out technical topics. He's done a few

**[19:09](https://youtube.com/watch?v=57JDI1S4rFA&t=1149s)** of these blog posts. He did a great one when he installed tail scale on his robot vacuum,

**[19:15](https://youtube.com/watch?v=57JDI1S4rFA&t=1155s)** she can cheekily call tail scale sucks. I also recommend that one because it's just a lot of fun,

**[19:22](https://youtube.com/watch?v=57JDI1S4rFA&t=1162s)** and Dave has a great way of presenting really technical topics in a really accessible way.

**[19:32](https://youtube.com/watch?v=57JDI1S4rFA&t=1172s)** What's interesting about that one is a lot of the Xiaomi and Robo Rock vacuums are actually

**[19:37](https://youtube.com/watch?v=57JDI1S4rFA&t=1177s)** just running a bun two underneath. So if you, there's an open source firmware out there for those robots

**[19:43](https://youtube.com/watch?v=57JDI1S4rFA&t=1183s)** called Valetudo, and essentially it works as like a man it, you spin up this man in the middle

**[19:49](https://youtube.com/watch?v=57JDI1S4rFA&t=1189s)** update server on your network, and then when the robot tries to phone home to get a firmware update,

**[19:55](https://youtube.com/watch?v=57JDI1S4rFA&t=1195s)** it actually goes through that server on your network, pulls down a patched firmware file that's

**[20:00](https://youtube.com/watch?v=57JDI1S4rFA&t=1200s)** rooted, and then suddenly you have root access to the a bun two system underneath, which means you

**[20:05](https://youtube.com/watch?v=57JDI1S4rFA&t=1205s)** can then install tail scale on it because it's just a bun two at the end of the day. I love that.

**[20:11](https://youtube.com/watch?v=57JDI1S4rFA&t=1211s)** Anyway, I see a question come through about TSIDP. Of course, we just did a video this week on

**[20:17](https://youtube.com/watch?v=57JDI1S4rFA&t=1217s)** tail scale identity provider TSIDP saying are there any more videos coming on this topic soon?

**[20:23](https://youtube.com/watch?v=57JDI1S4rFA&t=1223s)** Yes, soon ish maybe. The 1.0 release is coming at some point before the end of the year,

**[20:31](https://youtube.com/watch?v=57JDI1S4rFA&t=1231s)** and you can rest assured that there will be a video talking about identity and tail scales ambitions

**[20:36](https://youtube.com/watch?v=57JDI1S4rFA&t=1236s)** for becoming a platform for identity and lots of other things besides by the way,

**[20:43](https://youtube.com/watch?v=57JDI1S4rFA&t=1243s)** but at some point before the end of the year, so yes, but I don't know when exactly.

**[20:47](https://youtube.com/watch?v=57JDI1S4rFA&t=1247s)** Yeah. I saw somebody just submitted a comment and being as I'm a solutions engineer and therefore

**[20:56](https://youtube.com/watch?v=57JDI1S4rFA&t=1256s)** report up the change to the sales team, I should call this out and say that somebody mentioned

**[21:01](https://youtube.com/watch?v=57JDI1S4rFA&t=1261s)** they just found out that tail scale can build via the AWS marketplace and that help them

**[21:06](https://youtube.com/watch?v=57JDI1S4rFA&t=1266s)** get around some billing issues, and that is definitely an option if you are on one of our

**[21:13](https://youtube.com/watch?v=57JDI1S4rFA&t=1273s)** paid plans to go through the AWS or the Azure marketplace is for billing, so talk to your sales rep.

**[21:22](https://youtube.com/watch?v=57JDI1S4rFA&t=1282s)** Maybe you'll get to talk to me too. What is the best way folks can get in touch with the sales team,

**[21:29](https://youtube.com/watch?v=57JDI1S4rFA&t=1289s)** Jay? Sales at tailspeale.com is a great way. If you're not already working with a specific sales

**[21:36](https://youtube.com/watch?v=57JDI1S4rFA&t=1296s)** person that will get you rooted to whoever's next at that. And you mentioned the AWS

**[21:44](https://youtube.com/watch?v=57JDI1S4rFA&t=1304s)** billing portion, obviously that's one way. You can directly integrate your tail scale. You

**[21:48](https://youtube.com/watch?v=57JDI1S4rFA&t=1308s)** can just go to the AWS marketplace, click the tail scale button, and it will just go straight

**[21:52](https://youtube.com/watch?v=57JDI1S4rFA&t=1312s)** through your Amazon billing cycles that way. Are there any other things we do with cloud providers,

**[21:58](https://youtube.com/watch?v=57JDI1S4rFA&t=1318s)** a genuine question I don't know, but we have a tail scale billing, we have an AWS billing,

**[22:02](https://youtube.com/watch?v=57JDI1S4rFA&t=1322s)** is there any other any others? We also have not direct with the cloud providers.

**[22:10](https://youtube.com/watch?v=57JDI1S4rFA&t=1330s)** We've done a few events with AWS around marketing and whatnot, but from my side of the house,

**[22:18](https://youtube.com/watch?v=57JDI1S4rFA&t=1338s)** we have some terraform codes, some polumi code that is examples of how to spin up an auto-scaling

**[22:26](https://youtube.com/watch?v=57JDI1S4rFA&t=1346s)** group subnet router in AWS. And we've got those in our tail scale dev github repo.

**[22:35](https://youtube.com/watch?v=57JDI1S4rFA&t=1355s)** And these are things that myself or some of my colleagues have put together that we've helped

**[22:41](https://youtube.com/watch?v=57JDI1S4rFA&t=1361s)** customers find a solution for something that they're working on. And then we publish that there

**[22:48](https://youtube.com/watch?v=57JDI1S4rFA&t=1368s)** so that they're more widely available. So if you're having a problem that's an AWS infrastructure

**[22:56](https://youtube.com/watch?v=57JDI1S4rFA&t=1376s)** problem, chances are you're not the first person to do that. Tail scale has millions of tail nets now

**[23:03](https://youtube.com/watch?v=57JDI1S4rFA&t=1383s)** and a lot of people doing some truly bizarre things with the software, which I love to see

**[23:09](https://youtube.com/watch?v=57JDI1S4rFA&t=1389s)** every time. And so what's the most bizarre thing you've seen somebody do with tail scale?

**[23:16](https://youtube.com/watch?v=57JDI1S4rFA&t=1396s)** There was somebody I was talking to who was saying they were going to install us on a satellite

**[23:22](https://youtube.com/watch?v=57JDI1S4rFA&t=1402s)** for communication, which was pretty cool. My favorite go-to though is we're on a fleet of

**[23:31](https://youtube.com/watch?v=57JDI1S4rFA&t=1411s)** refrigerated trucks that need to send telemetry around food safety information like temperature

**[23:38](https://youtube.com/watch?v=57JDI1S4rFA&t=1418s)** logs back to central servers on a regular basis. They use spotty Wi-Fi and 3G modems

**[23:47](https://youtube.com/watch?v=57JDI1S4rFA&t=1427s)** because this fleet is older than the new tech. And the stability of the network is always a

**[23:56](https://youtube.com/watch?v=57JDI1S4rFA&t=1436s)** problem. And having the tunnel maintain a connection even when the underlying network is going

**[24:03](https://youtube.com/watch?v=57JDI1S4rFA&t=1443s)** through chaos means that they don't have to think about it anymore. It just works.

**[24:09](https://youtube.com/watch?v=57JDI1S4rFA&t=1449s)** Yeah, so you remember where I was talking about the natural versus earlier? I picked my laptop

**[24:13](https://youtube.com/watch?v=57JDI1S4rFA&t=1453s)** and go to the coffee shop and I can suddenly reach the Raspberry Pi on my desk.

**[24:16](https://youtube.com/watch?v=57JDI1S4rFA&t=1456s)** Well, this does translate to some really interesting and quite esoteric business use cases.

**[24:22](https://youtube.com/watch?v=57JDI1S4rFA&t=1462s)** I remember this must have been seven years ago. I went to the control room of a US freight company

**[24:30](https://youtube.com/watch?v=57JDI1S4rFA&t=1470s)** that have trucks. You've seen them, I can't, I won't name them, but you've seen their trucks on

**[24:37](https://youtube.com/watch?v=57JDI1S4rFA&t=1477s)** the road. I promise you in the States. And they had this giant control room with this huge screen

**[24:44](https://youtube.com/watch?v=57JDI1S4rFA&t=1484s)** on the wall. There were no roads marked on this map. It was just an empty silhouette of the United

**[24:52](https://youtube.com/watch?v=57JDI1S4rFA&t=1492s)** States. But you could tell where the interstates were just from the lines of the dots of where

**[24:57](https://youtube.com/watch?v=57JDI1S4rFA&t=1497s)** their trucks were and stuff. There was a few stragglers out in the middle of nowhere doing pickups

**[25:01](https://youtube.com/watch?v=57JDI1S4rFA&t=1501s)** or whatever. And I just wondered back then, how do they securely connect all these devices back

**[25:08](https://youtube.com/watch?v=57JDI1S4rFA&t=1508s)** to home base? And they had this complicated setup of bouncing through a cloud service.

**[25:14](https://youtube.com/watch?v=57JDI1S4rFA&t=1514s)** And then that cloud service was allowed in through their front door to their on-premise

**[25:18](https://youtube.com/watch?v=57JDI1S4rFA&t=1518s)** data center. And it was just this whole complicated web of stuff to go wrong. But with tail

**[25:23](https://youtube.com/watch?v=57JDI1S4rFA&t=1523s)** scale, you installed a client in the truck and then it can just reach back home without any of that

**[25:28](https://youtube.com/watch?v=57JDI1S4rFA&t=1528s)** mess. Yeah. And the solution that one of our companies that we worked with had in place before

**[25:36](https://youtube.com/watch?v=57JDI1S4rFA&t=1536s)** they moved to tail scale was they opened a port to the world and had a saved password on all of

**[25:42](https://youtube.com/watch?v=57JDI1S4rFA&t=1542s)** the devices. Yes. And it's the same password on all of the devices. So that's about as bad as

**[25:47](https://youtube.com/watch?v=57JDI1S4rFA&t=1547s)** sticking a posted note to the bottom of your monitor to be honest. Yeah. Maybe worse.

**[25:53](https://youtube.com/watch?v=57JDI1S4rFA&t=1553s)** Yeah. See Alex in the chat right on YouTube. I'd love to see a tail scale showcase. Like I

**[25:57](https://youtube.com/watch?v=57JDI1S4rFA&t=1557s)** find it really inspiring to see how others use tail scale. Maybe Jay, this is an idea for a future

**[26:03](https://youtube.com/watch?v=57JDI1S4rFA&t=1563s)** like regular segment in the podcast that you and I are threatening to do with increasing frequency

**[26:10](https://youtube.com/watch?v=57JDI1S4rFA&t=1570s)** that we should do like a tail scale showcase. Yeah. I mean, I need to get permission from my

**[26:17](https://youtube.com/watch?v=57JDI1S4rFA&t=1577s)** customers before I go into too much detail. But I've been working with a company for a few months

**[26:23](https://youtube.com/watch?v=57JDI1S4rFA&t=1583s)** now that does like QA work. And so they do a lot of automated testing. And they're really baking

**[26:30](https://youtube.com/watch?v=57JDI1S4rFA&t=1590s)** tail scale directly into their product in a really cool way. And it's something that I get really

**[26:37](https://youtube.com/watch?v=57JDI1S4rFA&t=1597s)** excited about because I'm a giant nerd. But there's also things that probably have a broader appeal.

**[26:45](https://youtube.com/watch?v=57JDI1S4rFA&t=1605s)** Being able to talk to those would be would be pretty great. So I should start putting a list

**[26:52](https://youtube.com/watch?v=57JDI1S4rFA&t=1612s)** together. I see somebody posted a question here that I think I know what's going on. They said,

**[26:59](https://youtube.com/watch?v=57JDI1S4rFA&t=1619s)** how did my user lose a tag that was applied? Thought I had an issue with my Mac and spent hours

**[27:05](https://youtube.com/watch?v=57JDI1S4rFA&t=1625s)** trying to figure out what was broken until I found it. Tags in tail scale are a bit different than

**[27:12](https://youtube.com/watch?v=57JDI1S4rFA&t=1632s)** the same word in a different context. A tag is part of our identity model. So when you tag a device,

**[27:20](https://youtube.com/watch?v=57JDI1S4rFA&t=1640s)** it is no longer associated with the user account that it was initially logged in as. So I recommend

**[27:26](https://youtube.com/watch?v=57JDI1S4rFA&t=1646s)** my customers tag shared devices, infrastructure devices, things that you don't want tied to

**[27:32](https://youtube.com/watch?v=57JDI1S4rFA&t=1652s)** a person. You know, if Alex is our IT guy and sets up our entire infrastructure and it's all logged

**[27:40](https://youtube.com/watch?v=57JDI1S4rFA&t=1660s)** in as Alex, then he wins the lottery next week and goes off and to to he when we deactivate his

**[27:47](https://youtube.com/watch?v=57JDI1S4rFA&t=1667s)** account, all of his devices go away. So we don't want that for infrastructure devices. So we use tags.

**[27:54](https://youtube.com/watch?v=57JDI1S4rFA&t=1674s)** A side effect of that is if you tag a user's device, it's not their device anymore. It is a tagged

**[28:00](https://youtube.com/watch?v=57JDI1S4rFA&t=1680s)** device. And if they log back in, it's their device again. It is no longer a tagged device. So if you

**[28:07](https://youtube.com/watch?v=57JDI1S4rFA&t=1687s)** want a way to collectively refer to a group of user's devices, you would use a group for that

**[28:16](https://youtube.com/watch?v=57JDI1S4rFA&t=1696s)** rather than a tag. And it's a a semantic difference that is specific to our context, but

**[28:24](https://youtube.com/watch?v=57JDI1S4rFA&t=1704s)** important as you start getting into the nuts and bolts and the more complex bits of your policy file.

**[28:34](https://youtube.com/watch?v=57JDI1S4rFA&t=1714s)** Have you ever wondered why in your tail scale ACLs or grounds file, it's called tag onus? Well,

**[28:40](https://youtube.com/watch?v=57JDI1S4rFA&t=1720s)** that's why. Yeah. And whoever comes the owner of the node in terms of the identity that it assumes

**[28:49](https://youtube.com/watch?v=57JDI1S4rFA&t=1729s)** on the tailnet. Sorry, Jay, go ahead. Almost. The tag owners are the people who are allowed to apply

**[28:56](https://youtube.com/watch?v=57JDI1S4rFA&t=1736s)** that tag. Admins can apply any tag, but a tag owner can apply a tag even if they're not an

**[29:06](https://youtube.com/watch?v=57JDI1S4rFA&t=1746s)** administrator confused. Yeah. Yeah, I actually do want to do a video specifically just on tagging.

**[29:17](https://youtube.com/watch?v=57JDI1S4rFA&t=1757s)** I've got quite a long list of videos to get to folks. I'm sure you'll appreciate, but

**[29:21](https://youtube.com/watch?v=57JDI1S4rFA&t=1761s)** one of the videos beyond the visual policy editor becoming a thing now. Hooray. But also is the

**[29:28](https://youtube.com/watch?v=57JDI1S4rFA&t=1768s)** nature of like node ownership and tagging and all that kind of stuff, because it is a little

**[29:33](https://youtube.com/watch?v=57JDI1S4rFA&t=1773s)** complicated when you want to get really granular with it sometimes. Like it's a powerful tool,

**[29:39](https://youtube.com/watch?v=57JDI1S4rFA&t=1779s)** and if you're wielding a powerful tool naturally, there are consequences. So you want to make sure

**[29:43](https://youtube.com/watch?v=57JDI1S4rFA&t=1783s)** you've got all the information to make those decisions moving forward. So get subscribed, like, comment,

**[29:49](https://youtube.com/watch?v=57JDI1S4rFA&t=1789s)** subscribe, and it's smash that like button. That's it. And keep an eye on the channel for more

**[29:56](https://youtube.com/watch?v=57JDI1S4rFA&t=1796s)** content about that soon. I'm going to paraphrase a question here, because they're asking

**[30:03](https://youtube.com/watch?v=57JDI1S4rFA&t=1803s)** something very specific, and I'm going to generalize it. They're asking about a way to have

**[30:08](https://youtube.com/watch?v=57JDI1S4rFA&t=1808s)** certain applications use an exit node, but not everything. And this may be useful in the case

**[30:14](https://youtube.com/watch?v=57JDI1S4rFA&t=1814s)** of geo shifting, or it may be useful in the case of, say, a SAS application that does IP allow

**[30:21](https://youtube.com/watch?v=57JDI1S4rFA&t=1821s)** listing. And rather than use an exit node for that, this is where you could have an app connector

**[30:26](https://youtube.com/watch?v=57JDI1S4rFA&t=1826s)** where you wrote by FQDN. And if you have a specific service that needs to come from a known IP

**[30:35](https://youtube.com/watch?v=57JDI1S4rFA&t=1835s)** address, you would list that service in the app connector. And then any request to, you know,

**[30:44](https://youtube.com/watch?v=57JDI1S4rFA&t=1844s)** I believe we use this internally for our Grafana server. So you have to be logged into the

**[30:50](https://youtube.com/watch?v=57JDI1S4rFA&t=1850s)** TailScale network to hit our Grafana tenant. And it just transparently gets routed whenever I type

**[30:56](https://youtube.com/watch?v=57JDI1S4rFA&t=1856s)** in grafana.com. And I don't see that happening. So for the person who asked a very specific question

**[31:05](https://youtube.com/watch?v=57JDI1S4rFA&t=1865s)** about an app being routed differently than the rest of the apps, not so much an app, but an FQDN.

**[31:12](https://youtube.com/watch?v=57JDI1S4rFA&t=1872s)** And that is a generalized solution. Yeah, split DNS is what you're referring to that, Jay, I think.

**[31:18](https://youtube.com/watch?v=57JDI1S4rFA&t=1878s)** The question I think is hoping for some kind of split tunneling on the device layer, which we don't

**[31:24](https://youtube.com/watch?v=57JDI1S4rFA&t=1884s)** support as far as I'm aware. Right. Yeah, we can't assign a tunnel per app, but the app that they

**[31:33](https://youtube.com/watch?v=57JDI1S4rFA&t=1893s)** mentioned specifically would have a set of URLs. So having an app connector handle those URLs

**[31:39](https://youtube.com/watch?v=57JDI1S4rFA&t=1899s)** would be the way to do it. Now, there was a question came in about running TailScale on an old version

**[31:46](https://youtube.com/watch?v=57JDI1S4rFA&t=1906s)** of Mac OS. I'm afraid I've lost the question on my screen here, but I have the answer.

**[31:51](https://youtube.com/watch?v=57JDI1S4rFA&t=1911s)** So as of TailScale 1.44, which came out in June 2023. So over two years ago, at this point,

**[31:59](https://youtube.com/watch?v=57JDI1S4rFA&t=1919s)** TailScale drops support for, well, go. More importantly, actually drops support for older versions of

**[32:05](https://youtube.com/watch?v=57JDI1S4rFA&t=1925s)** Mac OS. So it's, it is a TailScale limitation in so much as that we are an app-written in go,

**[32:13](https://youtube.com/watch?v=57JDI1S4rFA&t=1933s)** but the actual underlying reason as to why we don't support older versions like OS 10 versions of

**[32:19](https://youtube.com/watch?v=57JDI1S4rFA&t=1939s)** Mac OS these days is simply because go itself doesn't support old versions of Mac OS.

**[32:28](https://youtube.com/watch?v=57JDI1S4rFA&t=1948s)** Oh, I found that I'm going to cross that off the list. Had somebody ask if we, if we use

**[32:36](https://youtube.com/watch?v=57JDI1S4rFA&t=1956s)** Nix internally or just Docker, I know many of our engineers will use Nix and a couple of them

**[32:46](https://youtube.com/watch?v=57JDI1S4rFA&t=1966s)** are even nerder than me and will use Nix OS. You know, I'm here on a pop OS

**[32:54](https://youtube.com/watch?v=57JDI1S4rFA&t=1974s)** machine that I'm talking to you on now, which the real Linux nerds think that's almost windows,

**[33:01](https://youtube.com/watch?v=57JDI1S4rFA&t=1981s)** but I really enjoy it. I don't have to fight my OS on a daily basis, but I still have all the tools

**[33:08](https://youtube.com/watch?v=57JDI1S4rFA&t=1988s)** I need. You can, there's a beautiful halfway house too. Like, I mean, I obviously, I do a lot of

**[33:13](https://youtube.com/watch?v=57JDI1S4rFA&t=1993s)** video stuff in my job. And so I'm constantly using things like Final Cut and Adobe and a bunch

**[33:20](https://youtube.com/watch?v=57JDI1S4rFA&t=2000s)** of other tools that just aren't available on the Linux desktop. I have a framework over there,

**[33:26](https://youtube.com/watch?v=57JDI1S4rFA&t=2006s)** which I use when I'm doing the straight-up development work, but which has got, what's it called,

**[33:32](https://youtube.com/watch?v=57JDI1S4rFA&t=2012s)** Omachi on it at the moment, which I love Omachi by the way. It's real, I'm having a real good time

**[33:38](https://youtube.com/watch?v=57JDI1S4rFA&t=2018s)** with that. But I use Nix Darwin on my on my max to configure everything and home manager to import

**[33:45](https://youtube.com/watch?v=57JDI1S4rFA&t=2025s)** everything. And if you want to look at my Nix config, if you want to, it's on GitHub at Ironic

**[33:51](https://youtube.com/watch?v=57JDI1S4rFA&t=2031s)** Badger, Nix config. So everything is out in the open. You can go and tell me what I did wrong

**[33:57](https://youtube.com/watch?v=57JDI1S4rFA&t=2037s)** with Nix. So I probably did something wrong over there. Yeah. So it's a great, it's a great tool.

**[34:03](https://youtube.com/watch?v=57JDI1S4rFA&t=2043s)** I've got somebody here asking, is there a neat way to control tail scale ACLs?

**[34:08](https://youtube.com/watch?v=57JDI1S4rFA&t=2048s)** It's infrastructure is code, specifically terraform. And yes, you are going to tell me about

**[34:14](https://youtube.com/watch?v=57JDI1S4rFA&t=2054s)** something that you told me about two years ago when I first met you. Really? Did I tell you about

**[34:19](https://youtube.com/watch?v=57JDI1S4rFA&t=2059s)** your terraform? I just want to tell me about this tail scale. Yeah. Yeah, we have a terraform

**[34:24](https://youtube.com/watch?v=57JDI1S4rFA&t=2064s)** provider, and you can use it to manage your ACLs directly. I think our tail scale dash dev

**[34:33](https://youtube.com/watch?v=57JDI1S4rFA&t=2073s)** GitHub repo has some example code there, but if not the terraform operator docs definitely will

**[34:43](https://youtube.com/watch?v=57JDI1S4rFA&t=2083s)** dig directly into that. So you can really manage your network as code alongside the rest of your

**[34:50](https://youtube.com/watch?v=57JDI1S4rFA&t=2090s)** infrastructure as code and have a single source of truth for how things should look.

**[35:00](https://youtube.com/watch?v=57JDI1S4rFA&t=2100s)** What is GitHub's for those that aren't familiar? So I was talking about the terraform operator,

**[35:09](https://youtube.com/watch?v=57JDI1S4rFA&t=2109s)** but GitHub's is another way of operating your ACL as infrastructure as code.

**[35:17](https://youtube.com/watch?v=57JDI1S4rFA&t=2117s)** We have a runner that you can that is in GitHub that you can check in your ACL as a text file

**[35:26](https://youtube.com/watch?v=57JDI1S4rFA&t=2126s)** just like you would any other Git repo, and it will run through, validate the ACLs, and then post

**[35:33](https://youtube.com/watch?v=57JDI1S4rFA&t=2133s)** them up via the API. And that way you can use Git as your single source of truth for what the

**[35:45](https://youtube.com/watch?v=57JDI1S4rFA&t=2145s)** policy files should look like, but also have your versioning take advantage of code owners

**[35:51](https://youtube.com/watch?v=57JDI1S4rFA&t=2151s)** to make sure that any changes are approved by somebody who ought to be able to push that button

**[35:59](https://youtube.com/watch?v=57JDI1S4rFA&t=2159s)** and the ability to roll things back fairly quickly too.

**[36:04](https://youtube.com/watch?v=57JDI1S4rFA&t=2164s)** Yeah, it's really important, I think, in a less so in a personal scenario, but where you've

**[36:10](https://youtube.com/watch?v=57JDI1S4rFA&t=2170s)** got a team involved, or multiple departments, or anything like that where you need to

**[36:16](https://youtube.com/watch?v=57JDI1S4rFA&t=2176s)** I mean, we have audit logging built into every operation that gets put through the tailscarbing

**[36:20](https://youtube.com/watch?v=57JDI1S4rFA&t=2180s)** console, so you can see it's like a Git diff almost. If you manually modify the tailscale

**[36:28](https://youtube.com/watch?v=57JDI1S4rFA&t=2188s)** grants file, the policy file, that will be recorded somewhere, that will be logged somewhere,

**[36:33](https://youtube.com/watch?v=57JDI1S4rFA&t=2193s)** an auditors can go and view that and point the finger if they need to in a problem case. But

**[36:42](https://youtube.com/watch?v=57JDI1S4rFA&t=2202s)** the GitHub thing just moves that, I suppose that moment, or even that ability, it moves that

**[36:47](https://youtube.com/watch?v=57JDI1S4rFA&t=2207s)** ability to manually modify the policy file out of the tailscarbing console and into source control

**[36:53](https://youtube.com/watch?v=57JDI1S4rFA&t=2213s)** somewhere. And then you have your whole CI, CD pipeline that goes through and GitHub's style applies

**[36:59](https://youtube.com/watch?v=57JDI1S4rFA&t=2219s)** those changes. You mentioned the audit logging. Another great feature for production environments,

**[37:09](https://youtube.com/watch?v=57JDI1S4rFA&t=2229s)** especially is if you look at a change to the policy file in the audit log, it will have a revert button

**[37:17](https://youtube.com/watch?v=57JDI1S4rFA&t=2237s)** on the bottom of it. So if you push the change and it causes some problems, click on logs,

**[37:24](https://youtube.com/watch?v=57JDI1S4rFA&t=2244s)** find that entry and just hit revert and it will undo those changes very quickly.

**[37:30](https://youtube.com/watch?v=57JDI1S4rFA&t=2250s)** I have pointed that out to most of my customers as we're going through the features and how to use

**[37:35](https://youtube.com/watch?v=57JDI1S4rFA&t=2255s)** tailscale and production. And I have had a couple of people message me, you know, months or years

**[37:42](https://youtube.com/watch?v=57JDI1S4rFA&t=2262s)** down the road and say, Hey, remember when you told me about that revert button? It saved my

**[37:47](https://youtube.com/watch?v=57JDI1S4rFA&t=2267s)** bacon today because I could undo a change in 30 seconds instead of trying to figure out exactly

**[37:53](https://youtube.com/watch?v=57JDI1S4rFA&t=2273s)** which part of the file I changed caused the problem while we were in an average. Yeah, exactly.

**[38:01](https://youtube.com/watch?v=57JDI1S4rFA&t=2281s)** Now you are a Linux user, right? So that must mean that you're familiar with the pain of

**[38:05](https://youtube.com/watch?v=57JDI1S4rFA&t=2285s)** resolve.com for network manager fighting each other. Are you able to talk us through

**[38:10](https://youtube.com/watch?v=57JDI1S4rFA&t=2290s)** how one gets precedents over the other and what our users could do about them?

**[38:15](https://youtube.com/watch?v=57JDI1S4rFA&t=2295s)** Pain, I think you mean the joy of watching, yeah, watching the little robots struggle.

**[38:23](https://youtube.com/watch?v=57JDI1S4rFA&t=2303s)** You know, I don't get into the weeds of managing DNS anymore. This is one of the things I haven't

**[38:31](https://youtube.com/watch?v=57JDI1S4rFA&t=2311s)** done in years because I use tailscale everywhere and just use magic DNS and

**[38:37](https://youtube.com/watch?v=57JDI1S4rFA&t=2317s)** for quite a while, I used next DNS is my primary resolver and then I had a pie hole for a while.

**[38:46](https://youtube.com/watch?v=57JDI1S4rFA&t=2326s)** Now I'm using control D just to try that out for a bit and I hit the override local DNS switch

**[38:53](https://youtube.com/watch?v=57JDI1S4rFA&t=2333s)** and every machine is logged into tailscale and has the DNS handled. If you have a more complex

**[39:02](https://youtube.com/watch?v=57JDI1S4rFA&t=2342s)** DNS environment, specifically, if you have active directory, there are a few steps that you can

**[39:08](https://youtube.com/watch?v=57JDI1S4rFA&t=2348s)** take. But on Linux, I have one machine that I do, you can say except DNS equals false as a flag

**[39:19](https://youtube.com/watch?v=57JDI1S4rFA&t=2359s)** to tailscale set or tailscale up and you can then go back to using your system to resolve the

**[39:28](https://youtube.com/watch?v=57JDI1S4rFA&t=2368s)** to manage things as normal and how I normally do that is I just keep the the SIM link in place so

**[39:36](https://youtube.com/watch?v=57JDI1S4rFA&t=2376s)** everything that touches Etsy Resolve Conf ends up going to the right file to be read in by

**[39:46](https://youtube.com/watch?v=57JDI1S4rFA&t=2386s)** system D Resolve D. There's a comment from CLX in the chat as well saying that we have a

**[39:52](https://youtube.com/watch?v=57JDI1S4rFA&t=2392s)** comprehensive support document walking users through issues with Resolve.conf and that they

**[40:01](https://youtube.com/watch?v=57JDI1S4rFA&t=2401s)** followed the steps in there and it's fixed all their issues. So would this be with this be

**[40:07](https://youtube.com/watch?v=57JDI1S4rFA&t=2407s)** my Alex is polite with saying RTFM. I hope not, but there's kind of what I'm saying. This is a

**[40:13](https://youtube.com/watch?v=57JDI1S4rFA&t=2413s)** polite company. So you can just say RTM. Oh, I forgot, yes, it's a Canadian company isn't it?

**[40:22](https://youtube.com/watch?v=57JDI1S4rFA&t=2422s)** I have somebody here asking about a direct connection to double that. How does it work?

**[40:29](https://youtube.com/watch?v=57JDI1S4rFA&t=2429s)** It doesn't. So our net traversal magic really is, and if you read Dave Anderson's excellent

**[40:37](https://youtube.com/watch?v=57JDI1S4rFA&t=2437s)** blog posts on it, you get a lot more detailed than either Alex or I can muddle through. But

**[40:43](https://youtube.com/watch?v=57JDI1S4rFA&t=2443s)** it really does work with the nature of stable firewalls and the sort of default behavior of most

**[40:51](https://youtube.com/watch?v=57JDI1S4rFA&t=2451s)** of them to trick the firewall into letting it establish a direct connection. With double that,

**[40:58](https://youtube.com/watch?v=57JDI1S4rFA&t=2458s)** we aren't able to do that because each end of that connection is talking to a different

**[41:05](https://youtube.com/watch?v=57JDI1S4rFA&t=2465s)** next hop. So double that connections are pretty much always going to fall back to a DURP server.

**[41:18](https://youtube.com/watch?v=57JDI1S4rFA&t=2478s)** They're going to be relayed connections unless both ends have IPv6. A lot of places now that

**[41:27](https://youtube.com/watch?v=57JDI1S4rFA&t=2487s)** only offer double that connections will also give you a roadable IPv6 address in which case

**[41:33](https://youtube.com/watch?v=57JDI1S4rFA&t=2493s)** there is no net and everything just works. Everything just works. Yes. That's been my experience

**[41:42](https://youtube.com/watch?v=57JDI1S4rFA&t=2502s)** with IPv6. Yeah, everything just works. Right. Yeah. I mean, IPv6 has been around for

**[41:48](https://youtube.com/watch?v=57JDI1S4rFA&t=2508s)** 35 years now. So it's like any day now. It's just like Linux on the desktop. It's

**[41:56](https://youtube.com/watch?v=57JDI1S4rFA&t=2516s)** the year of Linux desktop and IPv6. Yeah, it's going to be the running joke before long.

**[42:01](https://youtube.com/watch?v=57JDI1S4rFA&t=2521s)** All right. So I have a question here for, well, maybe, maybe both of us.

**[42:06](https://youtube.com/watch?v=57JDI1S4rFA&t=2526s)** And any way or plans to enable or install tailscale on a risk-5 device.

**[42:11](https://youtube.com/watch?v=57JDI1S4rFA&t=2531s)** I just, I saw that question and I asked in our questions channel and our Slack.

**[42:22](https://youtube.com/watch?v=57JDI1S4rFA&t=2542s)** And we, we ship binaries for it. If you go to packages, that's pkgs.tailscale.com slash stable.

**[42:31](https://youtube.com/watch?v=57JDI1S4rFA&t=2551s)** There is a risk v64 package available right there. So. Oh, look at that.

**[42:40](https://youtube.com/watch?v=57JDI1S4rFA&t=2560s)** Today, Irissa, from our support team for finding that out in real time. For us.

**[42:50](https://youtube.com/watch?v=57JDI1S4rFA&t=2570s)** I'm curious to know, whoever asked that question, what's the risk-5 device that you're using?

**[42:55](https://youtube.com/watch?v=57JDI1S4rFA&t=2575s)** Let us know in the comments. Is it the framework? Because I was this close

**[43:01](https://youtube.com/watch?v=57JDI1S4rFA&t=2581s)** when I was building out this machine. I'm like, I could put a framework motherboard in there

**[43:06](https://youtube.com/watch?v=57JDI1S4rFA&t=2586s)** instead of a Raspberry Pi. Like I use Raspberry Pi's for everything. This could be a little more

**[43:11](https://youtube.com/watch?v=57JDI1S4rFA&t=2591s)** exciting. And like the framework risk-5 motherboard is quite reasonably priced for what you get.

**[43:20](https://youtube.com/watch?v=57JDI1S4rFA&t=2600s)** But I went with what I had on hand anyhow. So.

**[43:30](https://youtube.com/watch?v=57JDI1S4rFA&t=2610s)** All right. There's a question here from Sude here. Is it a good idea to use headscale or tailscale

**[43:35](https://youtube.com/watch?v=57JDI1S4rFA&t=2615s)** to expose a local service on a client's computer so it can reach our automation platform?

**[43:41](https://youtube.com/watch?v=57JDI1S4rFA&t=2621s)** Follow up question. What's the automation platform?

**[43:46](https://youtube.com/watch?v=57JDI1S4rFA&t=2626s)** Either role work, you know, it depends on how many clients that you're using. I will, of course,

**[43:57](https://youtube.com/watch?v=57JDI1S4rFA&t=2637s)** I work a lot with customers who do this with tailscale. You know, headscale is for those who don't

**[44:04](https://youtube.com/watch?v=57JDI1S4rFA&t=2644s)** know, was an open source re-implementation of the tailscale control plane. So it is not an official

**[44:10](https://youtube.com/watch?v=57JDI1S4rFA&t=2650s)** tailscale product, but we do work closely with the people who who built that out. In fact,

**[44:17](https://youtube.com/watch?v=57JDI1S4rFA&t=2657s)** one of them we ended up hiring and he still manages headscale, but works for tailscale.

**[44:26](https://youtube.com/watch?v=57JDI1S4rFA&t=2666s)** So we're very cognizant to not break it, but we don't support it directly. But we do have

**[44:36](https://youtube.com/watch?v=57JDI1S4rFA&t=2676s)** a number of customers who operate equipment in the their customers' environments. And I would

**[44:44](https://youtube.com/watch?v=57JDI1S4rFA&t=2684s)** say that if you're doing this widely, a big thing to keep in mind is the test section of your

**[44:54](https://youtube.com/watch?v=57JDI1S4rFA&t=2694s)** policy file. You want to make sure that under no conditions, can customer A ever see customer B's

**[45:00](https://youtube.com/watch?v=57JDI1S4rFA&t=2700s)** device. And so setting a test, which gives you these end state conditions, means that if you

**[45:09](https://youtube.com/watch?v=57JDI1S4rFA&t=2709s)** accidentally put in a two permissive policy, it won't let you save that because it violates the

**[45:16](https://youtube.com/watch?v=57JDI1S4rFA&t=2716s)** tests in place. So if you're working in a live environment in customer environments like secondary

**[45:25](https://youtube.com/watch?v=57JDI1S4rFA&t=2725s)** users, I'd say always use unit tests on your policy file. I have nothing to add. I have nothing

**[45:37](https://youtube.com/watch?v=57JDI1S4rFA&t=2737s)** further your honor. That was, that was great. Thanks, Jay. There's some chat in the YouTube comments

**[45:42](https://youtube.com/watch?v=57JDI1S4rFA&t=2742s)** talking about the automation platform was N8N in this example. Such a great application. I think

**[45:48](https://youtube.com/watch?v=57JDI1S4rFA&t=2748s)** Christian Lempers literally just put out a video today talking about N8N. I haven't had

**[45:52](https://youtube.com/watch?v=57JDI1S4rFA&t=2752s)** chance to watch it yet, but I was messing about with N8N a couple of months ago just connecting.

**[46:00](https://youtube.com/watch?v=57JDI1S4rFA&t=2760s)** It's basically like node red. And if this then that had a had a baby and out came N8N in the middle

**[46:07](https://youtube.com/watch?v=57JDI1S4rFA&t=2767s)** as this beautiful self hostable kind of automation platform of just click and join boxes together

**[46:13](https://youtube.com/watch?v=57JDI1S4rFA&t=2773s)** with lines and it will do stuff. It's it's really fun. Well, I want to do a video on it, but I just

**[46:18](https://youtube.com/watch?v=57JDI1S4rFA&t=2778s)** haven't quite figured out what the angle is yet. Yeah. I got a question here on AWS, who was

**[46:29](https://youtube.com/watch?v=57JDI1S4rFA&t=2789s)** somebody had a subnet router in AWS to connect to private subnets, but the DNS wasn't working

**[46:36](https://youtube.com/watch?v=57JDI1S4rFA&t=2796s)** because these are behind a subnet router. And they were asking if there's a way to translate DNS

**[46:42](https://youtube.com/watch?v=57JDI1S4rFA&t=2802s)** names from from the subnet. And what I generally do in AWS specifically is your row 53 resolver,

**[46:51](https://youtube.com/watch?v=57JDI1S4rFA&t=2811s)** which is the native DNS system for AWS. On whatever your private IP cider is for that subnet,

**[47:01](https://youtube.com/watch?v=57JDI1S4rFA&t=2821s)** dock two is going to be the row 53 resolver. So you can set that up as a split DNS entry

**[47:12](https://youtube.com/watch?v=57JDI1S4rFA&t=2832s)** for a subset of your devices in tail scale and use the subnet router to reach the row 53 on

**[47:23](https://youtube.com/watch?v=57JDI1S4rFA&t=2843s)** 10 dot zero dot zero dot two or 172 dot whatever dot two. And that should just work.

**[47:36](https://youtube.com/watch?v=57JDI1S4rFA&t=2856s)** Okay. There was a question came through from Bada Bada. I'm sorry. Are you guys working with

**[47:44](https://youtube.com/watch?v=57JDI1S4rFA&t=2864s)** unified to bring tail scale to the unified ecosystem? I'm aware of a Git repo and unofficial one that

**[47:49](https://youtube.com/watch?v=57JDI1S4rFA&t=2869s)** we can use, but I want something official. I don't know of any conversations happening with

**[47:58](https://youtube.com/watch?v=57JDI1S4rFA&t=2878s)** unified. If that were happening, that would probably be going through David Carney, who is one of our

**[48:06](https://youtube.com/watch?v=57JDI1S4rFA&t=2886s)** founders who works on strategic projects. I think that'd be pretty cool to have tail scale

**[48:14](https://youtube.com/watch?v=57JDI1S4rFA&t=2894s)** running on unified devices. So if you know anybody at unify, maybe I have them right off.

**[48:22](https://youtube.com/watch?v=57JDI1S4rFA&t=2902s)** Yeah. I mean, to be honest with you, I should have a long time loyalty customer discount from unify

**[48:26](https://youtube.com/watch?v=57JDI1S4rFA&t=2906s)** because literally my entire house is stuffed to the gunnels with the unify gear. There's a switch

**[48:31](https://youtube.com/watch?v=57JDI1S4rFA&t=2911s)** there. There's a switch there. There's another one in the rack over there. It's ridiculous.

**[48:36](https://youtube.com/watch?v=57JDI1S4rFA&t=2916s)** And I for the longest time, didn't run a unified firewall because I couldn't run tail scale on the

**[48:42](https://youtube.com/watch?v=57JDI1S4rFA&t=2922s)** firewall. So I stuck with open sense for a very long time because of that. In the end, I got

**[48:50](https://youtube.com/watch?v=57JDI1S4rFA&t=2930s)** cajoled by a friend of mine into buying a UDM fiber gateway cloud max prox GPOE 24 or whatever they

**[48:59](https://youtube.com/watch?v=57JDI1S4rFA&t=2939s)** called it. I don't know. And the only thing wrong with it in my mind is that it doesn't run tail

**[49:06](https://youtube.com/watch?v=57JDI1S4rFA&t=2946s)** scale officially. There are reposters as we alluded to where you can do that unofficially. So

**[49:12](https://youtube.com/watch?v=57JDI1S4rFA&t=2952s)** believe me when I say you are not alone, including tail scalers in wanting this feature.

**[49:18](https://youtube.com/watch?v=57JDI1S4rFA&t=2958s)** We just don't have it yet. I don't use my edge devices anything other than a router really.

**[49:28](https://youtube.com/watch?v=57JDI1S4rFA&t=2968s)** And I actually have a GLI net barrel, which we just had a blog post go out about a couple days ago.

**[49:36](https://youtube.com/watch?v=57JDI1S4rFA&t=2976s)** And that is inside my network and partitions off part of my network. But also runs tail scale natively.

**[49:46](https://youtube.com/watch?v=57JDI1S4rFA&t=2986s)** So for anything like my cobo, if I want to sync it over tail scale, it can do that with a

**[49:57](https://youtube.com/watch?v=57JDI1S4rFA&t=2997s)** reverse subnet router on the barrel. So I can download my books when I'm on the road because

**[50:05](https://youtube.com/watch?v=57JDI1S4rFA&t=3005s)** the barrel comes with me. Yeah, I've used those GLI net devices myself quite a few times and

**[50:12](https://youtube.com/watch?v=57JDI1S4rFA&t=3012s)** they are so handy. I know I digressing from unify a little bit here, but we went to the beach

**[50:18](https://youtube.com/watch?v=57JDI1S4rFA&t=3018s)** over the summer and the hotel we had charged by the device for Wi-Fi. I don't know what decade they

**[50:25](https://youtube.com/watch?v=57JDI1S4rFA&t=3025s)** think it is, but anyway. So I connected my GLI net slate to the Wi-Fi as the one device that I was

**[50:33](https://youtube.com/watch?v=57JDI1S4rFA&t=3033s)** going to pay for. And then everything else that was sat behind the router. The hotel had no idea.

**[50:40](https://youtube.com/watch?v=57JDI1S4rFA&t=3040s)** I had five devices connected. It was great. Yeah. And one thing I've noticed a lot because I

**[50:48](https://youtube.com/watch?v=57JDI1S4rFA&t=3048s)** travel a fair bit with work, going to conferences and whatnot. A lot of hotels now aren't using

**[50:55](https://youtube.com/watch?v=57JDI1S4rFA&t=3055s)** WPA for their Wi-Fi anymore. So there's no encryption there. So having something where you can

**[51:01](https://youtube.com/watch?v=57JDI1S4rFA&t=3061s)** write all of your traffic through an exit node means that your nerdy neighbor won't be snooping on

**[51:08](https://youtube.com/watch?v=57JDI1S4rFA&t=3068s)** what IP addresses you happen to be connecting to. There's another question in here about,

**[51:17](https://youtube.com/watch?v=57JDI1S4rFA&t=3077s)** is there a way to use proton and tail scale at the same time? And maybe you may be able to

**[51:26](https://youtube.com/watch?v=57JDI1S4rFA&t=3086s)** plummet up with custom IP tables rules. It's not a supported configuration and that is why we

**[51:34](https://youtube.com/watch?v=57JDI1S4rFA&t=3094s)** have an integration with Mulvad. Mulvad is another privacy VPN. They are a company that aligns well

**[51:42](https://youtube.com/watch?v=57JDI1S4rFA&t=3102s)** with us both technologically and ideologically. So we've set up a relationship there where you can

**[51:52](https://youtube.com/watch?v=57JDI1S4rFA&t=3112s)** buy a Mulvad subscription through tail scale and have exit nodes available to you from the Mulvad

**[51:59](https://youtube.com/watch?v=57JDI1S4rFA&t=3119s)** network. So if you want to be able to use that privacy VPN and tail scale at the same time,

**[52:06](https://youtube.com/watch?v=57JDI1S4rFA&t=3126s)** that would be the supported mechanism to do that. Now Ryan, housing comes in with a question

**[52:14](https://youtube.com/watch?v=57JDI1S4rFA&t=3134s)** that I wish I had a better answer for. Is there a way to get ESP 32 devices connected directly

**[52:21](https://youtube.com/watch?v=57JDI1S4rFA&t=3141s)** to my town? I think the answer is no, but I wanted to ask anyway. This is my new toy. I just picked

**[52:27](https://youtube.com/watch?v=57JDI1S4rFA&t=3147s)** up it's a ESP 32 e-paper. I haven't really gone into it yet. The answer is no, but it would be nice.

**[52:38](https://youtube.com/watch?v=57JDI1S4rFA&t=3158s)** I know some people have written like third party wire guard to tail scale bridges.

**[52:45](https://youtube.com/watch?v=57JDI1S4rFA&t=3165s)** You could do that in a containerized environment. That is kind of a hacky way of approaching it,

**[52:52](https://youtube.com/watch?v=57JDI1S4rFA&t=3172s)** which means I love it, but I don't recommend it. The other thing you can do of course is spin

**[52:59](https://youtube.com/watch?v=57JDI1S4rFA&t=3179s)** up a subnet router in the same network as the ESP 32. I'm sure you knew that already, but

**[53:05](https://youtube.com/watch?v=57JDI1S4rFA&t=3185s)** the ESPs in ESP homeland at least can run wire guard natively, but they don't have the user space

**[53:14](https://youtube.com/watch?v=57JDI1S4rFA&t=3194s)** that we need to run and do our thing, because it's a compiled firmware device. It's not running

**[53:20](https://youtube.com/watch?v=57JDI1S4rFA&t=3200s)** a full operating system, so it doesn't have a proper networking stack that we can kind of hook into.

**[53:24](https://youtube.com/watch?v=57JDI1S4rFA&t=3204s)** I believe is the technical answer. It was maybe a year ago I asked that question in our Slack internally,

**[53:31](https://youtube.com/watch?v=57JDI1S4rFA&t=3211s)** because that's another thing I want to see. Can I have a bunch of ESPs at my mum's house? I'd

**[53:37](https://youtube.com/watch?v=57JDI1S4rFA&t=3217s)** love to have that data feeding back into my home assistant. Little things for me like checking

**[53:43](https://youtube.com/watch?v=57JDI1S4rFA&t=3223s)** she's up and about in the morning and stuff like that. At the moment, I have a home assistant

**[53:48](https://youtube.com/watch?v=57JDI1S4rFA&t=3228s)** running in her house, and then I have that reach back out over the network. I can do it that way,

**[53:53](https://youtube.com/watch?v=57JDI1S4rFA&t=3233s)** but it just feels like an extra hop, you know what I mean?

**[53:58](https://youtube.com/watch?v=57JDI1S4rFA&t=3238s)** Short answer no. Long answer is it could be a fun project.

**[54:03](https://youtube.com/watch?v=57JDI1S4rFA&t=3243s)** Short answer no. Long answer no.

**[54:11](https://youtube.com/watch?v=57JDI1S4rFA&t=3251s)** I have somebody here asking about using two separate tailnets, and that is not currently possible,

**[54:21](https://youtube.com/watch?v=57JDI1S4rFA&t=3261s)** but short answer no, long answer kind of. One thing that I do, if I am testing something out in my

**[54:30](https://youtube.com/watch?v=57JDI1S4rFA&t=3270s)** lab environment, I still need access to some of our web-based tools that are on our corporate

**[54:36](https://youtube.com/watch?v=57JDI1S4rFA&t=3276s)** tailnet. I run a second tail scale D in user space mode and set one of my browser profiles to use

**[54:47](https://youtube.com/watch?v=57JDI1S4rFA&t=3287s)** it as a SOX5 proxy. So it can be done, but you really have to draw the rest of the owl yourself,

**[54:57](https://youtube.com/watch?v=57JDI1S4rFA&t=3297s)** and it is not going to be super intuitive. Like part of what I love about tail scale is it just

**[55:05](https://youtube.com/watch?v=57JDI1S4rFA&t=3305s)** works. It's magic, sparkles, pixie dust, it's wonderful, but when you really want to get

**[55:12](https://youtube.com/watch?v=57JDI1S4rFA&t=3312s)** under the hood and make things work that, you know, maybe shouldn't, there are ways of doing it.

**[55:17](https://youtube.com/watch?v=57JDI1S4rFA&t=3317s)** So a second tail scale D running in user space networking mode as a SOX5 proxy tied to a browser to

**[55:26](https://youtube.com/watch?v=57JDI1S4rFA&t=3326s)** use that proxy, can work in that scenario. I don't recommend doing this on your employer's

**[55:33](https://youtube.com/watch?v=57JDI1S4rFA&t=3333s)** equipment. There may be consequences there, but if this is your machine and you're playing around,

**[55:41](https://youtube.com/watch?v=57JDI1S4rFA&t=3341s)** that would be the direction I would point you in. That sounds like the definition of home lab

**[55:47](https://youtube.com/watch?v=57JDI1S4rFA&t=3347s)** junk to me. Oh yeah, it looks very proxy running in. Yeah. All right. Now normally, we trail off

**[55:57](https://youtube.com/watch?v=57JDI1S4rFA&t=3357s)** a little bit and do a bit of a speed run at the end. I actually do have a customer call right

**[56:02](https://youtube.com/watch?v=57JDI1S4rFA&t=3362s)** at the bottom of the hour. So Alex, do you want to squeeze in a couple more of these before?

**[56:09](https://youtube.com/watch?v=57JDI1S4rFA&t=3369s)** All right, speed, speed round time. I use tail scale at home, but I have a Raspberry Pi at my

**[56:14](https://youtube.com/watch?v=57JDI1S4rFA&t=3374s)** daughter's house running ad guard and tail scale. I can log on from my house to my daughters,

**[56:19](https://youtube.com/watch?v=57JDI1S4rFA&t=3379s)** but how can I log on to the Raspberry Pi so that I can update it? I would run tail scale SSH

**[56:25](https://youtube.com/watch?v=57JDI1S4rFA&t=3385s)** directly on the Raspberry Pi and then SSH to the tail scale IP or magic DNS name and you'll

**[56:32](https://youtube.com/watch?v=57JDI1S4rFA&t=3392s)** be able to apt update over SSH. I would love to see Alex show how he would set up multiple ACLs

**[56:41](https://youtube.com/watch?v=57JDI1S4rFA&t=3401s)** for a home lab situation with multiple services and also some best practices for family and friends

**[56:48](https://youtube.com/watch?v=57JDI1S4rFA&t=3408s)** accessing a tail net would be awesome. So I assume you're going to talk about no sharing,

**[56:52](https://youtube.com/watch?v=57JDI1S4rFA&t=3412s)** that kind of thing in that question. Yeah, I'll add it to my backlog. No sharing is one of those

**[56:58](https://youtube.com/watch?v=57JDI1S4rFA&t=3418s)** videos we wanted to make for a long time. What I would say in the interim is my colleague Kevin

**[57:04](https://youtube.com/watch?v=57JDI1S4rFA&t=3424s)** wrote on the tail scale blog and I'll put a link in the chat shortly about interesting ways to

**[57:11](https://youtube.com/watch?v=57JDI1S4rFA&t=3431s)** use tail scale with friends and family. It's a really great post. I'd recommend it.

**[57:16](https://youtube.com/watch?v=57JDI1S4rFA&t=3436s)** Yeah. All right, last one. Are there any examples of reverse proxy using TSIDP or similar?

**[57:26](https://youtube.com/watch?v=57JDI1S4rFA&t=3446s)** I don't have any. We do have, now before TSIDP existed, there is an engine X auth proxy that has been

**[57:38](https://youtube.com/watch?v=57JDI1S4rFA&t=3458s)** around for years now, which will inject a tail scale identity into HTTP simple auth headers

**[57:48](https://youtube.com/watch?v=57JDI1S4rFA&t=3468s)** and it is a plugin for engine X. Based on the question, that might be a good fit.

**[57:56](https://youtube.com/watch?v=57JDI1S4rFA&t=3476s)** I have used that internally for some of my lab things to just log in as my tail scale identity.

**[58:03](https://youtube.com/watch?v=57JDI1S4rFA&t=3483s)** This is before TSIDP existed, so now I'm migrating my things over to TSIDP, but I haven't had to

**[58:11](https://youtube.com/watch?v=57JDI1S4rFA&t=3491s)** reverse proxy anything in that environment yet, so I haven't tested that out.

**[58:18](https://youtube.com/watch?v=57JDI1S4rFA&t=3498s)** Yeah, it would be a really nice feature, wouldn't it, to have some at least basic auth in front

**[58:22](https://youtube.com/watch?v=57JDI1S4rFA&t=3502s)** of apps that don't natively speak OAuth or OIDC? Yeah, it's a great idea. In the podcast episode

**[58:32](https://youtube.com/watch?v=57JDI1S4rFA&t=3512s)** that came out yesterday, Ross talking with David Carney, our co-founder and Remi Gretcho, who's on

**[58:36](https://youtube.com/watch?v=57JDI1S4rFA&t=3516s)** the Strategic Projects team about TSIDP. I've got their ear at the minute to talk about TSIDP,

**[58:43](https://youtube.com/watch?v=57JDI1S4rFA&t=3523s)** so don't worry, I'll feed that idea right back in, I'm sure I'm thinking of it already, but

**[58:49](https://youtube.com/watch?v=57JDI1S4rFA&t=3529s)** I'm going to squeeze one more in because it's quick. Is there a straightforward way to tunnel some

**[58:54](https://youtube.com/watch?v=57JDI1S4rFA&t=3534s)** IPs via my tail scale subnet router instead of creating app connectors? Yes, you can advertise public

**[59:00](https://youtube.com/watch?v=57JDI1S4rFA&t=3540s)** IPs on a subnet router. It doesn't have to be private IPs, so if the service you're trying to reach

**[59:07](https://youtube.com/watch?v=57JDI1S4rFA&t=3547s)** isn't behind a CDN or otherwise being tricky, just put its IP address in there and it will transparently

**[59:13](https://youtube.com/watch?v=57JDI1S4rFA&t=3553s)** wrote for you. There you go. I mean, if you think about it under the covers, that's really all

**[59:18](https://youtube.com/watch?v=57JDI1S4rFA&t=3558s)** on app connectors doing. Yeah, it just does it dynamically based on DNS responses.

**[59:24](https://youtube.com/watch?v=57JDI1S4rFA&t=3564s)** Absolutely. Well, I think that will probably do us for today, so I want to say a great big thank you

**[59:30](https://youtube.com/watch?v=57JDI1S4rFA&t=3570s)** to everybody that's watched throughout, or even just dipped in and out throughout the hour.

**[59:35](https://youtube.com/watch?v=57JDI1S4rFA&t=3575s)** We do these things regularly. I have a plug for a Discord event coming up fairly soon, so on October

**[59:42](https://youtube.com/watch?v=57JDI1S4rFA&t=3582s)** the 7th, I will be doing a live stream on Discord with Remi Gretcho from the Strategic Projects team,

**[59:48](https://youtube.com/watch?v=57JDI1S4rFA&t=3588s)** I mentioned earlier. He's directly involved in the development work happening on TSIDP right now,

**[59:53](https://youtube.com/watch?v=57JDI1S4rFA&t=3593s)** so if you want to know more about TSIDP, join us on October the 7th on our Discord at

**[59:59](https://youtube.com/watch?v=57JDI1S4rFA&t=3599s)** discord.gg slash tail scale. So I guess all's left for me to say, thank you so much for watching,

**[01:00:05](https://youtube.com/watch?v=57JDI1S4rFA&t=3605s)** and until next time, I've been Alex. No, I'm still Jay. Thanks Jay, have a good one. Bye.

---

*Automatically generated transcript. May contain errors.*
