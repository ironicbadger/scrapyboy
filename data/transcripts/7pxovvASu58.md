---
video_id: "7pxovvASu58"
title: "The future of tsidp and zero trust with zero clicks"
description: "Join Alex from Tailscale with David Carney and Remy Guercio as they dive into TSIDP, Tailscale’s identity provider. Learn how it simplifies authentication and powers secure, identity-first networking...."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-09-23"
duration_seconds: 1616
youtube_url: "https://www.youtube.com/watch?v=7pxovvASu58"
thumbnail_url: "https://i.ytimg.com/vi/7pxovvASu58/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:14:45.725039"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 5165
transcription_time_seconds: 49.2
---

# The future of tsidp and zero trust with zero clicks

**[00:01](https://youtube.com/watch?v=7pxovvASu58&t=1s)** Welcome into this special episode today. I'm joined by David Carney, who is one of the co-founders of Tailscale and our Chief Strategy Officer and Remi Gretzo from the Strategic Projects team. Today we're going to dive into our project. You may have heard about if you follow Tailscale closely, TSIDP. This is an identity server that we've been steadily pushing forward towards the 1.0 release over the last few months. Today we're going to talk about where TSIDP is headed, what role it plays in Tailscale's vision for becoming a platform in the future.

**[00:31](https://youtube.com/watch?v=7pxovvASu58&t=31s)** And how it helps lay the groundwork for an identity layer for the internet itself. So, with that lofty introduction out of the way, David, Remi, who wants to go first and sort of give us an overview of TSIDP and what it is and who it's for? I can start with a little bit of leading work, a little bit maybe about what Tailscale does, and then Remi, maybe you can take it from there. So, Tailscale is a relatively better term identity for networking. So, we make it easy to connect any issue device.

**[01:01](https://youtube.com/watch?v=7pxovvASu58&t=61s)** This is anywhere in the world, no matter where they are, with strong guarantees of identity and encryption. It's the identity piece, which is actually really fascinating to us right now, because a lot of people don't understand that identity is really baked into every single connection. Like every time there's a connection, you can verify who the other person or what the other device is on the other end. And TSIDP is a way that we can actually expose more of that applications connecting into, like within your tailnet and even on the outside of your tailnet.

**[01:31](https://youtube.com/watch?v=7pxovvASu58&t=91s)** And Remi, maybe you want to take it a little bit from here. Yeah, I was going to say, so I think at least the problem that we're trying to solve with TSIDP is, I don't know about you, but I hate logging into things. I hate having to always log into things. You know, SSO is kind of supposed to fix that. But even with SSO, you get hit with every out of no day week. However long your security team wants you to go without logging into something, you get hit again with logging in.

**[02:01](https://youtube.com/watch?v=7pxovvASu58&t=121s)** And the things, and it's even more fun when you have to do a 2FA prompt or something else on top of that. But yeah, TSIDP is really about fixing that so that we don't have to do that anywhere. You don't have to spend that time.

**[02:17](https://youtube.com/watch?v=7pxovvASu58&t=137s)** It's kind of in the name, right? Tailscale identity provider. I've definitely been late for meetings because I have to click on that stupid little face thing on my OAuth provider.

**[02:29](https://youtube.com/watch?v=7pxovvASu58&t=149s)** So TSIDP is going to help with that. Yes, yes. And I mean, I still know that I started on a Tuesday at Tailscale because we have a weekly re-auth. And Tuesday, always without a fail, I get hit with the logged out. You should log back in.

**[02:48](https://youtube.com/watch?v=7pxovvASu58&t=168s)** What is TSIDP exactly? I know it's something to do with OpenID Connect, but what is that? And where does TSIDP fit in that jigsaw?

**[02:57](https://youtube.com/watch?v=7pxovvASu58&t=177s)** Yeah, so, you know, like Karnie mentioned, you know, identity is baked into the Tailscale network. And what TSIDP really is, here is where it's a lightweight, open ID, OIDC, open ID and OAuth authorization server.

**[03:17](https://youtube.com/watch?v=7pxovvASu58&t=197s)** And what it does is it leverages that identity on your network that exists on the network. And you can run it inside of your private Tailscale network. And so, you know, when you go to, you know, you have a OAuth app on your network doesn't actually have to be on your network, but if you do, it's going to redirect you just kind of like normally like you would expect when you go to click on the button, it's going to redirect you to TSIDP conveniently TSIDP happens to know who you are as soon as you get redirected.

**[03:44](https://youtube.com/watch?v=7pxovvASu58&t=224s)** And it can verify that and send you right back. So it's this convenient little, you know, convenient little thing that's just on your network to make your life a little bit easier.

**[03:53](https://youtube.com/watch?v=7pxovvASu58&t=233s)** So how does it know who you are? Is that because I'm already authenticated through the Tailscale client on my phone or my laptop?

**[04:02](https://youtube.com/watch?v=7pxovvASu58&t=242s)** Yeah, yeah. So, you know, you you log into Tailscale, right, you're logging into the network. You're using your existing corporate IDP, you know, that you have set up set up to log into Tailscale. And so that's the like you part, right, you're logging into the network. And then on TSIDP side, it actually uses a fun thing that we have called TSNET, which is a little go library that can basically listen for and kind of

**[04:31](https://youtube.com/watch?v=7pxovvASu58&t=271s)** run effectively like a who is on incoming connections and get the identity from the network. So, you know, TSIDP is a go application, TSNET is a little go library and, you know, we get to, we get to use that there.

**[04:46](https://youtube.com/watch?v=7pxovvASu58&t=286s)** But, you know, people can also use TSNET themselves. It's not limited just to us.

**[04:51](https://youtube.com/watch?v=7pxovvASu58&t=291s)** So, the way I like to think about or explain TSIDP, it's like it's like almost running a small little mirror of your identity provider inside of your network.

**[05:01](https://youtube.com/watch?v=7pxovvASu58&t=301s)** So it's got all the same kind of capabilities or at least what you've granted to the child to begin with.

**[05:06](https://youtube.com/watch?v=7pxovvASu58&t=306s)** And because it's effectively a private instance, you can do a nice little thing. You can set up like little security rules and things that are related to it that you don't necessarily have to share with your like with your primary identity provider.

**[05:16](https://youtube.com/watch?v=7pxovvASu58&t=316s)** So, what kind of products in the marketplace is it most analogous to?

**[05:21](https://youtube.com/watch?v=7pxovvASu58&t=321s)** I don't wish to draw direct comparisons because I know it's still early days for TSIDP. We've got big plans for it.

**[05:27](https://youtube.com/watch?v=7pxovvASu58&t=327s)** I think people will probably think of it most akin to kind of like an authentic or kind of like one of the little self-hosted IDPs that you might run within your network.

**[05:40](https://youtube.com/watch?v=7pxovvASu58&t=340s)** And, however, I will say on TSIDP is kind of the difference there. Is it intended to be incredibly simple to set up and start using, right?

**[05:50](https://youtube.com/watch?v=7pxovvASu58&t=350s)** It's really just mirroring your existing, you know, Google, I try ID, Octa IDP inside of the network and then providing you with all the extra little tail skill, tail skill benefits on top of that.

**[06:04](https://youtube.com/watch?v=7pxovvASu58&t=364s)** It works a whole lot like one you might host yourself, but again, aims to be a lot more simple to actually use.

**[06:13](https://youtube.com/watch?v=7pxovvASu58&t=373s)** I think the unique thing here is that it leverages the identity that's already part of the tailnet.

**[06:19](https://youtube.com/watch?v=7pxovvASu58&t=379s)** So can you talk to me a little bit about how we did it?

**[06:22](https://youtube.com/watch?v=7pxovvASu58&t=382s)** How do we do it? Because identity is baked into every connection inside of tail scale.

**[06:26](https://youtube.com/watch?v=7pxovvASu58&t=386s)** It's in the headers, for instance.

**[06:31](https://youtube.com/watch?v=7pxovvASu58&t=391s)** And the strong guarantees about that that tail scale enforces little apps inside of the network, if they can connect to it, can read those headers and understand them.

**[06:40](https://youtube.com/watch?v=7pxovvASu58&t=400s)** And from that, it can infer who's connecting to one.

**[06:43](https://youtube.com/watch?v=7pxovvASu58&t=403s)** And TSnet is basically that like avert like a small little open source application that runs inside of your network that can do that.

**[06:51](https://youtube.com/watch?v=7pxovvASu58&t=411s)** It's essentially a full user space implementation of tail scale that from an external point of view just looks like another little node.

**[06:58](https://youtube.com/watch?v=7pxovvASu58&t=418s)** But what you can do is you can plug applications into TSnet.

**[07:02](https://youtube.com/watch?v=7pxovvASu58&t=422s)** And then those things immediately become services, just like a machine would like somebody authenticating a server or a laptop or an iPhone.

**[07:10](https://youtube.com/watch?v=7pxovvASu58&t=430s)** And so we've built TSIDP and it plugs into your tailnet with TSnet.

**[07:17](https://youtube.com/watch?v=7pxovvASu58&t=437s)** And then from that, TSIDP can effectively just act as, well, an identity provider because it can see the identity through the network.

**[07:28](https://youtube.com/watch?v=7pxovvASu58&t=448s)** And so it's really a combination of just technologies that are built on a lot of like all the complexity that we've hidden away with tail scale.

**[07:34](https://youtube.com/watch?v=7pxovvASu58&t=454s)** So it's very simple to both open source.

**[07:36](https://youtube.com/watch?v=7pxovvASu58&t=456s)** And yeah, in our community projects and people should check them out if they want to take into the details, but the source goes definitely quite rockable.

**[07:43](https://youtube.com/watch?v=7pxovvASu58&t=463s)** I put a link in the description down below, of course, to the community projects that David just referenced there.

**[07:49](https://youtube.com/watch?v=7pxovvASu58&t=469s)** But Remy, I know that you replaced your authentication flow for Grafana with TSIDP. How's that been?

**[07:58](https://youtube.com/watch?v=7pxovvASu58&t=478s)** It's pretty cool.

**[08:00](https://youtube.com/watch?v=7pxovvASu58&t=480s)** It's pretty cool. So yeah, I mean, again, run Grafana on my, you know, on my local network, right?

**[08:09](https://youtube.com/watch?v=7pxovvASu58&t=489s)** There's a kind of a, you know, fun way of visualizing some things.

**[08:12](https://youtube.com/watch?v=7pxovvASu58&t=492s)** As our home lab is 10 years.

**[08:14](https://youtube.com/watch?v=7pxovvASu58&t=494s)** Yes. Yes.

**[08:15](https://youtube.com/watch?v=7pxovvASu58&t=495s)** Fun way of visualizing some things around the house.

**[08:17](https://youtube.com/watch?v=7pxovvASu58&t=497s)** You know, I have a, you know, a air quality monitor that's, you know, kind of throws out a bunch of metrics that I love to grab.

**[08:27](https://youtube.com/watch?v=7pxovvASu58&t=507s)** I, Joe, you know what the pollen count was 17 days ago at 302 p.m.

**[08:31](https://youtube.com/watch?v=7pxovvASu58&t=511s)** Yes, I do. Yes, I do.

**[08:33](https://youtube.com/watch?v=7pxovvASu58&t=513s)** I also have a 3D printer that I run in my office. So I do like to kind of keep track of, you know, all the particulates that are, that are maybe in the air from that.

**[08:44](https://youtube.com/watch?v=7pxovvASu58&t=524s)** So, you know, yeah, it sits right there on top of it.

**[08:47](https://youtube.com/watch?v=7pxovvASu58&t=527s)** But yeah, you know, I, of course, I like to, you know, graph and, you know, and look at all of that.

**[08:52](https://youtube.com/watch?v=7pxovvASu58&t=532s)** But yeah, I mean, you know, typically logging in to Grafana, right? You know, use a name and password or, you know, you're going to set up SSO in front of it.

**[08:59](https://youtube.com/watch?v=7pxovvASu58&t=539s)** Grafana also, what Grafana happens to also do, which is quite cool is so, you know, you go set up TSI D.P. is a custom, you know, OIDC provider in, you know, in Grafana.

**[09:11](https://youtube.com/watch?v=7pxovvASu58&t=551s)** And they have a very convenient little feature that you can add or you can turn on.

**[09:16](https://youtube.com/watch?v=7pxovvASu58&t=556s)** And that is, it will automatically, if it's the only, you know, it's the only off provider configured, it will automatically bump you over to TSI D.P. to then authenticate and send you back.

**[09:27](https://youtube.com/watch?v=7pxovvASu58&t=567s)** So now when I go to Grafana, I don't even do anything. I just go to Grafana. It bumps me to TSI D.P. TSI D.P. is I'm good. And I get bumped all the way back. So it's completely zero click. I just, just log in to Grafana all of a sudden, which is, you know, quite nice in a home lab, especially where I'm just, I don't, I don't want to do any of that or remember any of that. And I, you know, I just want to be in Grafana.

**[09:50](https://youtube.com/watch?v=7pxovvASu58&t=590s)** Which gets me thinking about what some of the other use cases in the future might be.

**[09:55](https://youtube.com/watch?v=7pxovvASu58&t=595s)** I know that AI and MCP servers are a bit of a buzzword in 2025, but you two have been playing around with TSI D.P. and MCP servers. Haven't you?

**[10:06](https://youtube.com/watch?v=7pxovvASu58&t=606s)** A little bit. Our customers have been playing around with them a lot more than we have.

**[10:10](https://youtube.com/watch?v=7pxovvASu58&t=610s)** And yeah, the conventional pattern just with tail scales, like, I'm just going to put everything inside of the helmet.

**[10:15](https://youtube.com/watch?v=7pxovvASu58&t=615s)** And, you know, treat it as local and everything just works.

**[10:20](https://youtube.com/watch?v=7pxovvASu58&t=620s)** In practice, that's not really how MCP works. You've got usually some local clients. And then you've got a whole bunch of things that are remote. And sometimes you can pull some of these things into your network, but a lot of the times around the outside.

**[10:30](https://youtube.com/watch?v=7pxovvASu58&t=630s)** And that was actually one of the problems we sought to.

**[10:33](https://youtube.com/watch?v=7pxovvASu58&t=633s)** Well, I guess address with some recent extensions to TSI D.P. And maybe you can go into detail about that.

**[10:39](https://youtube.com/watch?v=7pxovvASu58&t=639s)** Yeah, I was going to say, so I mean, if anybody's not familiar necessarily with MCP, you know, MCP is a really it's just a way for like your LLM.

**[10:50](https://youtube.com/watch?v=7pxovvASu58&t=650s)** So like, if you're using cloud desktop or cloud code or, you know, chat GPT or things like that, you know, you want to give it access to something, right.

**[10:58](https://youtube.com/watch?v=7pxovvASu58&t=658s)** So like you can just have a conversation with it, of course, but right, you want to give it access to some data or documentation or, you know, things that you have.

**[11:05](https://youtube.com/watch?v=7pxovvASu58&t=665s)** And up until recently, basically June.

**[11:10](https://youtube.com/watch?v=7pxovvASu58&t=670s)** So, you know, you build an MCP server, you expose it and, you know, in the LLM, you know, the LLM can go call it and use it.

**[11:18](https://youtube.com/watch?v=7pxovvASu58&t=678s)** But up until very recently, basically, there was no authentication on top of this.

**[11:23](https://youtube.com/watch?v=7pxovvASu58&t=683s)** It was, you know, it was just kind of like you were kind of expected to use these MCP servers locally.

**[11:28](https://youtube.com/watch?v=7pxovvASu58&t=688s)** And, you know, like maybe use an API key, right. They were just running local and you were just kind of kind of, you know, you give an API key and it go make some calls.

**[11:37](https://youtube.com/watch?v=7pxovvASu58&t=697s)** You know, obviously there was a proliferation of like MCP tools that run not just locally on your laptop, but, you know, or wherever you happen to be running things, but over the network as well.

**[11:47](https://youtube.com/watch?v=7pxovvASu58&t=707s)** So, you know, sometimes they're public, right. You might have like the GitHub MCP.

**[11:52](https://youtube.com/watch?v=7pxovvASu58&t=712s)** Or, you know, but sometimes, you know, in a lot of cases, we, you know, we talk to folks, especially in the enterprise, you know, they don't want to run local MCP servers on everybody's, you know, computer across the thing, but they also don't want their MCP server to be public.

**[12:07](https://youtube.com/watch?v=7pxovvASu58&t=727s)** So, you know, and they need to kind of figure that out.

**[12:10](https://youtube.com/watch?v=7pxovvASu58&t=730s)** And so, recently into the spec, or recently into the MCP spec, the, you know, the MCP committee added, like a whole authorization standard.

**[12:21](https://youtube.com/watch?v=7pxovvASu58&t=741s)** And basically what they said was, oh, off works, you know, looks good. We can adopt the most recent stuff.

**[12:28](https://youtube.com/watch?v=7pxovvASu58&t=748s)** And they basically just said, hey, we'll take it all. Whether or not it's, you know, widely implemented or not, we'll just take it all. It's all, you know, this is useful.

**[12:36](https://youtube.com/watch?v=7pxovvASu58&t=756s)** And they said, you know, do that. And that's how you're going to need to build, you know, that's if you want to build, you know, authorized MCP servers in a spec compliant way, you're going to need to adopt quite a few things.

**[12:48](https://youtube.com/watch?v=7pxovvASu58&t=768s)** And yeah, and so, you know, what we realized is, you know, tons of identity providers don't necessarily support the things that the, the MCP committee, you know, said, hey, you should use dynamic client registration.

**[13:01](https://youtube.com/watch?v=7pxovvASu58&t=781s)** So basically a way for your, you know, MCP client to, you know, automatically register itself is kind of a prime example of something that's not very widely implemented.

**[13:11](https://youtube.com/watch?v=7pxovvASu58&t=791s)** Hey, we have TSIDP. It's a little identity provider. It runs and, you know, it sits in front of your existing identity provider. Maybe, you know, let's try extending it, let's try adding all of these things for, you know, the MCP spec.

**[13:23](https://youtube.com/watch?v=7pxovvASu58&t=803s)** And so, yeah, you know, we did, it works. You know, if you're running MCP servers, you know, inside your, you know, your tail scale network, you can, you know, and you want them to be authorized still, right?

**[13:35](https://youtube.com/watch?v=7pxovvASu58&t=815s)** You know, it's, you know, maybe a little bit bigger than your home lab, but, you know, it's not like a public publicly available MCP server, something you're trying to do for your, you know, you're at your company.

**[13:45](https://youtube.com/watch?v=7pxovvASu58&t=825s)** You can use TSIDP to do, you know, to support authorization for those without having to think really about, you know, what your, whether or not your identity provider supports, you know, X, Y or Z.

**[14:00](https://youtube.com/watch?v=7pxovvASu58&t=840s)** So, putting anything on the network without any formal authentication is just not going to be really accessible thing in, in, in secops.

**[14:09](https://youtube.com/watch?v=7pxovvASu58&t=849s)** So, my question back to you really is, what kinds of use cases are you seeing customers doing with MCP services? Is it stuff like creating chat bots for their internal documentation or, like, what kind of stuff are they doing?

**[14:22](https://youtube.com/watch?v=7pxovvASu58&t=862s)** I think if you kind of, like, go out and you listen to folks and you kind of, you know, you're on Reddit or Twitter or something like that, right?

**[14:28](https://youtube.com/watch?v=7pxovvASu58&t=868s)** And you're, you know, trying to, you know, you're kind of just, like, listening to the buzz.

**[14:33](https://youtube.com/watch?v=7pxovvASu58&t=873s)** You'll hear a lot about, like, you know, documentation, you know, like using, using MCP to, you know, grab documentation or, like, do, like, automated testing.

**[14:41](https://youtube.com/watch?v=7pxovvASu58&t=881s)** I think, you know, playwright's a big one that you kind of hear a lot about.

**[14:44](https://youtube.com/watch?v=7pxovvASu58&t=884s)** But I think in the, you know, enterprise and a lot of what we're, you know, kind of like what we hear folks is, you know, really they have some, like, custom data source.

**[14:54](https://youtube.com/watch?v=7pxovvASu58&t=894s)** You can basically say, write some custom set of, you know, there's like documents or like, you know, custom, you know, they just, they have data, right?

**[15:03](https://youtube.com/watch?v=7pxovvASu58&t=903s)** And they want to be able to expose it, you know, they want to be able to expose it to, you know, they want to be able to expose it as an MCP server.

**[15:10](https://youtube.com/watch?v=7pxovvASu58&t=910s)** And they're, you know, right now they're asking the question of like, how do we do that safely? And there's a, there's a lot that's really out there, right?

**[15:18](https://youtube.com/watch?v=7pxovvASu58&t=918s)** You know, that you need to do, to do this safely.

**[15:22](https://youtube.com/watch?v=7pxovvASu58&t=922s)** I think the power comes when you're trying to connect multiple data sources together. So, for example, you know, you want to, I don't know, book a trip or something.

**[15:31](https://youtube.com/watch?v=7pxovvASu58&t=931s)** You've got to take in flights and dates and a bunch of business logic about expense policies and this, that and the other, right?

**[15:38](https://youtube.com/watch?v=7pxovvASu58&t=938s)** And trying to synthesize all that data together without some glue to put it all together, which is what the MCP servers are doing.

**[15:45](https://youtube.com/watch?v=7pxovvASu58&t=945s)** I believe is going to be tricky.

**[15:48](https://youtube.com/watch?v=7pxovvASu58&t=948s)** So, yeah.

**[15:49](https://youtube.com/watch?v=7pxovvASu58&t=949s)** Even if your IDP doesn't support all those things, can we, can people still benefit from, from TSIDP and MCP somehow?

**[15:58](https://youtube.com/watch?v=7pxovvASu58&t=958s)** That's the whole, you know, kind of goal of TSIDP.

**[16:01](https://youtube.com/watch?v=7pxovvASu58&t=961s)** I hate to say Sham or, you know, but it's like, you know, it's basically, you know, it lets you do, kind of, let's you experiment with these, you know, authorized MCP servers and things like that.

**[16:10](https://youtube.com/watch?v=7pxovvASu58&t=970s)** Without, again, needing to kind of rethink what IDP you're using or kind of, you know, I know a lot of the kind of MCP server builders out there are trying to have to build.

**[16:22](https://youtube.com/watch?v=7pxovvASu58&t=982s)** Like these OAuth proxy OAuth shim kind of things to make it where, you know, like things support it, you know, you don't have to do that with TSIDP.

**[16:32](https://youtube.com/watch?v=7pxovvASu58&t=992s)** With TSIDP, we've already done it, right? You're going to get all the nice, you know, you get the nice form fuzzy blanket of, you know, tail skills, network access controls, you know, private network, you know, those sorts of things.

**[16:43](https://youtube.com/watch?v=7pxovvASu58&t=1003s)** And then you get the, you know, the identity bit on top of it, you know, that works for both your existing apps, right?

**[16:49](https://youtube.com/watch?v=7pxovvASu58&t=1009s)** You know, the graphanas and everything like that.

**[16:51](https://youtube.com/watch?v=7pxovvASu58&t=1011s)** And, you know, the new sort of MCP, you know, MCP stuff you're trying to experiment with.

**[16:56](https://youtube.com/watch?v=7pxovvASu58&t=1016s)** There's a few things I want to touch on in particular. So, like, what everything that's reminiscent is true, but I guess from, I guess from an enterprise point of view, right?

**[17:06](https://youtube.com/watch?v=7pxovvASu58&t=1026s)** There's a bunch of really interesting, I guess, characteristics that TSIDP introduces.

**[17:13](https://youtube.com/watch?v=7pxovvASu58&t=1033s)** And so, yes, a lot of existing identity providers aren't what I would call MCP spec compliant in terms of what they offer.

**[17:19](https://youtube.com/watch?v=7pxovvASu58&t=1039s)** I don't like to mention that a lot of them don't support dynamic client registration, right?

**[17:24](https://youtube.com/watch?v=7pxovvASu58&t=1044s)** Because we're effectively a mirror of your existing identity provider, we can build those things in and we've done that.

**[17:29](https://youtube.com/watch?v=7pxovvASu58&t=1049s)** So, we basically provided the way to like level up existing identity providers to make them more MCP compliant.

**[17:35](https://youtube.com/watch?v=7pxovvASu58&t=1055s)** So, people can use those for MCP kinds of workloads to bring them up to the, but the spec requires.

**[17:40](https://youtube.com/watch?v=7pxovvASu58&t=1060s)** Secondly, all this obviously works inside of a tailnet.

**[17:44](https://youtube.com/watch?v=7pxovvASu58&t=1064s)** It also works with MCP servers outside of your tailnet.

**[17:48](https://youtube.com/watch?v=7pxovvASu58&t=1068s)** Which, yeah, which, yeah.

**[17:51](https://youtube.com/watch?v=7pxovvASu58&t=1071s)** So, this is part of the magic.

**[17:54](https://youtube.com/watch?v=7pxovvASu58&t=1074s)** There's another great feature called tailscale funnel, which lets you take an example, like an internal service and expose it publicly.

**[18:00](https://youtube.com/watch?v=7pxovvASu58&t=1080s)** And you can use funnel in combination TSIDP to basically put this service, the service running on an externally accessible or address.

**[18:12](https://youtube.com/watch?v=7pxovvASu58&t=1092s)** So, that external services, such as like Salesforce, for instance, or an MCP server or something else can add.

**[18:19](https://youtube.com/watch?v=7pxovvASu58&t=1099s)** So, we can extend the OAuth flow outside of the network to those particular services that are having requests sent to them from inside.

**[18:26](https://youtube.com/watch?v=7pxovvASu58&t=1106s)** Without those services needing to modify a single thing other than their callback endpoint.

**[18:31](https://youtube.com/watch?v=7pxovvASu58&t=1111s)** Right.

**[18:32](https://youtube.com/watch?v=7pxovvASu58&t=1112s)** So, if they use OAuth, we basically extend the OAuth boundary to things outside of the network.

**[18:38](https://youtube.com/watch?v=7pxovvASu58&t=1118s)** So, this is basically a way that, you know, you've got your nice secure tailnet.

**[18:43](https://youtube.com/watch?v=7pxovvASu58&t=1123s)** You've got your ACLs, you've got everything else inside of it.

**[18:46](https://youtube.com/watch?v=7pxovvASu58&t=1126s)** You've got your strong notion of identity.

**[18:48](https://youtube.com/watch?v=7pxovvASu58&t=1128s)** And you can go to like MCP registries and start using those things as long as they use OAuth.

**[18:52](https://youtube.com/watch?v=7pxovvASu58&t=1132s)** Right.

**[18:53](https://youtube.com/watch?v=7pxovvASu58&t=1133s)** Which the MCP spec requires and just people are starting to build this kind of stuff now.

**[18:57](https://youtube.com/watch?v=7pxovvASu58&t=1137s)** So, I think that's incredible.

**[18:59](https://youtube.com/watch?v=7pxovvASu58&t=1139s)** And then, I guess the third thing is in RemiTouch on this too.

**[19:04](https://youtube.com/watch?v=7pxovvASu58&t=1144s)** A lot from an enterprise use case, you don't want a lot of, let me think, direct, maybe not direct connections.

**[19:09](https://youtube.com/watch?v=7pxovvASu58&t=1149s)** So, you don't want a lot of connections between clients and servers, standard security patterns,

**[19:14](https://youtube.com/watch?v=7pxovvASu58&t=1154s)** you'll build some kind of proxy or a gateway.

**[19:16](https://youtube.com/watch?v=7pxovvASu58&t=1156s)** Because you'll run them through that because you want to be able to, like, auto everything and control everything.

**[19:20](https://youtube.com/watch?v=7pxovvASu58&t=1160s)** You want tons of logs.

**[19:21](https://youtube.com/watch?v=7pxovvASu58&t=1161s)** You want to be able to cut off access if you need to.

**[19:23](https://youtube.com/watch?v=7pxovvASu58&t=1163s)** And a big problem with running things through a gateway is there's this handoff.

**[19:28](https://youtube.com/watch?v=7pxovvASu58&t=1168s)** And so that, you know, somebody on the other side of a gateway would say, like, oh, the gateway is making this request.

**[19:33](https://youtube.com/watch?v=7pxovvASu58&t=1173s)** But who on the other, like, who's actually making the original request?

**[19:36](https://youtube.com/watch?v=7pxovvASu58&t=1176s)** And so we've improved the side of the piece so that, say, the MCP server that is receiving the request from a gateway can actually tell who it's from directly.

**[19:46](https://youtube.com/watch?v=7pxovvASu58&t=1186s)** So there's a way to basically do, like, it's called the token exchange.

**[19:49](https://youtube.com/watch?v=7pxovvASu58&t=1189s)** And so we support that as well.

**[19:51](https://youtube.com/watch?v=7pxovvASu58&t=1191s)** So things like identity delegation works if you're running an MCP proxy or gateway inside of tail scale as well.

**[19:58](https://youtube.com/watch?v=7pxovvASu58&t=1198s)** And the last single ad.

**[20:00](https://youtube.com/watch?v=7pxovvASu58&t=1200s)** And this is a lot of things is that this isn't just for MCP.

**[20:03](https://youtube.com/watch?v=7pxovvASu58&t=1203s)** It's basically anything that works with the law, right?

**[20:06](https://youtube.com/watch?v=7pxovvASu58&t=1206s)** So MCP is really important and very hot topic.

**[20:08](https://youtube.com/watch?v=7pxovvASu58&t=1208s)** But we're building with just for identity in general.

**[20:11](https://youtube.com/watch?v=7pxovvASu58&t=1211s)** And so you can, you know, there's other protocols or systems out there where people are trying to do these kinds of things or plug identity,

**[20:18](https://youtube.com/watch?v=7pxovvASu58&t=1218s)** where services into their networks.

**[20:20](https://youtube.com/watch?v=7pxovvASu58&t=1220s)** And that's really what this technology is all about.

**[20:23](https://youtube.com/watch?v=7pxovvASu58&t=1223s)** So my logical question follow up with my security hat on is if this service is running on my town and we are making things easy to connect to as a security guy.

**[20:36](https://youtube.com/watch?v=7pxovvASu58&t=1236s)** I don't like that.

**[20:37](https://youtube.com/watch?v=7pxovvASu58&t=1237s)** I like to be able to lock things down.

**[20:38](https://youtube.com/watch?v=7pxovvASu58&t=1238s)** I like to be able to create rule sets that says, you know, accounts can't access production except.

**[20:45](https://youtube.com/watch?v=7pxovvASu58&t=1245s)** Well, I don't know if I ever want accounts accessing production.

**[20:47](https://youtube.com/watch?v=7pxovvASu58&t=1247s)** But you know what I mean?

**[20:48](https://youtube.com/watch?v=7pxovvASu58&t=1248s)** Like, can we leverage some of the features built right into tail scale like ACLs and grants and that kind of thing to control access to?

**[20:56](https://youtube.com/watch?v=7pxovvASu58&t=1256s)** Is that possible?

**[20:58](https://youtube.com/watch?v=7pxovvASu58&t=1258s)** The short answer is yes.

**[21:00](https://youtube.com/watch?v=7pxovvASu58&t=1260s)** And so there's a high level of ACLs, which we already had inside of tail scale, which dictate who is allowed to connect to what.

**[21:08](https://youtube.com/watch?v=7pxovvASu58&t=1268s)** And so you know that if, you know, somebody's something is initiator successfully connected to you, you already have a guarantee that, oh, the ACLs let this happen.

**[21:16](https://youtube.com/watch?v=7pxovvASu58&t=1276s)** Right. But then on top of that, we can, you can add it and meta information so that say an MCB server can look at the headers and inspect it.

**[21:24](https://youtube.com/watch?v=7pxovvASu58&t=1284s)** And it's like, well, I already know who's on the other side.

**[21:27](https://youtube.com/watch?v=7pxovvASu58&t=1287s)** You know, but I can look at, I can, I can look for this additional information.

**[21:30](https://youtube.com/watch?v=7pxovvASu58&t=1290s)** That also comes with requests to make decisions, maybe like role-based decisions about what I'm supposed to do.

**[21:36](https://youtube.com/watch?v=7pxovvASu58&t=1296s)** Right.

**[21:37](https://youtube.com/watch?v=7pxovvASu58&t=1297s)** Remi can maybe go into a little bit more detail about it.

**[21:39](https://youtube.com/watch?v=7pxovvASu58&t=1299s)** Yeah, I don't know if you guys knew, but I don't know if you could feel me getting excited.

**[21:46](https://youtube.com/watch?v=7pxovvASu58&t=1306s)** So yeah, what's really cool here is yes, we can leverage like all of the existing things about tail scale.

**[21:56](https://youtube.com/watch?v=7pxovvASu58&t=1316s)** You know, when you're using TS IDP as well.

**[21:58](https://youtube.com/watch?v=7pxovvASu58&t=1318s)** So my touch on this just a little bit at the very beginning.

**[22:02](https://youtube.com/watch?v=7pxovvASu58&t=1322s)** And one of the big things is we have device posture rules in tail scale.

**[22:08](https://youtube.com/watch?v=7pxovvASu58&t=1328s)** Right. So, you know, think of that.

**[22:11](https://youtube.com/watch?v=7pxovvASu58&t=1331s)** Yeah.

**[22:12](https://youtube.com/watch?v=7pxovvASu58&t=1332s)** So right, you know, you don't want somebody to log in to something unless they, you know, let's say you've got TS IDP in front of some sensitive things.

**[22:23](https://youtube.com/watch?v=7pxovvASu58&t=1343s)** Right. You already know people to log in if they're on iOS 26 or something.

**[22:26](https://youtube.com/watch?v=7pxovvASu58&t=1346s)** Yep.

**[22:27](https://youtube.com/watch?v=7pxovvASu58&t=1347s)** Yep. You know, you don't want them to, you know, hey, I want you to be on a corporate managed device to be able to use, you know,

**[22:34](https://youtube.com/watch?v=7pxovvASu58&t=1354s)** with liquid glass only.

**[22:36](https://youtube.com/watch?v=7pxovvASu58&t=1356s)** Yes, liquid glass only.

**[22:37](https://youtube.com/watch?v=7pxovvASu58&t=1357s)** Yes, it has to be the newest and latest.

**[22:39](https://youtube.com/watch?v=7pxovvASu58&t=1359s)** I mean, we do, we do support OS version.

**[22:41](https://youtube.com/watch?v=7pxovvASu58&t=1361s)** You can, you know, you can specify that, you know, crowd strike Falcon score.

**[22:47](https://youtube.com/watch?v=7pxovvASu58&t=1367s)** You know, you can, you can put that in front of somebody being able to, you know, actually hit TS IDP to be able to authenticate into anything.

**[22:55](https://youtube.com/watch?v=7pxovvASu58&t=1375s)** So, and there's one other thing is, you know, we, we, you know, I know Alex you've talked about this before on the channel.

**[23:03](https://youtube.com/watch?v=7pxovvASu58&t=1383s)** But just in time access is another pattern that you can actually put in front of TS IDP if you, if you want to.

**[23:10](https://youtube.com/watch?v=7pxovvASu58&t=1390s)** So very flexible are, you know, the access control rules with tail scale are incredibly, incredibly flexible, very powerful.

**[23:19](https://youtube.com/watch?v=7pxovvASu58&t=1399s)** And you get to, you get to use them with TS IDP.

**[23:22](https://youtube.com/watch?v=7pxovvASu58&t=1402s)** So it's very, it's very fun.

**[23:24](https://youtube.com/watch?v=7pxovvASu58&t=1404s)** Well, you just broke TS IDP out into its own GitHub repo.

**[23:29](https://youtube.com/watch?v=7pxovvASu58&t=1409s)** Part of the tail scale, like main repository, it's now its own standalone thing.

**[23:34](https://youtube.com/watch?v=7pxovvASu58&t=1414s)** So are we, are we letting people loose on this thing?

**[23:38](https://youtube.com/watch?v=7pxovvASu58&t=1418s)** Is it ready to go?

**[23:39](https://youtube.com/watch?v=7pxovvASu58&t=1419s)** Can they, can they get started?

**[23:40](https://youtube.com/watch?v=7pxovvASu58&t=1420s)** Yeah.

**[23:41](https://youtube.com/watch?v=7pxovvASu58&t=1421s)** So today, I mean, you can get started today.

**[23:43](https://youtube.com/watch?v=7pxovvASu58&t=1423s)** It's, you know, on our GitHub, tail scale slash TS IDP.

**[23:47](https://youtube.com/watch?v=7pxovvASu58&t=1427s)** Like you mentioned, it's on repo now.

**[23:50](https://youtube.com/watch?v=7pxovvASu58&t=1430s)** We did that really, you know, we wanted to help improve the visibility of TS IDP, right?

**[23:54](https://youtube.com/watch?v=7pxovvASu58&t=1434s)** We want people to try it out and want people using it.

**[23:57](https://youtube.com/watch?v=7pxovvASu58&t=1437s)** We want, we want your feedback.

**[23:59](https://youtube.com/watch?v=7pxovvASu58&t=1439s)** You know, would absolutely love folks feedback.

**[24:02](https://youtube.com/watch?v=7pxovvASu58&t=1442s)** You know, that's, that's really what we're, that's really what we're looking for.

**[24:05](https://youtube.com/watch?v=7pxovvASu58&t=1445s)** And, you know, what's the right mechanism for that feedback?

**[24:08](https://youtube.com/watch?v=7pxovvASu58&t=1448s)** Is it a hub issue?

**[24:09](https://youtube.com/watch?v=7pxovvASu58&t=1449s)** Yeah.

**[24:10](https://youtube.com/watch?v=7pxovvASu58&t=1450s)** Yeah.

**[24:11](https://youtube.com/watch?v=7pxovvASu58&t=1451s)** So just follow GitHub issue.

**[24:12](https://youtube.com/watch?v=7pxovvASu58&t=1452s)** You can join us on Discord.

**[24:13](https://youtube.com/watch?v=7pxovvASu58&t=1453s)** We recently launched a, you know, tail scale.

**[24:15](https://youtube.com/watch?v=7pxovvASu58&t=1455s)** We have a Discord.gg slash tail scale, by the way.

**[24:18](https://youtube.com/watch?v=7pxovvASu58&t=1458s)** There we go.

**[24:19](https://youtube.com/watch?v=7pxovvASu58&t=1459s)** There we go.

**[24:20](https://youtube.com/watch?v=7pxovvASu58&t=1460s)** And so, you know, you can, you know, you can go there.

**[24:22](https://youtube.com/watch?v=7pxovvASu58&t=1462s)** We have a TS IDP channel in, in Discord.

**[24:25](https://youtube.com/watch?v=7pxovvASu58&t=1465s)** You know, please come, you know, come join, come, come let us know what you think.

**[24:29](https://youtube.com/watch?v=7pxovvASu58&t=1469s)** And, and yeah, so, you know, we're just, again, we're hoping for feedback.

**[24:34](https://youtube.com/watch?v=7pxovvASu58&t=1474s)** You know, especially even, you know, there's the kind of the home lab app situation.

**[24:37](https://youtube.com/watch?v=7pxovvASu58&t=1477s)** There's the, you know, corporate app situation.

**[24:40](https://youtube.com/watch?v=7pxovvASu58&t=1480s)** That's a little more like, you know, we want your feedback and stuff.

**[24:43](https://youtube.com/watch?v=7pxovvASu58&t=1483s)** It's a little more, you know, it's been around for a while.

**[24:46](https://youtube.com/watch?v=7pxovvASu58&t=1486s)** You know, I've been using it to log into my proxmox for the last nine months.

**[24:50](https://youtube.com/watch?v=7pxovvASu58&t=1490s)** And it's been working great.

**[24:51](https://youtube.com/watch?v=7pxovvASu58&t=1491s)** So, yeah.

**[24:52](https://youtube.com/watch?v=7pxovvASu58&t=1492s)** So, you know, that, that's been around for a while, right?

**[24:55](https://youtube.com/watch?v=7pxovvASu58&t=1495s)** And, but on the MCP side, all right, that, that ought spec, you know, came out in June.

**[25:02](https://youtube.com/watch?v=7pxovvASu58&t=1502s)** It's moving fast.

**[25:03](https://youtube.com/watch?v=7pxovvASu58&t=1503s)** If you're in the MCP space at all, you know, you realize just how fast everything's moving.

**[25:10](https://youtube.com/watch?v=7pxovvASu58&t=1510s)** So, you know, we're actively developing this.

**[25:13](https://youtube.com/watch?v=7pxovvASu58&t=1513s)** We're, you know, soliciting feedback on, you know, all of the new things that are out there.

**[25:17](https://youtube.com/watch?v=7pxovvASu58&t=1517s)** You know, if you're building an MCP server, if you're building an MCP gateway,

**[25:21](https://youtube.com/watch?v=7pxovvASu58&t=1521s)** you know, we would love to talk with you.

**[25:23](https://youtube.com/watch?v=7pxovvASu58&t=1523s)** You know, we would love to make your life easier.

**[25:26](https://youtube.com/watch?v=7pxovvASu58&t=1526s)** Yeah.

**[25:27](https://youtube.com/watch?v=7pxovvASu58&t=1527s)** Reach out via the discord or get a bushel and I'll put you in touch with Remi or Kani over there.

**[25:32](https://youtube.com/watch?v=7pxovvASu58&t=1532s)** Please.

**[25:33](https://youtube.com/watch?v=7pxovvASu58&t=1533s)** So, before we wrap anything, anywhere else you'd like to send people to look at stuff?

**[25:38](https://youtube.com/watch?v=7pxovvASu58&t=1538s)** I was going to say if you want to build something cool like this yourself, you know,

**[25:44](https://youtube.com/watch?v=7pxovvASu58&t=1544s)** we don't want to have all the fun.

**[25:46](https://youtube.com/watch?v=7pxovvASu58&t=1546s)** But, you know, I would also encourage you and you like to write go,

**[25:50](https://youtube.com/watch?v=7pxovvASu58&t=1550s)** or you know, you maybe like to have cloud code or somebody write some go for you.

**[25:53](https://youtube.com/watch?v=7pxovvASu58&t=1553s)** If you want to do that, I really encourage you to check out TSNet.

**[25:56](https://youtube.com/watch?v=7pxovvASu58&t=1556s)** It is like we mentioned, it is the kind of the core of what we use to build TSIDP.

**[26:02](https://youtube.com/watch?v=7pxovvASu58&t=1562s)** It gives you that identity bit and lets you, you know, out anything built with TSNet.

**[26:06](https://youtube.com/watch?v=7pxovvASu58&t=1566s)** You can basically have, you know, it shows up on your tail scale network.

**[26:09](https://youtube.com/watch?v=7pxovvASu58&t=1569s)** Please, you know, check that out, try building something, you know, that runs on tail scale.

**[26:13](https://youtube.com/watch?v=7pxovvASu58&t=1573s)** Well, thank you both so much for joining me today.

**[26:16](https://youtube.com/watch?v=7pxovvASu58&t=1576s)** By the way, all of this is available for free on every single tail scale pricing tier

**[26:21](https://youtube.com/watch?v=7pxovvASu58&t=1581s)** that we have right away from our free plan, our personal plan, all the way up to enterprise plan.

**[26:25](https://youtube.com/watch?v=7pxovvASu58&t=1585s)** So, there's no gatekeeping or anything like that there.

**[26:28](https://youtube.com/watch?v=7pxovvASu58&t=1588s)** And you can get started today by heading over to tailscale.com, sign up for a free account,

**[26:32](https://youtube.com/watch?v=7pxovvASu58&t=1592s)** 100 devices, and three users, completely for free.

**[26:35](https://youtube.com/watch?v=7pxovvASu58&t=1595s)** I don't think you'll find a more generous free tier than that in the segment.

**[26:40](https://youtube.com/watch?v=7pxovvASu58&t=1600s)** So, thank you both for joining me today.

**[26:42](https://youtube.com/watch?v=7pxovvASu58&t=1602s)** And until next time, I've been Alex from tail scale.

**[26:45](https://youtube.com/watch?v=7pxovvASu58&t=1605s)** Thank you.

**[26:46](https://youtube.com/watch?v=7pxovvASu58&t=1606s)** Thank you, Alex.

**[26:47](https://youtube.com/watch?v=7pxovvASu58&t=1607s)** All right, thank you.

---

*Automatically generated transcript. May contain errors.*
