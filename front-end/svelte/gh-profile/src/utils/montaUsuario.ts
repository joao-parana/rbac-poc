import type GhRepoResponse from "../interfaces/GhRepoResponse";
import type IRepositorio from "../interfaces/IRepositorio";
import type IUsuario from "../interfaces/IUsuario";

export default function montaUsuario(
  dadosUsuario: any,
  dadosRepositorios: any,
): IUsuario {
  const repositorios_recentes = dadosRepositorios.map(
    (repositorio: GhRepoResponse) => {
      return {
        nome: repositorio.name,
        url: repositorio.html_url,
      } as IRepositorio;
    },
  );

  return {
    avatar_url: dadosUsuario.avatar_url,
    login: dadosUsuario.login,
    nome: dadosUsuario.name,
    perfil_url: dadosUsuario.html_url,
    repositorios_publicos: dadosUsuario.public_repos,
    seguidores: dadosUsuario.followers,
    repositorios_recentes,
  };
}
