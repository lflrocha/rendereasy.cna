Introduction
============

This is a full-blown functional test. The emphasis here is on testing what
the user may input and see, and the system is largely tested as a black box.
We use PloneTestCase to set up this test as well, so we have a full Plone site
to play with. We *can* inspect the state of the portal, e.g. using 
self.portal and self.folder, but it is often frowned upon since you are not
treating the system as a black box. Also, if you, for example, log in or set
roles using calls like self.setRoles(), these are not reflected in the test
browser, which runs as a separate session.

Being a doctest, we can tell a story here.

First, we must perform some setup. We use the testbrowser that is shipped
with Five, as this provides proper Zope 2 integration. Most of the 
documentation, though, is in the underlying zope.testbrower package.

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()

The following is useful when writing and debugging testbrowser tests. It lets
us see all error messages in the error_log.

    >>> self.portal.error_log._ignored_exceptions = ()

With that in place, we can go to the portal front page and log in. We will
do this using the default user from PloneTestCase:

    >>> from Products.PloneTestCase.setup import portal_owner, default_password

Because add-on themes or products may remove or hide the login portlet, this test will use the login form that comes with plone.  

    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()

Here, we set the value of the fields on the login form and then simulate a
submit click.  We then ensure that we get the friendly logged-in message:

    >>> "You are now logged in" in browser.contents
    True

Finally, let's return to the front page of our site before continuing

    >>> browser.open(portal_url)

-*- extra stuff goes here -*-
The CNA Destaques content type
===============================

In this section we are tesing the CNA Destaques content type by performing
basic operations like adding, updadating and deleting CNA Destaques content
items.

Adding a new CNA Destaques content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'CNA Destaques' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CNA Destaques').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CNA Destaques' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CNA Destaques Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'CNA Destaques' content item to the portal.

Updating an existing CNA Destaques content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New CNA Destaques Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New CNA Destaques Sample' in browser.contents
    True

Removing a/an CNA Destaques content item
--------------------------------

If we go to the home page, we can see a tab with the 'New CNA Destaques
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New CNA Destaques Sample' in browser.contents
    True

Now we are going to delete the 'New CNA Destaques Sample' object. First we
go to the contents tab and select the 'New CNA Destaques Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New CNA Destaques Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New CNA Destaques
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New CNA Destaques Sample' in browser.contents
    False

Adding a new CNA Destaques content item as contributor
------------------------------------------------

Not only site managers are allowed to add CNA Destaques content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'CNA Destaques' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CNA Destaques').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CNA Destaques' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CNA Destaques Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new CNA Destaques content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The CNA Destaque content type
===============================

In this section we are tesing the CNA Destaque content type by performing
basic operations like adding, updadating and deleting CNA Destaque content
items.

Adding a new CNA Destaque content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'CNA Destaque' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CNA Destaque').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CNA Destaque' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CNA Destaque Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'CNA Destaque' content item to the portal.

Updating an existing CNA Destaque content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New CNA Destaque Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New CNA Destaque Sample' in browser.contents
    True

Removing a/an CNA Destaque content item
--------------------------------

If we go to the home page, we can see a tab with the 'New CNA Destaque
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New CNA Destaque Sample' in browser.contents
    True

Now we are going to delete the 'New CNA Destaque Sample' object. First we
go to the contents tab and select the 'New CNA Destaque Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New CNA Destaque Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New CNA Destaque
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New CNA Destaque Sample' in browser.contents
    False

Adding a new CNA Destaque content item as contributor
------------------------------------------------

Not only site managers are allowed to add CNA Destaque content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'CNA Destaque' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CNA Destaque').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CNA Destaque' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CNA Destaque Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new CNA Destaque content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Card content type
===============================

In this section we are tesing the Card content type by performing
basic operations like adding, updadating and deleting Card content
items.

Adding a new Card content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Card' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Card').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Card' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Card Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Card' content item to the portal.

Updating an existing Card content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Card Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Card Sample' in browser.contents
    True

Removing a/an Card content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Card
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Card Sample' in browser.contents
    True

Now we are going to delete the 'New Card Sample' object. First we
go to the contents tab and select the 'New Card Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Card Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Card
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Card Sample' in browser.contents
    False

Adding a new Card content item as contributor
------------------------------------------------

Not only site managers are allowed to add Card content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Card' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Card').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Card' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Card Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Card content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Instagram content type
===============================

In this section we are tesing the Instagram content type by performing
basic operations like adding, updadating and deleting Instagram content
items.

Adding a new Instagram content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Instagram' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Instagram').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Instagram' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Instagram Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Instagram' content item to the portal.

Updating an existing Instagram content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Instagram Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Instagram Sample' in browser.contents
    True

Removing a/an Instagram content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Instagram
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Instagram Sample' in browser.contents
    True

Now we are going to delete the 'New Instagram Sample' object. First we
go to the contents tab and select the 'New Instagram Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Instagram Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Instagram
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Instagram Sample' in browser.contents
    False

Adding a new Instagram content item as contributor
------------------------------------------------

Not only site managers are allowed to add Instagram content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Instagram' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Instagram').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Instagram' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Instagram Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Instagram content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Twitter content type
===============================

In this section we are tesing the Twitter content type by performing
basic operations like adding, updadating and deleting Twitter content
items.

Adding a new Twitter content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Twitter' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Twitter').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Twitter' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Twitter Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Twitter' content item to the portal.

Updating an existing Twitter content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Twitter Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Twitter Sample' in browser.contents
    True

Removing a/an Twitter content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Twitter
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Twitter Sample' in browser.contents
    True

Now we are going to delete the 'New Twitter Sample' object. First we
go to the contents tab and select the 'New Twitter Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Twitter Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Twitter
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Twitter Sample' in browser.contents
    False

Adding a new Twitter content item as contributor
------------------------------------------------

Not only site managers are allowed to add Twitter content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Twitter' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Twitter').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Twitter' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Twitter Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Twitter content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Pergunta Resposta content type
===============================

In this section we are tesing the Pergunta Resposta content type by performing
basic operations like adding, updadating and deleting Pergunta Resposta content
items.

Adding a new Pergunta Resposta content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Pergunta Resposta' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Pergunta Resposta').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Pergunta Resposta' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Pergunta Resposta Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Pergunta Resposta' content item to the portal.

Updating an existing Pergunta Resposta content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Pergunta Resposta Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Pergunta Resposta Sample' in browser.contents
    True

Removing a/an Pergunta Resposta content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Pergunta Resposta
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Pergunta Resposta Sample' in browser.contents
    True

Now we are going to delete the 'New Pergunta Resposta Sample' object. First we
go to the contents tab and select the 'New Pergunta Resposta Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Pergunta Resposta Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Pergunta Resposta
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Pergunta Resposta Sample' in browser.contents
    False

Adding a new Pergunta Resposta content item as contributor
------------------------------------------------

Not only site managers are allowed to add Pergunta Resposta content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Pergunta Resposta' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Pergunta Resposta').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Pergunta Resposta' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Pergunta Resposta Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Pergunta Resposta content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Vinheta content type
===============================

In this section we are tesing the Vinheta content type by performing
basic operations like adding, updadating and deleting Vinheta content
items.

Adding a new Vinheta content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Vinheta' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Vinheta').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Vinheta' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Vinheta Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Vinheta' content item to the portal.

Updating an existing Vinheta content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Vinheta Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Vinheta Sample' in browser.contents
    True

Removing a/an Vinheta content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Vinheta
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Vinheta Sample' in browser.contents
    True

Now we are going to delete the 'New Vinheta Sample' object. First we
go to the contents tab and select the 'New Vinheta Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Vinheta Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Vinheta
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Vinheta Sample' in browser.contents
    False

Adding a new Vinheta content item as contributor
------------------------------------------------

Not only site managers are allowed to add Vinheta content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Vinheta' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Vinheta').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Vinheta' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Vinheta Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Vinheta content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Coluna content type
===============================

In this section we are tesing the Coluna content type by performing
basic operations like adding, updadating and deleting Coluna content
items.

Adding a new Coluna content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Coluna' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Coluna').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Coluna' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Coluna Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Coluna' content item to the portal.

Updating an existing Coluna content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Coluna Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Coluna Sample' in browser.contents
    True

Removing a/an Coluna content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Coluna
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Coluna Sample' in browser.contents
    True

Now we are going to delete the 'New Coluna Sample' object. First we
go to the contents tab and select the 'New Coluna Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Coluna Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Coluna
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Coluna Sample' in browser.contents
    False

Adding a new Coluna content item as contributor
------------------------------------------------

Not only site managers are allowed to add Coluna content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Coluna' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Coluna').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Coluna' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Coluna Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Coluna content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Foto content type
===============================

In this section we are tesing the Foto content type by performing
basic operations like adding, updadating and deleting Foto content
items.

Adding a new Foto content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Foto' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Foto').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Foto' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Foto Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Foto' content item to the portal.

Updating an existing Foto content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Foto Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Foto Sample' in browser.contents
    True

Removing a/an Foto content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Foto
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Foto Sample' in browser.contents
    True

Now we are going to delete the 'New Foto Sample' object. First we
go to the contents tab and select the 'New Foto Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Foto Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Foto
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Foto Sample' in browser.contents
    False

Adding a new Foto content item as contributor
------------------------------------------------

Not only site managers are allowed to add Foto content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Foto' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Foto').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Foto' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Foto Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Foto content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Album content type
===============================

In this section we are tesing the Album content type by performing
basic operations like adding, updadating and deleting Album content
items.

Adding a new Album content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Album' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Album').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Album' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Album Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Album' content item to the portal.

Updating an existing Album content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Album Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Album Sample' in browser.contents
    True

Removing a/an Album content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Album
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Album Sample' in browser.contents
    True

Now we are going to delete the 'New Album Sample' object. First we
go to the contents tab and select the 'New Album Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Album Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Album
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Album Sample' in browser.contents
    False

Adding a new Album content item as contributor
------------------------------------------------

Not only site managers are allowed to add Album content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Album' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Album').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Album' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Album Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Album content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)



