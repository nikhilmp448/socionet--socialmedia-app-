from api.views import BlacklistTokenUpdateView
from blockUser.views import UserBlockViewSet
from fgroups.views import group_memberViewSet, groupViewSet
from friends.views import FollowViewSet
from votes.views import VoteViewSet
from comments.views import CommentViewSet
from posts.views import PostViewSet, storyViewSet
from django.urls import path
from users import views as userview
from rest_framework.routers import DefaultRouter
from users.views import UserRegisterViewSet, UserViewSet, UsersearchView
from user_profile.views import ProfileViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
urlpatterns=[
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/blacklist/',BlacklistTokenUpdateView.as_view(),name="blacklist"),

    # path('password/change/',userview.password_change,name="password-change"),
    path('users_search/', UsersearchView.as_view(), name='user-list'),
]
############# USER API #####################

router.register(r'UserRegister',UserRegisterViewSet,basename='UserRegister')
router.register(r'users', UserViewSet,basename='users')
router.register(r'profiles',ProfileViewSet)

router.register(r'Blocked',UserBlockViewSet,basename='Blocked')


############# POST ACTION API #####################

router.register(r'posts',PostViewSet)
router.register(r'comments',CommentViewSet)
router.register(r'votes',VoteViewSet)
router.register(r'story',storyViewSet)


############# FRIENDS API #####################

router.register(r'follow',FollowViewSet,basename='follow')

############# GROUP API #####################

router.register(r'group',groupViewSet,basename='group')
router.register(r'group_member',group_memberViewSet,basename='group_member')

urlpatterns=urlpatterns+router.urls