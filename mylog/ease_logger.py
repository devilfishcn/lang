
import logging
access_log = logging.getLogger('china.beijing.fengtai.shanyucheng')
logging.basicConfig()
# access_log.setLevel('INFO')
access_log.info('xx')

my_log = logging.getLogger('china.beijing.fengtai.shanyucheng.102')
my_log.setLevel('INFO')
my_log.info('xx')