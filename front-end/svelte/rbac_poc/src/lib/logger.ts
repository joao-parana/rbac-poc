// FILE: src/lib/logger.ts
import { env } from '$lib/environment';

export const logger = {
	info: (message: string, data?: object) => {
		if (env.isProd) {
			console.log(
				JSON.stringify({
					level: 'info',
					time: new Date().toISOString(),
					message,
					...data
				})
			);
		}
		if (env.isDev) {
			console.log(message, data);
		}
	},
	error: (error: unknown) => {
		console.log('Debugando o método logger.error ! ', error);
		console.error(
			JSON.stringify({
				level: 'error',
				time: new Date().toISOString(),
				error: error instanceof Error ? error.stack : String(error)
			})
		);
	}
};
