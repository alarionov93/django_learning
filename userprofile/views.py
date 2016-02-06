from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from userprofile.forms import UserProfileForm
from django.contrib.auth.decorators import login_required


@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            # TODO: use url name here!
            return HttpResponseRedirect('/accounts/profile/')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)
    args = {}
    args.update(csrf(request))

    args['form'] = form
    args['user_p'] = request.user
    full_name = '%s %s' % (request.user.first_name, request.user.last_name, )
    args['full_name'] = full_name

    return render_to_response('profile.html', args)


def redirect_to_login(request):
    return HttpResponseRedirect('/core/accounts/login/?next=/accounts/profile/')
