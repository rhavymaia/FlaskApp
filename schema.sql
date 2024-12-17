create table tb_propriedades (
  id serial PRIMARY KEY,
  nome varchar(50) NOT NULL,
  cidade TEXT NOT NULL
);

create table tb_cidades (
  id serial PRIMARY KEY,
  nome varchar(50) NOT NULL,
  uf varchar(2) NOT NULL
);

COMMIT;