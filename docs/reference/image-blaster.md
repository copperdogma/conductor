# image-blaster

- **Canonical project:** [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster)
- **Capability:** Claude skill pipeline for turning an image into 3D scene assets.
- **Useful when:** exploring photo-based worlds, game-environment prototypes,
  or film-location previz. These are future possibilities, not current commitments.
- **Tags:** image-to-3D, world-generation, meshes, gaussian-splats, game-dev, previz
- **Last checked:** 2026-10-24
- **Evidence:** Source-checked; no local installation or generation test.
- **Disposition:** Keep for future use; no present adoption recommendation.

## Small scout

The repository and its README exist. The documented outputs include object
meshes (`.glb`/`.obj`), an environment Gaussian splat (`.spz`), and ambient/object
sound (`.mp3`). It orchestrates Claude, World Labs, and FAL; it is not a
standalone local model. The example configuration requires World Labs and FAL
API keys. Code is MIT licensed; provider services and generated assets need
separate terms/cost checks before use.

The post's “any photo,” physics, and five-minute claims are unverified here.
The README also advertises sub-five-minute generation, but this source check
does not demonstrate timing, fidelity, collision behavior, or game-ready output.

## Sources and provenance

- [Discovery post by @liambraus](https://x.com/liambraus/status/2106383261089849825)
  and [author's repository reply](https://x.com/liambraus/status/2106383264282026459):
  retrieved through Twitter Scraper; names image-blaster and supplies a short link.
- The short link `https://t.co/agY7s0DE4f` could not be opened by the web tool.
  Search located the matching named upstream repository, whose own README
  identifies `neilsonnn/image-blaster`; the short-link redirect itself remains
  unverified.
- [Upstream README](https://github.com/neilsonnn/image-blaster#readme)
- [Example configuration](https://github.com/neilsonnn/image-blaster/blob/main/.env.example)
- [License](https://github.com/neilsonnn/image-blaster/blob/main/LICENSE.md)

## Revisit when

A future project needs an image-derived 3D environment. Then recheck maintenance,
provider availability, pricing and rights, and try one non-private image against
that project's actual navigation, asset, and performance requirements.
