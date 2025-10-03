---
video_id: "WB8uTiD6JTo"
title: "Zero Trust Webinar Series: Part Two (Least Privileged Access)"
description: "As part of our multi-part series on migrating to a Zero Trust architecture, we will cover Least Privileged Access and related topics such as micro-segmentation and continuous verification. A fundament..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-04-29"
duration_seconds: 2850
youtube_url: "https://www.youtube.com/watch?v=WB8uTiD6JTo"
thumbnail_url: "https://i.ytimg.com/vi/WB8uTiD6JTo/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:34:20.400002"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 8236
transcription_time_seconds: 73.5
---

# Zero Trust Webinar Series: Part Two (Least Privileged Access)

**[00:00](https://youtube.com/watch?v=WB8uTiD6JTo&t=0s)** Thank you all so much for being here today. We are really excited to talk about least privilege access as part of our Zero Trust webinar series. Quickly, before we jump in, just want to really quickly introduce myself and my co-host. My name is Sydney, I lead marketing here at Tailscale. Jordan, why don't you do a quick intro? Hello, I had a product here as well, and that might have been a Freudian slip there, as I'm suffering a little bit from a cold today, so I am actually a little bit worse today.

**[00:30](https://youtube.com/watch?v=WB8uTiD6JTo&t=30s)** I promise that wasn't planned, but I'm happy to go with it. And just really quickly, as an agenda for what we're planning to talk about today, we're really excited to talk about all things least privilege access in some related topics.

**[00:45](https://youtube.com/watch?v=WB8uTiD6JTo&t=45s)** We will also then talk a little bit about least privilege access control in the context of Tailscale and what you're able to do to embody the tenants of Zero Trust and least privilege access with Tailscale. With that, I think we can go ahead and dive in.

**[01:03](https://youtube.com/watch?v=WB8uTiD6JTo&t=63s)** This is actually the second part of our Zero Trust series where we're talking about different concepts in Zero Trust. Really quickly, before we jump into least privilege access, wanted to just highlight what Zero Trust is in case there are folks here who aren't as familiar.

**[01:18](https://youtube.com/watch?v=WB8uTiD6JTo&t=78s)** Zero Trust is a security principle built on the idea of never trust always verify. So instead of assuming that devices, users, or network segments are inherently trustworthy.

**[01:29](https://youtube.com/watch?v=WB8uTiD6JTo&t=89s)** With Zero Trust enforcement, you are continually verifying the identification. You are ensuring that anyone or device in your network has least privilege access, which we'll talk more about today.

**[01:43](https://youtube.com/watch?v=WB8uTiD6JTo&t=103s)** And there's strict segmentation across all your resources to ensure that you know you can follow these the tenants of Zero Trust and make sure that the only the right folks or devices or services are connected to parts of your infrastructure.

**[01:59](https://youtube.com/watch?v=WB8uTiD6JTo&t=119s)** That you're trying to protect. So I will say with traditional perimeter based security models, there is typically a reliance on implicit trust, which is the idea that, you know, once someone or something is inside your network, you trust them and they have broad access, which creates some vulnerabilities that can be dangerous for the security of your business and infrastructure.

**[02:21](https://youtube.com/watch?v=WB8uTiD6JTo&t=141s)** Zero Trust eliminates this assumption that essentially once someone is inside your network that you can trust them implicitly forever.

**[02:28](https://youtube.com/watch?v=WB8uTiD6JTo&t=148s)** So, you know, oftentimes with Zero Trust, you'll see every request is authenticated or authorized based on identity and context. We're going to talk a lot more about that today.

**[02:38](https://youtube.com/watch?v=WB8uTiD6JTo&t=158s)** Access is granted on a least privilege basis. So just enough access to do the job, nothing more. Again, we're going to really dive deep into least privilege access today.

**[02:47](https://youtube.com/watch?v=WB8uTiD6JTo&t=167s)** There's this idea that lateral movement across your infrastructure should be restricted.

**[02:52](https://youtube.com/watch?v=WB8uTiD6JTo&t=172s)** So you're segmenting your infrastructure based on identity device and application layers and then continuous monitoring of all of that to ensure that, you know, even if you authenticate and authorize and you're giving someone access on a least privilege basis and you're restricting their lateral movement that you continue to trust that individual or that device on an ongoing basis.

**[03:16](https://youtube.com/watch?v=WB8uTiD6JTo&t=196s)** At its core, ultimately, Zero Trust is about securing connectivity in a world where traditional network boundaries no longer exist.

**[03:22](https://youtube.com/watch?v=WB8uTiD6JTo&t=202s)** And so we're, again, going to really dive deep into a couple core requirements and tenants of zero trust today, specifically going to talk about least privilege access and some related topics, microsegmentation continuous verification and a couple others.

**[03:38](https://youtube.com/watch?v=WB8uTiD6JTo&t=218s)** As mentioned before, this is the second in our zero trust webinar series. If you're interested in learning more about zero trust and connectivity.

**[03:47](https://youtube.com/watch?v=WB8uTiD6JTo&t=227s)** So the first bullet on this slide, we have a part one of a webinar that we can share and, you know, happy to follow up with questions related to that.

**[03:56](https://youtube.com/watch?v=WB8uTiD6JTo&t=236s)** And if you're interested in what isn't highlighted on on this slide, so monitoring and analysis and adaptive policies, we will do a future webinar and jump into that, you know, happy to follow up and share invite information about that future webinar when we have it scheduled.

**[04:15](https://youtube.com/watch?v=WB8uTiD6JTo&t=255s)** But let's jump into why we're here, which is to talk about least privilege access. You might sometimes see this abbreviated as LPA and least privilege access is core principle of zero trust security that essentially ensures users devices and applications have only the minimum level of access necessary to perform their function and nothing more.

**[04:38](https://youtube.com/watch?v=WB8uTiD6JTo&t=278s)** This really matters because in traditional security models, there's often an over provision of access. So you assume that users and system inside your trusted network are safe and always will be safe.

**[04:51](https://youtube.com/watch?v=WB8uTiD6JTo&t=291s)** That creates some pretty obvious security gaps where attackers can move laterally often compromising one system or even, you know, forgetting attackers, it could also just mean that someone that you trust in one part of your infrastructure makes a mistake and does something you didn't intend or don't want in a different part of your infrastructure and your security is jeopardized.

**[05:13](https://youtube.com/watch?v=WB8uTiD6JTo&t=313s)** Your product breaks or other problems occur, even if it wasn't, you know, an active attack. It was just a human error from someone you trust zero trust in least privilege access again eliminates this idea of implicit trust and it allows for enforcement of strict access controls based on identity role in context.

**[05:32](https://youtube.com/watch?v=WB8uTiD6JTo&t=332s)** Within least privilege access, there are some key levers we're going to dive a little bit deeper into today. One is this concept of identity centric authorization. So access is granted based on your verified identity role in real time context.

**[05:47](https://youtube.com/watch?v=WB8uTiD6JTo&t=347s)** There's also a concept of micro segmentation so users and workloads are isolated to prevent unrestricted movement across the network.

**[05:56](https://youtube.com/watch?v=WB8uTiD6JTo&t=356s)** The continuous verification, so access permissions are constantly re-evaluated based on real time risk signals and finally just in time access so temporary access is granted as needed and revoked when no longer necessary.

**[06:10](https://youtube.com/watch?v=WB8uTiD6JTo&t=370s)** And these are the concepts we're going to dive a little bit deeper into under this umbrella of least privilege access.

**[06:16](https://youtube.com/watch?v=WB8uTiD6JTo&t=376s)** So first I'll start with identity centric authorization. So this is really foundational to all of zero trust. Essentially you're ensuring that access decisions are based on identity rather than things like your network location, your IP address for static firewall rules.

**[06:36](https://youtube.com/watch?v=WB8uTiD6JTo&t=396s)** So with an identity centric authorization approach, you can enable granular dynamic access controls that adapt to user roles devices and risk levels.

**[06:46](https://youtube.com/watch?v=WB8uTiD6JTo&t=406s)** So you know the key components of this are one thinking of identity as this new perimeter, but with zero trust and identity centric authorization, we care more about who you are rather than where you are as a primary factor for access.

**[07:00](https://youtube.com/watch?v=WB8uTiD6JTo&t=420s)** Every access request is not only evaluated in real time, but it's evaluated based on identity attribute device posture and the contextual risk. The next layer down after you think of identity as this new perimeter is authenticating before access concepts like single sign on using an SSL through your identity providers for your IDP or having multi factor authentication where you not only need to password, but you also have to authenticate with a cell phone number, you be key or some other way to

**[07:29](https://youtube.com/watch?v=WB8uTiD6JTo&t=449s)** ensure you are who you say you are. And then there's obviously some device identity verification that can also happen on the actual device.

**[07:38](https://youtube.com/watch?v=WB8uTiD6JTo&t=458s)** So you know how this concept of identity as a perimeter, but then when someone does try to gain access, you really authenticate them and their device in multiple ways to ensure that they are who you think they are.

**[07:51](https://youtube.com/watch?v=WB8uTiD6JTo&t=471s)** And then there's a level deeper that you can and should get to, which is role based and attribute based access control. So you might have heard the acronym are back, for example.

**[08:01](https://youtube.com/watch?v=WB8uTiD6JTo&t=481s)** And all this is saying is that, you know, yes, we have this identity as a perimeter we've authenticated you are who you say you are, but we also might care about what your role is in the company too.

**[08:12](https://youtube.com/watch?v=WB8uTiD6JTo&t=492s)** So does every engineer or IT admin or someone in HR or someone in marketing, should they get access to your entire infrastructure or could be provide access to parts of your infrastructure just based on not only who they say they are, but the role they have.

**[08:29](https://youtube.com/watch?v=WB8uTiD6JTo&t=509s)** You can also take this a step further with attribute based access control, so not just look at their title, but also things like their exact location, the time of day security posture device type.

**[08:42](https://youtube.com/watch?v=WB8uTiD6JTo&t=522s)** For example, you could say, again, we have identity as its new perimeter, someone has requested access with SSO and MFA and we trust them and they're the right, they're an engineer, they're the right role for what they've applied to, but maybe they're on vacation in a geography where we know that there's a lot of security risk.

**[09:01](https://youtube.com/watch?v=WB8uTiD6JTo&t=541s)** You might say okay, hey, actually, even though we trust you, we don't want you accessing this critical infrastructure from the location you're in because of other other reasons.

**[09:12](https://youtube.com/watch?v=WB8uTiD6JTo&t=552s)** And on top of this, you could have things like policy enforcement point sometimes called PEPs or PEPs, which say like okay, we're going to look at all the whole world of who someone is and how they've tried to get access their role, other attributes and we're actually going to give points to all of those different factors.

**[09:30](https://youtube.com/watch?v=WB8uTiD6JTo&t=570s)** And then say okay, the moment someone has points beyond this threshold, there are too many risks and we're not going to trust them and so this can also really help with identity centered authorization where you kind of layer in all of the different facets of identity and assign them different kind of risk points.

**[09:49](https://youtube.com/watch?v=WB8uTiD6JTo&t=589s)** And then finally, on top of all of that, you have to do the continuous authentication. So again, just because you know someone is who they say they are, they've kind of passed the access controls, they have the right role, they have the right attributes doesn't mean that now their access is indefinite, you have to do the continuous authentication to ensure that they continue to be who we expect them to be.

**[10:12](https://youtube.com/watch?v=WB8uTiD6JTo&t=612s)** And all this is to say is when you do identity center got their authorization correctly, you're able to eliminate implicit trust, you can enable to find grain control, reduce attack surfaces and improve overall compliance.

**[10:30](https://youtube.com/watch?v=WB8uTiD6JTo&t=630s)** Moving on, the next kind of key tenant of least privilege access and an important part of zero trust is micro segmentation. So this enforces these privilege privilege access by dividing networks into isolated segments and controlling traffic.

**[10:45](https://youtube.com/watch?v=WB8uTiD6JTo&t=645s)** Between them based on identity policy risk. So instead of flat network, where an attacker can move freely once inside micro segmentation restricts access at a granular level.

**[10:56](https://youtube.com/watch?v=WB8uTiD6JTo&t=656s)** When you also layer in micro segmentation, what it allows you to do is say we're not going to kind of take the traditional approach of having a really broad perimeter that, you know, once someone kind of passes all those bars, they they have access to kind of everything inside that perimeter.

**[11:12](https://youtube.com/watch?v=WB8uTiD6JTo&t=672s)** We're going to instead micro segment and enforce kind of strict access controls between workloads applications and users, even within that perimeter, each segment is isolated so that a breach in one area does not impact others.

**[11:27](https://youtube.com/watch?v=WB8uTiD6JTo&t=687s)** This is really important if there is a vulnerability that an attacker or someone who makes mistakes accidentally takes advantage of your whole network doesn't go down, your whole infrastructure doesn't go down, you've been able to isolate that vulnerability in one place.

**[11:41](https://youtube.com/watch?v=WB8uTiD6JTo&t=701s)** And again, identity and context is going to be really important to this. So instead of relying on static IPs or VLANs micro segmentation uses that identity role in real time security signals to enforce the access policies you have in place.

**[11:54](https://youtube.com/watch?v=WB8uTiD6JTo&t=714s)** So access is determined by who the user is what device they're using in their security context and that check is again continuous.

**[12:03](https://youtube.com/watch?v=WB8uTiD6JTo&t=723s)** You can also do things under the umbrella of micro segmentation to isolate workloads or even applications, you can say each application database or containers in a separate security zone.

**[12:15](https://youtube.com/watch?v=WB8uTiD6JTo&t=735s)** So preventing even further lateral movement. You can even have service to service segmentation. So only approved services can communicate with each other and you can even have environment segmentation. So you want your dev testing and production environment strictly separated.

**[12:31](https://youtube.com/watch?v=WB8uTiD6JTo&t=751s)** So again, you can kind of play around in sandboxes without worrying about creating problems in parts of your infrastructure or with your customers or users that you don't want or don't expect.

**[12:42](https://youtube.com/watch?v=WB8uTiD6JTo&t=762s)** When you have micro segmentation, it also kind of enables more sophisticated policy based enforcement. So you can use access control lists or ACLs to define explicit rules for who can access what.

**[12:55](https://youtube.com/watch?v=WB8uTiD6JTo&t=775s)** Again, this could be role based so like engineers can access the database, but they can access HR records. You can also do things and Jordan will talk a lot more about how easy this is with tail scale, but you can use tags and labeling to kind of create groups among devices, user services, really anything your network to kind of create a group that then that group can have access to certain parts of your infrastructure.

**[13:17](https://youtube.com/watch?v=WB8uTiD6JTo&t=797s)** And all this means that you can have really dynamic policies that adjust. So, you know, even to the degree of like, hey, when a device has an outdated operating system, you can stop trusting it. And so micro segmentation really allows overall for that really granular access control and security.

**[13:37](https://youtube.com/watch?v=WB8uTiD6JTo&t=817s)** So again, you know, in this kind of umbrella at least privileged access, you aren't creating vulnerabilities, even with folks who trust by having this really kind of broad perimeter of what a person or divide kind of fact.

**[13:55](https://youtube.com/watch?v=WB8uTiD6JTo&t=835s)** All right, I'm going to keep trucking. So we talked about this a lot already. So I'm not going to harp too much on this point, but it's really important with anything you're doing in zero trust release privilege access that you continually verify.

**[14:09](https://youtube.com/watch?v=WB8uTiD6JTo&t=849s)** Accord 10 out of zero trust is that you're not going to just be one and done with trust you're not going to trust someone once and then trust them forever. You have to continuously evaluate and make sure that things like steel sessions or credential hijacking or unauthorized lateral movements aren't happening within your network.

**[14:28](https://youtube.com/watch?v=WB8uTiD6JTo&t=868s)** And to ensure that not only are you secure today, but you will continuously be secure.

**[14:33](https://youtube.com/watch?v=WB8uTiD6JTo&t=873s)** Again, really important component of this is moving beyond the mindset of one time off authentication, no more static trust. We're not going to, you know, just because a user log in successfully once allow for the retention of that access indefinitely.

**[14:49](https://youtube.com/watch?v=WB8uTiD6JTo&t=889s)** No more persistent trust. We need to reevaluate it every step and ensure that the identity device security posture and behavioral anomalies were watching are being watched in real time.

**[15:00](https://youtube.com/watch?v=WB8uTiD6JTo&t=900s)** And as I mentioned before, we'll talk a lot more about monitoring in a future zero trust webinar, but it's really important to couple that with this continuous verification effort.

**[15:10](https://youtube.com/watch?v=WB8uTiD6JTo&t=910s)** And why we care about continuous verification or the level above that is because when you continually verify what you're actually getting is a continuous risk based evaluation of the access in your network.

**[15:22](https://youtube.com/watch?v=WB8uTiD6JTo&t=922s)** So once you're continually checking, it means that you can surface more easily behavioral anomalies, you can do device posture checks. So to ensure devices are meeting that security baseline, you know, things like up to date operating system endpoint protection enabled.

**[15:37](https://youtube.com/watch?v=WB8uTiD6JTo&t=937s)** Anything that you really care about or matters to your business or projects kind of device posture.

**[15:44](https://youtube.com/watch?v=WB8uTiD6JTo&t=944s)** And then it also means that you can have really adaptive access controls. So again, if you see risk increases increase, you can restrict your access immediately.

**[15:56](https://youtube.com/watch?v=WB8uTiD6JTo&t=956s)** And all of this can be automated. So it's a, you know, I think one challenge with a lot of traditional security approaches is

**[16:05](https://youtube.com/watch?v=WB8uTiD6JTo&t=965s)** If you wanted to kind of create this in a custom way, you'd have to do it manually now with tools like tail scale and other tools on the market.

**[16:12](https://youtube.com/watch?v=WB8uTiD6JTo&t=972s)** This can all be automated. So you set up your system. You set up these controls and the continuous verification just happens.

**[16:19](https://youtube.com/watch?v=WB8uTiD6JTo&t=979s)** And again, this also allows for other really kind of exciting zero trust benefits, things like again, we've already talked about dynamic policy adjustments are changing those policies really quickly in real time.

**[16:32](https://youtube.com/watch?v=WB8uTiD6JTo&t=992s)** It also allows for just in time reauthentication and also allows for things like automatic revocation when the session times out and making sure, you know, human error isn't a core vulnerability, you know, we've all heard of the story of someone's at a wee work. They leave

**[16:49](https://youtube.com/watch?v=WB8uTiD6JTo&t=1009s)** They're laptop open. They run at the bathroom. They grab a coffee and someone, you know, a bad actor walked by Snoop did something nasty while while they were away from their seat for even just five minutes.

**[17:01](https://youtube.com/watch?v=WB8uTiD6JTo&t=1021s)** And again, all of this together with continuous verification, it's really just about giving you the security signals you need to make sure everything is is good and safe in your infrastructure.

**[17:14](https://youtube.com/watch?v=WB8uTiD6JTo&t=1034s)** You have those identity and device posture signals integrated with your IDP, you know, MDM's EDR solutions, like whatever you're using to kind of secure your devices in your network.

**[17:26](https://youtube.com/watch?v=WB8uTiD6JTo&t=1046s)** And you have that awareness about what's going on in your network and who is engaging with it from, for example, high risk locations or for an IP's in a way that feels anomalous and could be a signal that someone is a bad actor.

**[17:42](https://youtube.com/watch?v=WB8uTiD6JTo&t=1062s)** And it also means you can leverage tools and Jordan will talk a little bit about this in the context of tailscale, but around audit logging and incident responses. So if all of the structure of your zero trust security is set up properly, then you can spend your time on DevOps, IT security focused on the actual kind of monitoring response to incidents instead of just like spending all of your time.

**[18:09](https://youtube.com/watch?v=WB8uTiD6JTo&t=1089s)** Giving and revoking access or dealing with basic connectivity tickets. And again, this continuous verification what it gets you is that elimination of persistent trust, the prevention of lateral movements reduction and insider threats and ensures that you're compliant.

**[18:26](https://youtube.com/watch?v=WB8uTiD6JTo&t=1106s)** And last but not least, we'll talk a little bit about just in time access. So this is, I think, one of the best modern security opportunities as it relates to zero trust and least privilege access, because it basically says, hey, yes, we know all the people that are accessing our infrastructure and the devices, we trust them, we have everything set up in place.

**[18:49](https://youtube.com/watch?v=WB8uTiD6JTo&t=1129s)** But there might be times when part of your infrastructure needs support from a team that doesn't usually touch it or an application that doesn't usually connect. And how do we in a really sustainable scalable way, give that access.

**[19:04](https://youtube.com/watch?v=WB8uTiD6JTo&t=1144s)** What just in time access means is you can provide access to those systems only when needed for a limited time, under strict policy controls. So you don't have to spend a lot of cycles spinning up and winding down access, you can in an automated way, give that access to the team that needs it that you trust for that moment of time when they needed and no more.

**[19:28](https://youtube.com/watch?v=WB8uTiD6JTo&t=1168s)** And what that means is access is a femoral so you reduce the risk of credential abuse, again, reducing the risk of lateral movements and insider threats.

**[19:38](https://youtube.com/watch?v=WB8uTiD6JTo&t=1178s)** And the key components of just in time or get access are eliminating this idea of standing privileges. So again, and traditional security models, a security team might have to grant permission to an ad hoc team that needs to jump in and address the problem, but then they also have to remember to take those credentials away.

**[19:58](https://youtube.com/watch?v=WB8uTiD6JTo&t=1198s)** Which is just more overhead for that team and creates risk.

**[20:03](https://youtube.com/watch?v=WB8uTiD6JTo&t=1203s)** Jit replaces this always on access with time limited just in time access. So you don't have this problem of sale credentials leading to an attack.

**[20:12](https://youtube.com/watch?v=WB8uTiD6JTo&t=1212s)** And what time loaded just in time access means is again, users only get access when they exactly needed.

**[20:19](https://youtube.com/watch?v=WB8uTiD6JTo&t=1219s)** And this can be kind of pre-approved in a couple different ways. So one way is based on time. So you say, hey, we're going to give you access for pre-determined duration of time.

**[20:31](https://youtube.com/watch?v=WB8uTiD6JTo&t=1231s)** We think it'll take you 30 minutes to go in, deploy the fix and come out. So we're just going to give you access for 30 minutes and it's going to automatically expire when the task is done.

**[20:39](https://youtube.com/watch?v=WB8uTiD6JTo&t=1239s)** You know, you can also do things like set it based on the actual task being done. So, hey, we know that you're working on this deployment. When the deployment is done, we can kind of link our jet access to that deployment. And then when the task is complete, your access expires right away.

**[20:59](https://youtube.com/watch?v=WB8uTiD6JTo&t=1259s)** You can also do things based on like temporary rule changes, temporary location changes essentially just means adding kind of a temporary layer onto all of the identity and access controls we've already talked about.

**[21:14](https://youtube.com/watch?v=WB8uTiD6JTo&t=1274s)** And what's kind of ironic about jet access is if you set up the system to allow for this, if you set this up properly, it actually makes it easier to give people access, but without compromising your security. So you can have more self service requests, particularly if there is kind of a routine task that's done, let's say, once a quarter and you know this team.

**[21:39](https://youtube.com/watch?v=WB8uTiD6JTo&t=1299s)** It is going to need access for this period of time. You could think of, for example, like a finance team closing a book at the end of a quarter, but you can actually set that up to be self served. So you don't need to spend a lot of manual time.

**[21:51](https://youtube.com/watch?v=WB8uTiD6JTo&t=1311s)** You can bake that into your kind of security system. It also actually makes it easier to for managers and peers to kind of approve and review because, you know, you're not giving access indefinitely. And so there doesn't need to be as much of this intense kind of security.

**[22:08](https://youtube.com/watch?v=WB8uTiD6JTo&t=1328s)** Review because we're only given access for 30 minutes or a really set period of time. And it also means that you can, again, be creative in how you kind of customize that jit access around unusual location and usual device and again time and all this usually will still have the benefit of that monitoring again we'll talk about that more next time.

**[22:33](https://youtube.com/watch?v=WB8uTiD6JTo&t=1353s)** But if you have things enabled in your security system, be a tailscale or another tool you're using to do like session recording or audit logs jit is covered in that. So you can still see what folks are doing. It doesn't. It's not like an all access pass for the time period.

**[22:49](https://youtube.com/watch?v=WB8uTiD6JTo&t=1369s)** That the access is granted. But all this means is that you're preventing kind of this privilege creep that can tend to happen in traditional systems where access is kind of accumulated unnecessarily over time.

**[23:01](https://youtube.com/watch?v=WB8uTiD6JTo&t=1381s)** You reduce the chance of an insider threat, even if it's just a human error and a mistake that someone makes you minimize the attack surface and overall it's easier to be compliant.

**[23:15](https://youtube.com/watch?v=WB8uTiD6JTo&t=1395s)** And all this is to say is, you know, whether you're using tailscale or another system. I definitely recommend kind of checking out the current solution you use and make sure it's not falling short.

**[23:26](https://youtube.com/watch?v=WB8uTiD6JTo&t=1406s)** A lot of legacy solutions will, you know, say that there's your trust because it's like a kind of a buzzy word right now.

**[23:34](https://youtube.com/watch?v=WB8uTiD6JTo&t=1414s)** But if you actually look under the hood, what you'll see is they're not doing identities centric authorization.

**[23:40](https://youtube.com/watch?v=WB8uTiD6JTo&t=1420s)** The solutions are overly complex with rigid identity infrastructure, VPNs and static IP white listing is leading to a lot of security headaches and there might be like to rigid our back because there isn't.

**[23:51](https://youtube.com/watch?v=WB8uTiD6JTo&t=1431s)** Again, that flexibility and control a lot of customer needs to happen.

**[23:56](https://youtube.com/watch?v=WB8uTiD6JTo&t=1436s)** Or on the micro segmentation side, you might see an over reliance on firewalls and VLANs, you might see a lack of application where segmentation again static ACLs that are never being updated and a lack of visibility into what's actually happening inside your network and inside those segments.

**[24:13](https://youtube.com/watch?v=WB8uTiD6JTo&t=1453s)** Often legacy solutions don't do that continuous verification. It really is still just a one time authentication, which leads to long term risk.

**[24:22](https://youtube.com/watch?v=WB8uTiD6JTo&t=1462s)** There aren't those real time security signals or manual incident response delays. And there isn't real jet access. And so you can't prevent those standing privileges and all the problems that come with that.

**[24:35](https://youtube.com/watch?v=WB8uTiD6JTo&t=1475s)** And ultimately, what this all leads to if you're if you're kind of security or networking connectivity solutions are legacy is engineers who are frustrated because they're not getting access provisioned in a timely way.

**[24:52](https://youtube.com/watch?v=WB8uTiD6JTo&t=1492s)** Their VPN might be slow and unreliable. They're accidentally breaking things. They're blocked from fixing incidents when things slow down or when things do break. And overall, it means everything is slower.

**[25:03](https://youtube.com/watch?v=WB8uTiD6JTo&t=1503s)** And so while you might not be able to point to a direct connection between these legacy solutions and lower revenue or worst business outcomes, what you'll hear from your engineering team is that they're slow that they're frustrated all the time and it just can't get their work done.

**[25:20](https://youtube.com/watch?v=WB8uTiD6JTo&t=1520s)** And then on the IT and security side, what you might hear is they're just spending hours and hours on permission tickets that feel like busy work like it feels like it could and should be automated.

**[25:31](https://youtube.com/watch?v=WB8uTiD6JTo&t=1531s)** They're struggling to maintain the rules that are in place. They're having to kind of constantly add and remove access.

**[25:39](https://youtube.com/watch?v=WB8uTiD6JTo&t=1539s)** You might also hear about shadow IT. So teens at the company, particularly engineering teams just saying it's not worth it. They're so frustrated. And so they kind of bypass whatever systems, IT and security or setting up, which obviously create a lot of vulnerability and a lot of risk.

**[25:55](https://youtube.com/watch?v=WB8uTiD6JTo&t=1555s)** IT and security, spending a lot of time chasing down, stale permissions. They feel like they can't do their job well.

**[26:01](https://youtube.com/watch?v=WB8uTiD6JTo&t=1561s)** And it's again, this really frustrating situation where they're scrambling to contain threats reactively, but then also spending a lot of their time on what amounts to busy work that should just be automated. So they're instead focused on on real threats and real monitoring instead of just like dealing with frustrated engineers and their tickets.

**[26:21](https://youtube.com/watch?v=WB8uTiD6JTo&t=1581s)** But thankfully, tailscale has a lot of really great solutions that mitigate all of these frustrations and problems that are pretty common with legacy solutions.

**[26:30](https://youtube.com/watch?v=WB8uTiD6JTo&t=1590s)** And so with that, I'm going to hand things off to Jordan, who is going to talk a little bit more about tailscales approach to least privilege access and some of the benefits you might feel and see if you use tailscale.

**[26:43](https://youtube.com/watch?v=WB8uTiD6JTo&t=1603s)** Perfect.

**[26:44](https://youtube.com/watch?v=WB8uTiD6JTo&t=1604s)** Thanks. And as you mentioned, we do have a unique way of kind of going after your trust because of the architecture of tailscale, right?

**[26:50](https://youtube.com/watch?v=WB8uTiD6JTo&t=1610s)** But it is all built on these same foundational pillars that Sydney's was discussing whether we're talking about continuous verification, microseconditation, active assurance or obviously that idea of discovering seeing what's out there.

**[27:02](https://youtube.com/watch?v=WB8uTiD6JTo&t=1622s)** Now what makes us unique is continuous validation is really the user I didn't even built into the network, which we'll see here in a second, but it also takes in all that extra context that Sydney was mentioning around that device.

**[27:12](https://youtube.com/watch?v=WB8uTiD6JTo&t=1632s)** Identity and user and device state and patching that all together so you can make educated choices on who should actually have access to your network.

**[27:20](https://youtube.com/watch?v=WB8uTiD6JTo&t=1640s)** We talk about microseconditation, it really not just about device device or users devices, right? There's also SaaS apps and platforms as a service and all of these need to be able to be taken apart of your connectivity solution so that you can have zero trust across your entire environment.

**[27:36](https://youtube.com/watch?v=WB8uTiD6JTo&t=1656s)** And we talk about active insurance will look shortly around how we enable you to have visibility and the threats, you have network logs and audit logs.

**[27:44](https://youtube.com/watch?v=WB8uTiD6JTo&t=1664s)** And again, that idea of discovery, having a complete inventory of everything on your network really makes this unique, right? We talk about how tailscale is built and it is a mesh network that sits on top.

**[27:55](https://youtube.com/watch?v=WB8uTiD6JTo&t=1675s)** But identity is built into it at the layer three, built from your your identity provider, whether we're talking about Google or intrad, your users log in via that SSO and have that identity embedded in every request they make across the network.

**[28:08](https://youtube.com/watch?v=WB8uTiD6JTo&t=1688s)** So here we see Omelie logging in, we verify her identity and then through ACLs, which we'll see here in a second, we can control their access to exactly what they need to get.

**[28:17](https://youtube.com/watch?v=WB8uTiD6JTo&t=1697s)** So here we see the compute and server, but this does look like a large complex graph compared to your average network, right?

**[28:23](https://youtube.com/watch?v=WB8uTiD6JTo&t=1703s)** So as you skip to the next slide, we really see how we make this simpler in tailscale via our ACLs. So our ACLs are access control lists that you can manage this code that allows you to control exactly which groups or users can see which devices or groups of devices here we see David and Omelie again, whether they're in a group of employees and we can control whether they're having access to SaaS apps or making sure they.

**[28:47](https://youtube.com/watch?v=WB8uTiD6JTo&t=1727s)** Access different internet resources via an exit notes that they're always coming off the same IP, but at the same time blocking them from reaching production infrastructure that only engineers should have.

**[28:58](https://youtube.com/watch?v=WB8uTiD6JTo&t=1738s)** And so this allows us to create these dynamic software to find primators that you can create in real time either via infrastructure as code or via APIs and again explicitly authorizing the resources accessible just for that user to get their job done.

**[29:12](https://youtube.com/watch?v=WB8uTiD6JTo&t=1752s)** Again, we can integrate this into IC with get officer others to have that velocity or we see customers doing this via automation on top of our API.

**[29:20](https://youtube.com/watch?v=WB8uTiD6JTo&t=1760s)** If we go to the next piece, it really is around this identity base, excuse me, we got too many slots today, my sick brain.

**[29:29](https://youtube.com/watch?v=WB8uTiD6JTo&t=1769s)** And we talked about zero trust with test tailscale, right, the least privileged access that mesh is capable of providing hypergranate because we know about every node and connections in between those and we enforce those on the node.

**[29:40](https://youtube.com/watch?v=WB8uTiD6JTo&t=1780s)** So we have again user and device groups.

**[29:43](https://youtube.com/watch?v=WB8uTiD6JTo&t=1783s)** We have the idea of tags, which allows you to tag a specific service account identities, both controlling what other machines can go to, but also again controlling which users and devices can come into them.

**[29:56](https://youtube.com/watch?v=WB8uTiD6JTo&t=1796s)** IP and domain rules are even ports and protocol rules we can get into that granular context and make sure they have access to exactly what they need.

**[30:04](https://youtube.com/watch?v=WB8uTiD6JTo&t=1804s)** I kind of alluded to this a little bit earlier, but with tailscale, we really do have the magic and activity across all of your different resources, its network and cloud agnostic, allowing to wrap things and BTCs or Kubernetes, but also software as a service and infrastructure as a service like RDS and other databases, bringing these all into one system and allowing the control access.

**[30:24](https://youtube.com/watch?v=WB8uTiD6JTo&t=1824s)** Either again by users by their identity of groups or via machines and services is sitting alluded to earlier and the skills globally with regional routing built into the network, allowing to distribute as fast as possible across all your different environments.

**[30:38](https://youtube.com/watch?v=WB8uTiD6JTo&t=1838s)** And finally, we talk about continuous verification, it is built into the way tailscale works every specific request is going out with that identity and we're able to check both whether they check signed in via SSO.

**[30:50](https://youtube.com/watch?v=WB8uTiD6JTo&t=1850s)** They have the right groups going on and we also get down until the city was mentioning earlier what clients they're using and an MDM based appointments as well if there's specific attributes that you're using to get to qualify trust whether these are specific to your business or general kind of ratings that you want to look at.

**[31:08](https://youtube.com/watch?v=WB8uTiD6JTo&t=1868s)** You can either do this with tailscale individually or integrate with tools like Jamf to have these attributes pushed out to your devices through device posture management.

**[31:18](https://youtube.com/watch?v=WB8uTiD6JTo&t=1878s)** Really is a long list here right of just general tailscale security features, but it is good to understand the foundation that enables us to see your trust again, we talked about the identity of where mesh network is all built on top of wire guard that enables these end to end tunnels between devices enabling zero trust between them.

**[31:36](https://youtube.com/watch?v=WB8uTiD6JTo&t=1896s)** You have HTPS services that you're looking to deploy as well, we can handle that for you managing all your certificates and making sure these users having access to exactly what they need.

**[31:45](https://youtube.com/watch?v=WB8uTiD6JTo&t=1905s)** We talked a little bit more about everything being built around SSO, we do have advanced provider support there, whether you're looking at Google or Microsoft with support for nested groups or even get hub and octa.

**[31:56](https://youtube.com/watch?v=WB8uTiD6JTo&t=1916s)** We mentioned a little bit earlier around enforcing least privilege access with our access control is or ACLs here, you can write our back policies based on again those users and roles, but also contacts about the device that they're coming from and what they're trying to connect to so here we're talking about different things on tags and ports again limiting exactly to where you want them to connect.

**[32:18](https://youtube.com/watch?v=WB8uTiD6JTo&t=1938s)** We talk about user provisioning and group syncing or skin, we have support across Microsoft and Google allowing you to have automated updates of your groups and keeping that in sync with tailscale, making sure you only have to manage that in one single place.

**[32:32](https://youtube.com/watch?v=WB8uTiD6JTo&t=1952s)** For some of our customers that have a little higher security kind of.

**[32:37](https://youtube.com/watch?v=WB8uTiD6JTo&t=1957s)** Guard rails or kind of less rest tolerance, we have the idea of tailnet walk, which is disables anything from joining your network unless they've been signed by a trusted node inside your network it is a little extra work to get nodes added for customers that want that it is out there and able to take advantage of.

**[32:55](https://youtube.com/watch?v=WB8uTiD6JTo&t=1975s)** Now we talk about ACLs, some people are a little either new to managing this is code or a little worried that you know a fat finger or something can throw off their access list.

**[33:04](https://youtube.com/watch?v=WB8uTiD6JTo&t=1984s)** And so we have this idea of ACL tests that allow you to write test against your access control list to safely maintain desire configuration. So if we want to make sure no one.

**[33:13](https://youtube.com/watch?v=WB8uTiD6JTo&t=1993s)** Except engineers ever have access to prod we can actually write a test as part of our access control list and when we make edits we can always make sure those tests pass before that new ACL changes rolled out.

**[33:25](https://youtube.com/watch?v=WB8uTiD6JTo&t=2005s)** And as we mentioned before we do support get offs for ACLs when you're starting to get going you can click and point inside the UI but as soon as you do reach scale most customers choose to go down that get offs either with terraform or others.

**[33:38](https://youtube.com/watch?v=WB8uTiD6JTo&t=2018s)** And able to manage this as code that gives you all the version control around this and the safety of PR reviews and others.

**[33:45](https://youtube.com/watch?v=WB8uTiD6JTo&t=2025s)** So again integrating into the tools you are to use and trying to make it easy to take advantage of these security features.

**[33:55](https://youtube.com/watch?v=WB8uTiD6JTo&t=2035s)** Now security is one thing but we have to obviously enable control and compliance as well we talked about visibility earlier and we do have the idea of both audit logging and network flow logging so.

**[34:05](https://youtube.com/watch?v=WB8uTiD6JTo&t=2045s)** Audit logs will allow you to see all changes to your system and people coming on to it whereas network flow logging literally allows you to see all the requests that are going between nodes on the tail net.

**[34:14](https://youtube.com/watch?v=WB8uTiD6JTo&t=2054s)** And you have the ability to stream these out to your seem of choice for monitoring and putting up compliance requirements or just for further investigation if you want to dig in either for a security reason or for kind of a troubleshooting reason trying to understand connectivity between two devices.

**[34:28](https://youtube.com/watch?v=WB8uTiD6JTo&t=2068s)** As we mentioned earlier we do have device posture management built into the system you whether through integrations with other services like mobile device management allowing you to manage your telescope diplomas not just for desktop applications but also across Android and iPhones as well.

**[34:44](https://youtube.com/watch?v=WB8uTiD6JTo&t=2084s)** Automated user provisioning and group syncing allows you to automatically sync your user groups between octan azure ad via skim and also works with Google workspace via their proprietary technology.

**[34:55](https://youtube.com/watch?v=WB8uTiD6JTo&t=2095s)** But again making it easier for admins to manage this list versus having to do a whole separate process on the side.

**[35:02](https://youtube.com/watch?v=WB8uTiD6JTo&t=2102s)** And finally we do have the idea of device approvals and node inside the network here allows you to have device approvals either by admins or others when people are joining your talent either new you know employees or new contractors.

**[35:16](https://youtube.com/watch?v=WB8uTiD6JTo&t=2116s)** People can't just join and get immediate access they have to go through an approval process to get there.

**[35:24](https://youtube.com/watch?v=WB8uTiD6JTo&t=2124s)** And we talk about determining trustworthiness with device posture management again it goes beyond just the identity here we're able to build different controls on the attributes so customers can create device posture is based on individual things like the operating system or serial numbers etc allowing you to say not only this user can do certain things but this user can do certain things when they're on a certain device.

**[35:49](https://youtube.com/watch?v=WB8uTiD6JTo&t=2149s)** Here on the right we see that omelette must have had a company issued iPhone and MacBook didn't meet their posture requirements but they can't just bring an unknown Android device into the network without having device approval.

**[36:02](https://youtube.com/watch?v=WB8uTiD6JTo&t=2162s)** Again this does integrate with industry leading EDR and indeed MDM tools to fetch these additional device attributes so we have a few numbers things like the IP where they're originating and others built into tail scale.

**[36:13](https://youtube.com/watch?v=WB8uTiD6JTo&t=2173s)** But you can also integrate with your tool of choice to bring in all that extra metadata and then build your trust context on top of that.

**[36:27](https://youtube.com/watch?v=WB8uTiD6JTo&t=2187s)** And as Sydney mentions earlier we do have just in time access built on top of device posture allowing you to give users secure temporary access.

**[36:36](https://youtube.com/watch?v=WB8uTiD6JTo&t=2196s)** Exact use cases were speaking of before for instance maybe you have deployments that have to happen at a certain time or certain maintenance tasks that happen every Friday night at 5 p.m.

**[36:46](https://youtube.com/watch?v=WB8uTiD6JTo&t=2206s)** You can now automate this temporary access through just in time API's or as the screenshot we were looking at earlier we do have a slack bot working engineers and others can request this access on demand and have device approval happened underneath the scenes.

**[37:01](https://youtube.com/watch?v=WB8uTiD6JTo&t=2221s)** Again this is really just all about protecting your critical production infrastructure really no one needs.

**[37:07](https://youtube.com/watch?v=WB8uTiD6JTo&t=2227s)** Global access to production 24 hours a day right you need to get in there and do specific jobs and as Sydney mentioned earlier you can now tie access to those specific workflows whether you're talking about just having it on a time based period or actually using our APIs and tying it to your deployments so when a CDI pipeline finishes or deployment finishes you can revoke access either for a user or for that specific CID C pipeline so they only have access when they need to get their jobs.

**[37:35](https://youtube.com/watch?v=WB8uTiD6JTo&t=2255s)** Again we talk about just leveraging seamless automation here for more resources just in time is really the perfect way to get them their access without having code out or tokens out in the wild that could be compromised and give people access to your production infrastructure.

**[37:52](https://youtube.com/watch?v=WB8uTiD6JTo&t=2272s)** And I think this is probably very kind of familiar things and kind of you have to see competitors out there that have kind of similar offings I do think our mesh base approach is a little different than what you see from legacy vendors obviously and remove some of the bottlenecks.

**[38:06](https://youtube.com/watch?v=WB8uTiD6JTo&t=2286s)** But here is an interesting very interesting piece of tail scale that allows you to actually build your own services that are identity aware as well so before we talked a lot about you know devices and sass here we're talking about building internal services that can take advantage of that identity is being built into every request that comes through tail scale.

**[38:25](https://youtube.com/watch?v=WB8uTiD6JTo&t=2305s)** So here on the left you see the idea of our tsnaggo package as you can import into any application you're building and allows you to spin up a server on a specific port and hostname

**[38:34](https://youtube.com/watch?v=WB8uTiD6JTo&t=2314s)** when this services were getting new information or new requests from internal services you does come through with these identity headers that you see here with your application then can take advantage of it's important to point out that you don't have to use the tsnaggo package to take advantage of these identity headers these are always available on in your quest is coming through it's just a tsnag makes it easier and gives you a little bit of a library to have accessors and access to get to this information.

**[39:02](https://youtube.com/watch?v=WB8uTiD6JTo&t=2342s)** And finally we have a new way of writing ACLs that you might not have seen in the past which is the idea of ACL grants this is actually going GA here in the next couple months but the cool piece here is this idea of being able to actually write ACLs in type side of tail scale the control access downstream.

**[39:20](https://youtube.com/watch?v=WB8uTiD6JTo&t=2360s)** So here you're seeing you know a service has been added on example.com we're enabling read access but only giving right access to a specific group of admins.

**[39:29](https://youtube.com/watch?v=WB8uTiD6JTo&t=2369s)** Again this is something you can do today whether you're talking about building on tsnaggo or taking advantage of a number of community plugins which you can see on our website today but it does give you that other way of bringing in these services and having all your controls across them all codified in one single place.

**[39:49](https://youtube.com/watch?v=WB8uTiD6JTo&t=2389s)** Great and with that we come to the end of our presentation. I hope folks learn a little bit about least privilege access and some other facets of zero trust.

**[40:01](https://youtube.com/watch?v=WB8uTiD6JTo&t=2401s)** I hope interest was peaked or expanded on how tail scale can be used to help you and your organization embody zero trust and least privilege access.

**[40:14](https://youtube.com/watch?v=WB8uTiD6JTo&t=2414s)** But with that we'll kind of leave the rest of the time for any questions that y'all have want to make sure that if anything came up during our conversation that we can continue the dialogue.

**[40:27](https://youtube.com/watch?v=WB8uTiD6JTo&t=2427s)** We have a question so how does tail scale handle access revocation in real time, especially in scenarios where our compromised device or credential needs to be immediately locked out of the network.

**[40:42](https://youtube.com/watch?v=WB8uTiD6JTo&t=2442s)** Jordan you want to take that one.

**[40:43](https://youtube.com/watch?v=WB8uTiD6JTo&t=2443s)** I was about to let lead job because I looked like it was half typing one.

**[40:47](https://youtube.com/watch?v=WB8uTiD6JTo&t=2447s)** So tail scale has a set of keys that it creates when you provision the device.

**[40:55](https://youtube.com/watch?v=WB8uTiD6JTo&t=2455s)** If you want to if you want to revoke those keys, you basically remove its device profile from the admin console or from the control plane.

**[41:05](https://youtube.com/watch?v=WB8uTiD6JTo&t=2465s)** And as a result, it immediately revokes those keys via a netmap protocol to all the other clients essentially sends out a message to all the other clients that says.

**[41:15](https://youtube.com/watch?v=WB8uTiD6JTo&t=2475s)** If this particular device with this public key tries to communicate with you, it is no longer valid.

**[41:20](https://youtube.com/watch?v=WB8uTiD6JTo&t=2480s)** Those netmap updates happen in generally milliseconds that happened very, very quickly across the network. So when you remove a device, whether it is a machine based device that's tagged or a device that is user based.

**[41:34](https://youtube.com/watch?v=WB8uTiD6JTo&t=2494s)** Once you expire that key, it can no longer communicate in the secure network. And therefore is removed pretty instantly.

**[41:41](https://youtube.com/watch?v=WB8uTiD6JTo&t=2501s)** Any other questions or any follow on. Right.

**[42:01](https://youtube.com/watch?v=WB8uTiD6JTo&t=2521s)** We did just take a question in the Q&A. Marissa just asked in general, is it possible to build on tail scale.

**[42:06](https://youtube.com/watch?v=WB8uTiD6JTo&t=2526s)** And the answer to that is yes. So tail scale has the capability of embedding itself into other applications via TS net as job mentioned. So if you are building your applications in the go programming language.

**[42:17](https://youtube.com/watch?v=WB8uTiD6JTo&t=2537s)** We have a first class library, which we call TS net, which allows you to build directly on top of that in terms of applications.

**[42:24](https://youtube.com/watch?v=WB8uTiD6JTo&t=2544s)** Tailscale is also a connectivity platform. When you add tailscale as a client to any device or any application.

**[42:32](https://youtube.com/watch?v=WB8uTiD6JTo&t=2552s)** Tailscale handles the network connectivity for you and also handles the actual security and authentication for you via ACLs and a lot of the mechanisms that we've seen here.

**[42:41](https://youtube.com/watch?v=WB8uTiD6JTo&t=2561s)** So we have customers who are directly building on tailscale right now. And I think one of the aspirations that we have as an organization is to see tailscale become a platform that you could build on top of which lots of customers are already doing.

**[42:52](https://youtube.com/watch?v=WB8uTiD6JTo&t=2572s)** If you are interested in building other applications with all the programming languages, we do have some limited support for that that is kind of evolving as we speak.

**[43:00](https://youtube.com/watch?v=WB8uTiD6JTo&t=2580s)** So we do a lot of exciting things in that space as well. But I think the short answer guys, absolutely yes. And we are customers that are building directly on tailscale right now.

**[43:08](https://youtube.com/watch?v=WB8uTiD6JTo&t=2588s)** When we talk about everything we talked about today was kind of typical network. And we're thinking about our users and our machines.

**[43:15](https://youtube.com/watch?v=WB8uTiD6JTo&t=2595s)** When you talk about building on tailscale, we also see customers that are essentially embedding it into their software. They have the needs, whether they're deploying software or appliances inside of customer networks that are very secure.

**[43:28](https://youtube.com/watch?v=WB8uTiD6JTo&t=2608s)** And we enable them to have that one central plane across their network and the customers network.

**[43:32](https://youtube.com/watch?v=WB8uTiD6JTo&t=2612s)** So you're seeing more and more people like this actually not only just building on top of it, but building it directly into their products as well, which is exciting.

**[43:45](https://youtube.com/watch?v=WB8uTiD6JTo&t=2625s)** We recently did a blog post announcing it, but there are a bunch of development teams in the community that are not only building on tailscale but making those projects available to anyone and everyone who

**[44:00](https://youtube.com/watch?v=WB8uTiD6JTo&t=2640s)** is excited about some of the work being done that integrates tailscale. A lot of it is open source and just available for any use. So Jordan just dropped it in the chat, but definitely recommend checking out community projects. And if you have an idea for a project that you'd be really excited to build with or on tailscale, we love to hear about it and potentially help.

**[44:27](https://youtube.com/watch?v=WB8uTiD6JTo&t=2667s)** Yeah, I did add a link there to our community projects, but I think there's another kind of community probably is really interested if you are curious about this idea of building on and taking advantage of that identity.

**[44:37](https://youtube.com/watch?v=WB8uTiD6JTo&t=2677s)** It's called TSI DP that allows you to use the tailscale identity to wrap and connect to other third party services. So it is something that's picking your interest that would urge you to kind of click through there and see how they've done that. As Cindy mentioned, it's all open source and ready for

**[44:59](https://youtube.com/watch?v=WB8uTiD6JTo&t=2699s)** The other questions.

**[45:01](https://youtube.com/watch?v=WB8uTiD6JTo&t=2701s)** I think that's a question for you. Will you be at the Seattle meetup on may have no sadly not, but maybe as a couple quick plugs, we are going to be at RSA in San Francisco next week.

**[45:18](https://youtube.com/watch?v=WB8uTiD6JTo&t=2718s)** And then as Jake flagged, we are planning to be at Grafana con in Seattle in May, and we are doing a community meetup, I think around the same time, just

**[45:32](https://youtube.com/watch?v=WB8uTiD6JTo&t=2732s)** Trying to get folks together, many of whom are building on tailscale or building with tailscale and just kind of get together and share some cool stuff folks are hacking together, we can share more about that in the follow up to this, but we love talking to

**[45:48](https://youtube.com/watch?v=WB8uTiD6JTo&t=2748s)** Users, folks interested, we love learning out and going deep in the technology.

**[45:53](https://youtube.com/watch?v=WB8uTiD6JTo&t=2753s)** We also love getting feedback if you're using tailscale or feel like we should be adding new features, you have ideas, we love to have this conversation. So please come and say hi, if you're planning to be at RSA, if you're planning to be at Grafana con.

**[46:08](https://youtube.com/watch?v=WB8uTiD6JTo&t=2768s)** You know, we also are planning to be at like Dash and Falcon and GitHub universe and a bunch of other events this year and hopefully also planning support community meetup. So be on the look out and come say hi.

**[46:37](https://youtube.com/watch?v=WB8uTiD6JTo&t=2797s)** Any other questions. Alright, well, there are no other questions. I think you all, we will send the presentation recording out so you'll get it. We can also share some of the links and additional information we shared in that outreach. Thank you all so much for joining and please if you have any other questions with thoughts.

**[47:00](https://youtube.com/watch?v=WB8uTiD6JTo&t=2820s)** Even, you know, even after the webinar ends, please don't hesitate to reach out. Like I said, we love nerding out. I'm talking about this stuff with folks. So please don't be strangers and, you know, we look forward to the next time we get to connect.

**[47:14](https://youtube.com/watch?v=WB8uTiD6JTo&t=2834s)** Plus one to everything. Sydney said, great job. Thanks for having come and.

**[47:19](https://youtube.com/watch?v=WB8uTiD6JTo&t=2839s)** Alright, thanks. You all have a great week. We'll talk soon. Bye.

---

*Automatically generated transcript. May contain errors.*
