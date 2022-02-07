from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required
from ..models import User,Post
from .forms import PitchForm,CommentForm

# views
@main.route("/")
def index():
    post=Post.query.all()
    pickup=Post.query.filter_by(category='pickup').all()
    interview=Post.query.filter_by(category='interview').all()
    product=Post.query.filter_by(category='product').all()
    promotion=Post.query.filter_by(category='promotion').all()

    '''View root page function that returns the index page and its data'''
    return render_template('index.html',posts=post,pickup=pickup,interview=interview,product=product,promotion=promotion)


@main.route("/pitch",methods=['GET','POST'])
@login_required
def pitch():
    pitch=PitchForm()
    if pitch.validate_on_submit():
        title=pitch.title.data
        category=pitch.category.data
        body=pitch.content.data
        new_post=Post(title=title,category=category,content=body)
        Post.save_post(new_post)
        return redirect(url_for('.index'))
    return render_template("pitch.html",pitch_form=pitch)

@main.route("/comment",methods=['GET','POST'])
@login_required
def comment():
    comment=CommentForm()
    return render_template("comment.html",comment_form=comment)    

