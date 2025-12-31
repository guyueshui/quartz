import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { resolveRelative } from "../util/path"
import { QuartzPluginData } from "../plugins/vfile"
import style from "./styles/recentNotes.scss"
import { GlobalConfiguration } from "../cfg"
import { i18n } from "../i18n"
import { classNames } from "../util/lang"

interface Options {
  title?: string
  limit: number
  filter: (f: QuartzPluginData) => boolean
}

const defaultOptions = (cfg: GlobalConfiguration): Options => ({
  limit: 3,
  filter: () => true,
})

function shuffleArray<T>(arr: T[]): T[] {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

export default ((userOpts?: Partial<Options>) => {
  const RandomNotes: QuartzComponent = ({
    allFiles,
    fileData,
    displayClass,
    cfg,
  }: QuartzComponentProps) => {
    const opts = { ...defaultOptions(cfg), ...userOpts }
    const pages = shuffleArray(allFiles.filter(opts.filter))
    return (
      <div class={classNames(displayClass, "random-notes")}>
        <h3>{opts.title ?? i18n(cfg.locale).components.recentNotes.title}</h3>
        <ul class="random-ul">
          {pages.slice(0, opts.limit).map((page) => {
            const title = page.frontmatter?.title ?? i18n(cfg.locale).propertyDefaults.title

            return (
              <li class="random-li">
                <h3>
                  <a href={resolveRelative(fileData.slug!, page.slug!)} class="internal">
                    {title}
                  </a>
                </h3>
              </li>
            )
          })}
        </ul>
      </div>
    )
  }

  RandomNotes.css = style
  return RandomNotes
}) satisfies QuartzComponentConstructor
