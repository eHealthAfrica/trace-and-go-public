### Remove formhub.
>Wed, 29 Apr 2015 16:15:23 +0200

>Author: Lucy Chambers (lucychambers@users.noreply.github.com)

>Commiter: Lucy Chambers (lucychambers@users.noreply.github.com)

We're not using this.


### Updated requirements and travis for flake8 style guide (origin/tim/pep8, tim/pep8)
>Wed, 29 Apr 2015 14:13:02 +0000

>Author: Tim Watts (tim.watts@ehealthnigeria.org)

>Commiter: Tim Watts (tim.watts@ehealthnigeria.org)




### Fix flake issues
>Wed, 29 Apr 2015 14:07:25 +0000

>Author: Tim Watts (tim.watts@ehealthnigeria.org)

>Commiter: Tim Watts (tim.watts@ehealthnigeria.org)




### Clean up with autopep8
>Wed, 29 Apr 2015 14:01:29 +0000

>Author: Tim Watts (tim.watts@ehealthnigeria.org)

>Commiter: Tim Watts (tim.watts@ehealthnigeria.org)




### Remove Twilio Mention
>Wed, 29 Apr 2015 11:41:17 +0200

>Author: Lucy Chambers (lucychambers@users.noreply.github.com)

>Commiter: Lucy Chambers (lucychambers@users.noreply.github.com)

Twilio not used.


### Small updates
>Tue, 28 Apr 2015 18:49:50 +0200

>Author: Didi Hoffmann (didi@ribalba.de)

>Commiter: Didi Hoffmann (didi@ribalba.de)




### Minor changes to readme
>Mon, 27 Apr 2015 15:35:51 +0200

>Author: Lucy Chambers (lucychambers@users.noreply.github.com)

>Commiter: Lucy Chambers (lucychambers@users.noreply.github.com)




### Updated Readme with new understanding of project
>Mon, 27 Apr 2015 15:31:42 +0200

>Author: Lucy Chambers (lucychambers@users.noreply.github.com)

>Commiter: Lucy Chambers (lucychambers@users.noreply.github.com)

Updates from Didi.


### Fixed inverted markdown links
>Tue, 21 Apr 2015 10:23:43 +0200

>Author: Lucy Chambers (lucy@fedia.net)

>Commiter: Lucy Chambers (lucy@fedia.net)




### Add “Just admitted” as patient status
>Mon, 13 Apr 2015 16:02:31 +0000

>Author: Francesco Kirchhoff (mail@frances.co)

>Commiter: Francesco Kirchhoff (mail@frances.co)




### fix pip url for telerivet
>Mon, 13 Apr 2015 19:59:24 +0200

>Author: Lutz Paelike (lutz@delutze.de)

>Commiter: Lutz Paelike (lutz@delutze.de)




### Add “Just admitted” as patient status
>Mon, 13 Apr 2015 16:02:31 +0000

>Author: Francesco Kirchhoff (mail@frances.co)

>Commiter: Francesco Kirchhoff (mail@frances.co)




### Added that as soon as the system is queried and the patient has a status we also send this out
>Mon, 2 Mar 2015 18:57:36 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### Removed patient ID
>Wed, 11 Feb 2015 09:27:14 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### Typo in initial_message
>Wed, 11 Feb 2015 09:23:26 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### Fixed typo in sms
>Mon, 9 Feb 2015 14:55:00 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### And forgot the migration
>Fri, 6 Feb 2015 17:33:23 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### Fixed small typo
>Fri, 6 Feb 2015 17:31:28 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### Moved more sending logic into the models and updated the workings
>Fri, 6 Feb 2015 17:28:44 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### Updated the tolerative
>Mon, 2 Feb 2015 22:02:26 +0100

>Author: Didi Hoffmann (didi@ribalba.de)

>Commiter: Didi Hoffmann (didi@ribalba.de)




### When the status is sent, we obviously want to send the text and not the char.
>Mon, 2 Feb 2015 21:55:27 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### - Admin update - error fixing - wording in extra file
>Fri, 30 Jan 2015 17:04:53 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### Added a method to stop people from trying to brute force codes
>Thu, 11 Dec 2014 19:04:10 +0000

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### Added a wordings file so people can edit it easily
>Thu, 11 Dec 2014 18:44:53 +0000

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### A lot of refactoring: - Deleted the etu model and moved everything into core - Changed the Patient model to reflect the things we are seeing on the ground - Changed the workflow to webhooks and not queries - Changed the API to AUTH always - Deleted the possibility to add eval methods as we will always only have one - General cleanup
>Thu, 11 Dec 2014 18:40:11 +0000

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### More features: - Added support for rapidpro.io - Added phone number cleanup
>Thu, 11 Dec 2014 11:36:51 +0000

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### Add test for PATCH
>Wed, 3 Dec 2014 14:16:24 +0700

>Author: Simon (svansintjan@gmail.com)

>Commiter: Simon (svansintjan@gmail.com)




### basics for API test, POST and GET
>Wed, 3 Dec 2014 14:09:07 +0700

>Author: Simon (svansintjan@gmail.com)

>Commiter: Simon (svansintjan@gmail.com)




### Add reference to PATCH method in README
>Wed, 3 Dec 2014 11:09:09 +0700

>Author: Simon (svansintjan@gmail.com)

>Commiter: Simon (svansintjan@gmail.com)




### Tweak documentation
>Wed, 3 Dec 2014 10:59:12 +0700

>Author: Simon (svansintjan@gmail.com)

>Commiter: Simon (svansintjan@gmail.com)




### Add Filter, Search, and README
>Wed, 3 Dec 2014 10:52:48 +0700

>Author: Simon (svansintjan@gmail.com)

>Commiter: Simon (svansintjan@gmail.com)

* Add django-filter to requirements.txt
* Add filters based on alive, age, first_name, and last_name
* Add search fields based on first_name, last_name



### Add initial API
>Wed, 3 Dec 2014 09:10:36 +0700

>Author: Simon (svansintjan@gmail.com)

>Commiter: Simon (svansintjan@gmail.com)

* Add Django Rest Framework as a requirement
* Initialize the initial API folder structure
* Add a patient serializer
* Add a patient viewset



### Added logo
>Tue, 25 Nov 2014 23:18:12 +0100

>Author: Dietger Hoffmann (didi@ribalba.de)

>Commiter: Dietger Hoffmann (didi@ribalba.de)




### updated license
>Tue, 25 Nov 2014 14:09:50 +0100

>Author: Fox (ffffux@users.noreply.github.com)

>Commiter: Fox (ffffux@users.noreply.github.com)




### Added about us
>Mon, 24 Nov 2014 19:00:10 +0100

>Author: Didi Hoffmann (didi@ribalba.de)

>Commiter: Didi Hoffmann (didi@ribalba.de)




### gender-neutral terms
>Mon, 24 Nov 2014 18:54:15 +0100

>Author: Fox (ffffux@users.noreply.github.com)

>Commiter: Fox (ffffux@users.noreply.github.com)




### Added the contribution
>Mon, 24 Nov 2014 18:47:34 +0100

>Author: Didi Hoffmann (didi@ribalba.de)

>Commiter: Didi Hoffmann (didi@ribalba.de)




### Added my contact data
>Mon, 24 Nov 2014 18:39:29 +0100

>Author: Didi Hoffmann (didi@ribalba.de)

>Commiter: Didi Hoffmann (didi@ribalba.de)




### A little more detail for the readme
>Mon, 24 Nov 2014 18:37:23 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### Update README.md
>Mon, 24 Nov 2014 18:26:40 +0100

>Author: Fox (ffffux@users.noreply.github.com)

>Commiter: Fox (ffffux@users.noreply.github.com)




### Update README.md
>Mon, 24 Nov 2014 18:24:44 +0100

>Author: Fox (ffffux@users.noreply.github.com)

>Commiter: Fox (ffffux@users.noreply.github.com)




### Added Version 2.0 Apache
>Mon, 24 Nov 2014 18:24:07 +0100

>Author: Didi Hoffmann (didi@ribalba.de)

>Commiter: Didi Hoffmann (didi@ribalba.de)




### Removed the old code to send messages with a delay
>Mon, 24 Nov 2014 18:19:08 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### Rename
>Mon, 24 Nov 2014 17:45:53 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### Added initial patient data form for formhub
>Mon, 24 Nov 2014 17:40:22 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### General repo cleanup
>Mon, 24 Nov 2014 16:11:16 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### Small initial install
>Mon, 24 Nov 2014 15:54:25 +0100

>Author: Didi Hoffmann (didi@ribalba.de)

>Commiter: Didi Hoffmann (didi@ribalba.de)




### Started writing the description of the services
>Mon, 24 Nov 2014 15:42:06 +0100

>Author: Didi Hoffmann (didi@ribalba.de)

>Commiter: Didi Hoffmann (didi@ribalba.de)




### Created the initial readme.md
>Mon, 24 Nov 2014 13:13:53 +0100

>Author: Didi Hoffmann (didi@ribalba.de)

>Commiter: Didi Hoffmann (didi@ribalba.de)




### Added case insensitivity to the queries
>Thu, 20 Nov 2014 19:07:57 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




### Initial import
>Thu, 13 Nov 2014 22:55:18 +0100

>Author: Didi Hoffmann (didi@rebelproject.org)

>Commiter: Didi Hoffmann (didi@rebelproject.org)




