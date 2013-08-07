#!/usr/bin/python
# -*- coding: utf-8 -*-

from zope.interface import Interface
from zope.interface import implements
from Products.Five import BrowserView

class ITraverseUid(Interface):

    pass

class Browser(BrowserView):

    implements(ITraverseUid)


    def __bobo_traverse__(self, REQUEST, uid):
        """ """
        context=self.context
        rc=context.getAdapter('rc')()

        sub_path=list(REQUEST['TraversalRequestNameStack'])
        sub_path.reverse()

        object_=rc.lookupObject(uid)
        return object_.restrictedTraverse('/'.join(sub_path))
