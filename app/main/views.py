from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required,current_user
from ..models import User,Post,Like,Dislike,Comment
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

@main.route('/upvote/<id>', methods=['GET', 'POST'])
@login_required
def like(id):
    data = Like.get_like(id)
    output = f'{current_user.id}:{id}'
    for vote in data:
        res = f'{vote}'
        if output == res:
            return redirect(url_for('main.index', id=id))
        else:
            continue
    new_upvote = Like(post_id=id)
    new_upvote.save_like()
    return redirect(url_for('main.index', id=id))

@main.route('/downvote/<id>', methods=['GET', 'POST'])
@login_required
def dislike(id):   
    data = Dislike.get_dislike(id)
    output = f'{current_user.id}:{id}'
    for vote in data:
        res = f'{vote}'
        if output == res:
            return redirect(url_for('main.index', id=id))
        else:
            continue
    new_downvote = Dislike(post_id=id)
    new_downvote.save_dislike()
    return redirect(url_for('main.index', id=id))
    
@main.route('/comment/<id>', methods=['GET', 'POST'])
@login_required
def comment(id):
    comment_form = CommentForm()
    post = Post.query.get(id)
    fetch_all_comments = Comment.query.filter_by(post_id=id).all()
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        p_id = id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment=comment, user_id=user_id, post_id=p_id)
        new_comment.save_comment()
        return redirect(url_for('.comment', id=p_id))
    return render_template('comment.html', comment_form=comment_form, post=post, all_comments=fetch_all_comments)