import consistent_hash
db_dict = { 'heiniu_102':1,'heiniu_103':1,'heiniu_104':1}
consistent_hash = consistent_hash.ConsistentHash(db_dict)
seed = '13691036309_130124198312063310'
db_name = consistent_hash.get_node(seed)
  
print db_name
