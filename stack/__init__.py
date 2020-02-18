import os

USE_DOKKU = os.environ.get("USE_DOKKU") == "on"
USE_EB = os.environ.get("USE_EB") == "on"
USE_EC2 = os.environ.get("USE_EC2") == "on"
USE_ECS = os.environ.get("USE_ECS") == "on"
USE_EKS = os.environ.get("USE_EKS") == "on"
USE_GOVCLOUD = os.environ.get("USE_GOVCLOUD") == "on"
USE_NAT_GATEWAY = os.environ.get("USE_NAT_GATEWAY") == "on"

if USE_EKS:
    from . import vpc  # noqa: F401
    from . import template
    from . import repository  # noqa: F401
    from . import eks  # noqa: F401
else:
    from . import sftp  # noqa: F401
    from . import assets  # noqa: F401
    from . import cache  # noqa: F401
    from . import database  # noqa: F401
    from . import logs  # noqa: F401
    from . import vpc  # noqa: F401
    from . import template

    if not USE_GOVCLOUD:
        # make sure this isn't added to the template for GovCloud, as it's not
        # supported in this region
        from . import search  # noqa: F401

    if USE_NAT_GATEWAY:
        from . import bastion  # noqa: F401

    if USE_ECS:
        from . import repository  # noqa: F401
        from . import ecs_cluster  # noqa: F401
    elif USE_EB:
        from . import repository  # noqa: F401
        from . import eb  # noqa: F401
    elif USE_DOKKU:
        from . import dokku  # noqa: F401
    elif USE_EC2 or USE_GOVCLOUD:
        # USE_GOVCLOUD and USE_EC2 both provide EC2 instances
        from . import instances  # noqa: F401

# Must be last to tag all resources
from . import tags  # noqa: F401

print(template.template.to_yaml())
