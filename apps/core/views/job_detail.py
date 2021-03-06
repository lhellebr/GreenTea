# Author: Pavel Studenik <pstudeni@redhat.com>
# Date: 24.9.2013

"""View for job detail page"""

from django.conf import settings
from django.core.paginator import Paginator
from django.views.generic import TemplateView

from apps.core.models import Job, JobTemplate


class JobDetailView(TemplateView):

    """Show all runs of the job"""
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)

        jobt_id = kwargs["id"]
        jobt = JobTemplate.objects.get(id=jobt_id)
        jobs_list = Job.objects.filter(
            template=jobt).order_by("-schedule__counter")
        paginator = Paginator(jobs_list, settings.PAGINATOR_OBJECTS_ONPAGE)
        jobs = paginator.page(int(self.request.GET.get('page', 1)))

        context.update({
            "jobtemplate": jobt,
            "jobs": jobs,
            "paginator": paginator,
        })
        return context
