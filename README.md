django-ember-tag
================

Simple helper tag for using ember in django templates

Install
-------

Place ember.py into your app templatetags module:

    your_project_root
      +-your_app
         +-templatetags
         |  +- __init__.py
         |  +- ember.py
         +- models.py
         +- tests.py
         +- views.py
         
Usage
-----
         
In the template, load the ember helper tags and use:

  {% ember #<tagname> [arg1] [arg2] [argN] %} ... {% ember /<tagname> %}
  
  {% ember <variable> %}


Example:

    {% load ember %}

    <ul class="nav">
        <li>{% linkto "index" %}{% trans "Home" %}{% endlinkto %}</li>
        <li>{% linkto "about" %}{% trans "About" %}{% endlinkto %}</li>
        <li>{% linkto "blog" %}{% trans "Blog" %}{% endlinkto %}</li>
        <li>{% linkto "blog" %}{% trans "Blog" %}{% endlinkto %}</li>
    </ul>
    
    {% ember #if isAuthenticated %}
        <ul class="nav pull-right">
            <li><i class="icon-user"></i> {% ember User.email %}</li>
            <li>{% linkto "logout" %}<i class="icon-signout"></i>{% endlinkto %}</li>            
        </div>
    {% ember else %}
        <form class="navbar-form pull-right">
            <input class="span2" type="text" placeholder="{% trans "Email" %}">
            <input class="span2" type="password" placeholder="{% trans "Password" %}">
            <button type="submit" class="btn">{% trans "Login" %}</button>
        </form>
    {% ember /if %}

Resulting HTML after rendering (with Brazilian Portuguese locale):

    <ul class="nav">
        <li>{{#linkTo "index"}}Início{{/linkTo}}</li>
        <li>{{#linkTo "about"}}Sobre{{/linkTo}}</li>
        <li>{{#linkTo "blog"}}Notícias{{/linkTo}}</li>
        <li>{{#linkTo "help"}}Ajuda{{/linkTo}}</li>
        </li>
    </ul>
    {{#if isAuthenticated}}
        <div class="pull-right">
            <ul class="nav pull-right">
                <li><i class="icon-user"></i> {% ember User.email %}</li>
                <li>{% linkto "logout" %}<i class="icon-signout"></i>{% endlinkto %}</li>            
            </div>
        </div>
    {{else}}
        <form class="navbar-form pull-right">
            <input class="span2" type="text" placeholder="Email">
            <input class="span2" type="password" placeholder="Senha">
            <button type="submit" class="btn">Login</button>
        </form>
    {{/if}}
