---
video_id: "Jn8_Sh4r8d4"
title: "ACLs 101 - An Introduction to Access Control Lists | Tailscale Explained"
description: "In our \"Tailscale Explained\" series we show you all you need to know to get started on a particular area or feature of Tailscale.

In today's video we cover Tailscale ACLs. We'll discuss ACL tags, ACL..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-09-25"
duration_seconds: 1081
youtube_url: "https://www.youtube.com/watch?v=Jn8_Sh4r8d4"
thumbnail_url: "https://i.ytimg.com/vi_webp/Jn8_Sh4r8d4/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T17:51:09.515379"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 3374
transcription_time_seconds: 28.3
---

# ACLs 101 - An Introduction to Access Control Lists | Tailscale Explained

**[00:00](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=0s)** Welcome into another episode of Tailscale Explained, I'm Alex. In this series, we cover everything

**[00:05](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=5s)** you ever wanted to know about Tailscale, things like subnet routers, or Tailscale SSH. And today,

**[00:11](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=11s)** we're going to cover ACLs. You can find a link to the Tailscale Explained playlist in the

**[00:16](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=16s)** description down below. Now you can think of ACLs or access controlists as a series of rules or

**[00:22](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=22s)** permissions that govern how and where data can flow within your tailnet. If you ever worked with

**[00:28](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=28s)** a firewall rule in the past, you'll feel pretty comfortable with the concept right away.

**[00:33](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=33s)** By default, your tailnet ships with a permissive allow all rule, which allows every node to talk

**[00:38](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=38s)** to every other node within your tailnet. That's because architecturally, a tailnet is designed

**[00:43](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=43s)** around the concept of least privilege. In other words, unless you explicitly allow something to

**[00:48](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=48s)** happen, it can't. One of the most common questions we hear is, how does Tailscale's mesh

**[00:55](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=55s)** architecture differ from a traditional VPN using a hub and spoke model? Well, ACLs are a culmination

**[01:02](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=62s)** of one of those mesh architecture benefits. By connecting each node directly to your tailnet,

**[01:08](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=68s)** you gain fine-grained control over the connectivity between those nodes and a whole host of other

**[01:13](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=73s)** benefits like end-to-end encryption as well. And this is all done without relying on a potentially

**[01:19](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=79s)** bottlenecked centralized VPN server too. Nearly every connection with Tailscale is a direct

**[01:25](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=85s)** device to device connection. ACLs can govern anything from SSH connections to controlling traffic

**[01:31](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=91s)** based on source device, destination device, protocol, port number and a whole bunch more stuff.

**[01:37](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=97s)** There'll be a link to the documentation for ACLs down below where the full feature set is

**[01:42](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=102s)** discussed for you. In today's video though, I'm going to show you how to write your first ACL rule

**[01:47](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=107s)** with a feature that not many people know exists. Tests built right into your ACL rule set.

**[01:53](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=113s)** By writing a test, we can ensure that your ACLs are doing exactly what you expect them to do

**[01:58](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=118s)** at all times. So, let's jump into writing your first rule. You can find your ACLs under the

**[02:06](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=126s)** access controls option in your Tailscale admin console. Now, this is a demo tailnet that I have here

**[02:12](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=132s)** and you can see I've got a bunch of preconfigured ACL rules in here already. Now, a quick tip before

**[02:17](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=137s)** we get started, if you want to go back to factory defaults and get back to our default policy file,

**[02:24](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=144s)** simply clear out the entire contents of this text box and click on this reset to default policy

**[02:30](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=150s)** button down here at the bottom. If it turns out that that was a mistake for you and you think to

**[02:36](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=156s)** yourself, hmm, I wish I hadn't made that change for whatever reason. You can go up to the logs

**[02:42](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=162s)** option here again in the Tailscale admin console and look at the audit log for the various changes

**[02:47](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=167s)** that were made to the configuration of your tailnet. You can see that in these configuration logs,

**[02:52](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=172s)** I have an option here to look at the changes that were made, a bit like a git diff between the left

**[02:56](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=176s)** and the right side a few moments ago. So now, if I want to revert my changes and go back to my previous

**[03:02](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=182s)** version, I simply scroll down to the revert to previous version button, click on revert and then if

**[03:07](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=187s)** I go back to my access controls page, you can see that my ACLs file is now back as it was a few

**[03:12](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=192s)** moments ago. Now, just so that we're all starting from the same place, I'm going to reset my policy

**[03:16](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=196s)** file back to scratch again, back to factory, the default policy. And you'll notice that there are

**[03:22](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=202s)** a few things going on in this file. Firstly, I want to talk you through the fact that this is

**[03:26](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=206s)** something called Hugh Jason, human readable Jason. And this editor has a bunch of syntax checking

**[03:33](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=213s)** built in for you. So if we forget, for example, to close a bracket, I'm just going to comment this

**[03:38](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=218s)** out with a pair of forward slashes. If we make a mistake, this editor will kind of sanity check a

**[03:43](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=223s)** lot of stuff for us. This is how all the test validation stuff works later too, which we'll get

**[03:48](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=228s)** on to. Don't worry about that. So you can just go through and make edits in here and it's a fairly

**[03:54](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=234s)** intelligent editor, even though it looks like it's just a text box. It's got some smarts behind it.

**[03:59](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=239s)** So the first rule I want to draw your attention to, the first block, I suppose, is this ACLs block here?

**[04:06](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=246s)** This is that permissive allow all rule that I mentioned in the intro. This is the rule that

**[04:11](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=251s)** allows us to connect any device to any device. And indeed, we can verify that with a very simple

**[04:17](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=257s)** SSH script. So if I show you this script I have here, which is super basic, to be honest,

**[04:23](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=263s)** but it does a connect timeout every second and tries to SSH into one of my tailnet nodes called

**[04:29](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=269s)** fake NERS. So if I just leave this running in the background, you'll see that right now I'm connected

**[04:35](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=275s)** to that node. If I just pop this up here in the corner, we'll leave that running up there.

**[04:40](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=280s)** Now, as soon as I make a change to my rule set, I want you to watch in real time what happens,

**[04:44](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=284s)** really, I'm going to click save. And within a split second, you can see that the SSH

**[04:49](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=289s)** connections have stopped working. That's because in real time, these changes get pushed down to

**[04:55](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=295s)** each device. Each tailnet policy file gets sent to the local device. These rule sets are enforced

**[05:03](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=303s)** locally. They're not enforced by the centralized server. So they're very performant. I want to just

**[05:07](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=307s)** show you the fact that it works in real time in the other way as well. If I reenable that rule,

**[05:12](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=312s)** you'll see that soon as the tailnet policy file gets saved, the SSH connections are reestablished

**[05:18](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=318s)** almost right away. So having such a wide open permissive rule can potentially be a little bit of a

**[05:25](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=325s)** security risk, right? We don't necessarily want our developers to be able to SSH into production.

**[05:31](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=331s)** So I can't imagine why you might want to not allow your developers to SSH into production.

**[05:36](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=336s)** Hmm, but anyway, it's sometimes that is the world that we live in. So how can we go about writing a

**[05:41](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=341s)** rule that would let, for example, only my laptop here connect to that other host over SSH?

**[05:48](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=348s)** It's actually quite straightforward. All we do, I'm just going to copy and pay something here

**[05:52](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=352s)** in from my notes. If we write a rule that says the action here is to accept a connection or

**[06:00](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=360s)** allow traffic, in other words, from a source called Magrithia, which actually should be

**[06:06](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=366s)** MVP Baldric, I think in this case. And this is going to fail, don't worry. This is all part of

**[06:11](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=371s)** the part of the act. With the destination in this case of fake NAS with a wild card for the port

**[06:18](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=378s)** number on the protocol of TCP, you can change this to be UDP. There's a bunch of other stuff too.

**[06:23](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=383s)** So if we look in the syntax reference here in the documentation, you can see that the protocol

**[06:28](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=388s)** option supports any IANA protocol number from one through to 255. So jumping back to our ACLs

**[06:36](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=396s)** file, I'm just going to leave this as TCP, because that's the protocol SSH transits over. It's a

**[06:42](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=402s)** TCP protocol. I'm going to disable this, allow all rule. So we've already seen that as soon as I do

**[06:49](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=409s)** that, all of the SSH connections are actually going to stop for us. So if I click save, we can see

**[06:55](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=415s)** that we've got a problem immediately. The source MVP Baldric is an invalid address. Now that

**[07:01](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=421s)** first, that might seem a little weird, because if we look at my tailnet configuration up here,

**[07:06](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=426s)** this device MVP Baldric, well, it exists. And this is a deliberate choice that we've made,

**[07:12](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=432s)** architecturally speaking, because we don't want to allow people to change their node names. I mean,

**[07:17](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=437s)** typically in these ACL files, you can refer to nodes by their host names. Whereas in this specific

**[07:24](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=444s)** case, you actually have to define explicitly the hosts that are listed. So I'm going to copy in

**[07:30](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=450s)** another small piece of code just here for us. And you can see that I've got a list of hosts,

**[07:36](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=456s)** but I don't have MVP Baldric. So let's go ahead and add that. So MVP Baldric. And then I need to get my

**[07:42](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=462s)** IP address, the number here, the 100. I can go in macOS client anyway. I can go up to the menu bar,

**[07:48](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=468s)** click on this device option, and then just put this into my ACLs file over here. And now what we've

**[07:54](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=474s)** got is essentially we've set a hosts variable. And this is done deliberately so that people can't

**[07:59](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=479s)** rename their nodes and gain permission to resources simply by virtue of their their node name matching

**[08:06](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=486s)** something in the ACL rule set that it shouldn't. So you have to explicitly allow MVP Baldric

**[08:12](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=492s)** to be referred to as MVP Baldric throughout the file. And so we can see that that now is working

**[08:18](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=498s)** just fine. The SSH connection remains intact. I'm still making my connection every second over here.

**[08:23](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=503s)** But let's say I wanted to just change this port number from a wild card, which allows every TCP

**[08:28](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=508s)** port to only allowing a TLS port on port 443. If I click save, we'll see that immediately the

**[08:35](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=515s)** SSH connection on port 22 starts complaining. That's exactly what we would expect. So again,

**[08:41](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=521s)** if I change this to 22, we'll see that again in real time, the SSH connection comes back again.

**[08:48](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=528s)** And so that's the general principle behind writing your first ACL rule. We have an action,

**[08:53](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=533s)** which in this case is accept deny by the way is not a valid option to put into this block.

**[08:59](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=539s)** And that's because remember tail scale works on the least privileged model. So everything by implicit

**[09:04](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=544s)** design is deny. So the only permissible value in action is accept. Source will actually be fairly

**[09:10](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=550s)** self explanatory. That's the source. The origin of where the traffic is coming from destination is

**[09:15](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=555s)** where the traffic is going to. So in our case, fake NARS and then port 22, although we had a wild

**[09:21](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=561s)** card at the beginning, then the protocol is TCP, as I mentioned. So let's just presuppose we've

**[09:27](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=567s)** spent several hours working on making our town at policy file perfect or we want to make sure

**[09:33](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=573s)** that we're writing the correct rules that do the right things for us. We're going to need to

**[09:37](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=577s)** start looking at tests, which I mentioned again in the intro. So let's just put in a rule here.

**[09:42](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=582s)** I'm going to bring something in from my clipboard again. You can see at the bottom,

**[09:45](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=585s)** there is a test section commented out. I'm going to replace this with the thing from my clipboard

**[09:50](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=590s)** and also just modify this to say MVP ball trick. And you can see that I've now got a test in place

**[09:55](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=595s)** which is going to enforce and assert that I can SSH to fake NARS on port 22. So if I now try and

**[10:03](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=603s)** change in my ACL rule further up here on the top, if I now try and change that to 443,

**[10:11](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=611s)** you can see I can't. That's because the test has failed. So I'd need to modify my test as well.

**[10:18](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=618s)** And now you can see I can save the ACL rule. And obviously notice that the SSH traffic has dropped

**[10:24](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=624s)** over here on the right hand side too. And so that's the general idea behind tests. If you try and

**[10:28](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=628s)** modify the file such that it breaks the test assertion, you can't do it. This can be particularly

**[10:34](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=634s)** useful while modifying things much further up in the file without realizing that you're actually

**[10:39](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=639s)** breaking connectivity that perhaps your CI server needs to make sure that it can actually connect

**[10:45](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=645s)** where it is into production to deploy for you or something. It's very easily done and these tests

**[10:50](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=650s)** prevent those mistakes from happening. TailScale SSH is one of my favourite tailscale features.

**[10:57](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=657s)** In fact, we have a whole separate tailscale explain video about the specifics of it.

**[11:02](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=662s)** Within a nutshell, it runs a second SSH server as part of the tailscale demon and intercepts

**[11:08](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=668s)** incoming SSH requests on the tailscale interface. It reuses the identity you implicitly provide

**[11:15](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=675s)** by being connected to your tailnet to validate against the parameters we set in our ACLs.

**[11:21](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=681s)** Those parameters allow or deny access via SSH. There are no SSH keys to manage. I just love

**[11:27](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=687s)** that feature so much and it's all handled transparently via tailscales identity and authentication.

**[11:34](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=694s)** Now in this ACL stands that we're about to cover, we're going to delve a little bit into groups,

**[11:39](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=699s)** tags and node ownership. All of the nodes in this example tailnet are currently owned by the

**[11:45](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=705s)** user that authenticated them. That's me and we can verify who owns the machine by looking under

**[11:50](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=710s)** its node name for this thing here. So this is a tailscales at gmail.com currently owns this node.

**[11:56](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=716s)** By default, we ship an ACL rule which allows all users to SSH into their own devices in check

**[12:02](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=722s)** mode. So let's just take a quick look at that. Head back over to your access controls page

**[12:07](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=727s)** and in the default policy file scroll down to the SSH stanza over here and you'll notice that

**[12:12](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=732s)** the action here is check. This check mode requires you to reauthenticate your client as per this check

**[12:19](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=739s)** period. The default value for this is every 12 hours. So in other words, if you want to SSH to a

**[12:25](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=745s)** specific node and validate someone's identity a little more strongly than just being logged into

**[12:30](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=750s)** the tailnet, you can have them reauthenticated a tailnet in order for the SSH connection to be allowed.

**[12:36](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=756s)** Now if that's a little too much for you, in my home lab at least, I don't need that level of

**[12:41](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=761s)** control. You can change this value to accept and this will simply allow you to connect via SSH

**[12:48](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=768s)** to these remote nodes by virtue of being connected to the tailnet. That will be enough identity

**[12:52](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=772s)** for you to proceed. You'll notice here that in this stanza we're using this special group called

**[12:57](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=777s)** auto group. This group automatically includes users and destinations or usernames with the appropriate

**[13:04](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=784s)** properties. There's a big long list of auto groups available in the documentation if you want to

**[13:09](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=789s)** make use of them and they can be really handy. One thing I want to point you to though is this

**[13:14](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=794s)** user's line here for SSH. At the moment, I'm allowed to SSH into this node as any user, both root

**[13:21](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=801s)** and a non-root user. But if I wanted to, for example, limit SSH access as root, I want to take that

**[13:28](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=808s)** permission away from somebody, I now click save. This is going to prevent me from SSHing to fake

**[13:34](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=814s)** NAS as root, presuming that the node itself actually allows SSH via root in its SSH configuration.

**[13:40](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=820s)** However, as you start to add lots of nodes and more likely lots of users, it can be handy to have

**[13:45](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=825s)** a way to allow only certain users to have SSH access to certain nodes or even not at all.

**[13:52](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=832s)** We can do this in a number of ways using the policy file, but the easiest way to group lots of

**[13:56](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=836s)** users together are groups. So let's create a couple of groups. So first, let's create two groups.

**[14:03](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=843s)** Scroll up to the top of your ACLs file and replace the group's stanza with something that looks

**[14:09](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=849s)** a little bit like this. You can find all of the syntax in the syntax reference in our documentation

**[14:14](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=854s)** over here. This can be really useful when creating automation that connects using SSH on the back end

**[14:20](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=860s)** like a GitHub action or some of the CICD workflow, but it's also probably just good practice to have

**[14:26](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=866s)** users group to affect their world views as a unit. Now you can see here in the policy file,

**[14:31](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=871s)** I've declared two groups, the admin group and the dev group. And once declared, we can now use

**[14:37](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=877s)** those groups in the policy to say that dev can SSH to nodes tagged as dev, for example. But in order

**[14:44](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=884s)** for that to work, you're going to have to create a tag owner as well. As the name suggests, ownership

**[14:50](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=890s)** of a node is owned by the tag and not a person anymore. Remember how if I just click save here

**[14:56](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=896s)** and go back to my machines page, remember how nodes are owned by the person that authenticated it

**[15:01](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=901s)** to the tailnet? Well, if we tag a node, it becomes owned by that tag. So let's create a tag owner.

**[15:08](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=908s)** In this case, I'm just going to paste in a few tags I made earlier. And we can see that I've got

**[15:12](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=912s)** the prod tag, the CI tag dev as well as container. Now if I click save, what I can do if I can go back

**[15:19](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=919s)** to my admin console, and I can now apply a tag to a specific node. So let's treat Magrathia,

**[15:26](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=926s)** for example, for a second, as a developer machine. I can now tag that as dev and we can start to

**[15:32](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=932s)** use our policy file to construct elaborate ways of preventing people from accessing certain things

**[15:38](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=938s)** that they're not supposed to access or don't need to access. Your security teams are going to

**[15:43](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=943s)** love this one. Note that the only way to fully untag a node completely and revert to a person

**[15:49](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=949s)** owning a node is to delete the node from your tailnet and reauthenticate it. So with all of that prep

**[15:56](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=956s)** out of the way, let's now start to look at the SSH stanza that we were looking at earlier in our

**[16:02](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=962s)** access controls. So scrolling to the bottom, that's where the SSH block typically lives.

**[16:07](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=967s)** I'm going to leave the default role in place because this is in reality, it's just a demo

**[16:12](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=972s)** talent for me that I can try examples for these videos for. But I'm going to add this second rule,

**[16:18](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=978s)** which would show the hypothetical conclusion of everything we just discussed. This rule allows users

**[16:24](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=984s)** in the dev group to SSH into nodes tagged as dev as a non-root user or the root user via SSH.

**[16:32](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=992s)** You can start to get really fancy and lock these things down by explicitly naming source and

**[16:38](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=998s)** destination hosts specific users. For example, let's say I don't want my developers to be able to access

**[16:44](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=1004s)** all non-root users. I only want them, for example, to be able to access the deploy user via SSH.

**[16:51](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=1011s)** If I click save now, you'll see that the tailnet policy files saves correctly. Now if I was on a

**[16:57](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=1017s)** node tagged as dev and I was trying to SSH into a remote node tagged as dev, I wouldn't be able to do

**[17:02](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=1022s)** it for any other user except the user deploy on the remote Linux system. This entire video has

**[17:08](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=1028s)** really only scratched the surface of what ACLs can do. It's quite a big topic and we didn't even

**[17:13](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=1033s)** get into stuff like doing it via getops. Getops would let you define your rulesetting code and deploy

**[17:19](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=1039s)** them automatically using a CI server. This will allow you to follow your organization's typical code

**[17:25](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=1045s)** review process on network infrastructure changes. So let us know down below if that's a video you

**[17:30](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=1050s)** would like to see and I'll make it for you. If you're interested in using tailscale at your company,

**[17:35](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=1055s)** reach out to our sales team to get started at tailscale.com slash contact slash sales.

**[17:40](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=1060s)** There'll be a link down below for that too. Thank you so much for watching. Happy ruleset making.

**[17:45](https://youtube.com/watch?v=Jn8_Sh4r8d4&t=1065s)** And until next time, I'm Alex from tailscale.

---

*Automatically generated transcript. May contain errors.*
